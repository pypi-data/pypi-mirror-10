'''This module defines a base class for optimization techniques.'''

import climate
import collections
import numpy as np
import theano
import theano.tensor as TT

from . import util

logging = climate.get_logger(__name__)


def build(algo, loss, params, inputs, updates=(), monitors=(),
          monitor_gradients=False):
    '''Construct an optimizer by name.

    Parameters
    ----------
    algo : str
        The name of the optimization algorithm to build.
    loss : Theano expression
        Loss function to minimize. This must be a scalar-valued expression.
    params : list of Theano variables
        Symbolic variables to adjust to minimize the loss.
    inputs : list of Theano variables
        Symbolic variables required to compute the loss.
    updates : list of update pairs, optional
        A list of pairs providing updates for the internal of the loss
        computation. Normally this is empty, but it can be provided if the loss,
        for example, requires an update to an internal random number generator.
    monitors : dict or sequence of (str, Theano expression) tuples, optional
        Additional values to monitor during optimization. These must be provided
        as either a sequence of (name, expression) tuples, or as a dictionary
        mapping string names to Theano expressions.
    monitor_gradients : bool, optional
        If True, add monitors to log the norms of the parameter gradients during
        optimization. Defaults to False.

    Returns
    -------
    optimizer : :class:`Optimizer`
        An optimizer instance.
    '''
    return Optimizer.build(algo, loss, params, inputs,
                           updates=updates, monitors=monitors,
                           monitor_gradients=monitor_gradients)


class Optimizer(util.Registrar(str('Base'), (), {})):
    '''An optimizer computes gradient updates to iteratively optimize a loss.

    Parameters
    ----------
    loss : Theano expression
        Loss function to minimize. This must be a scalar-valued expression.
    params : list of Theano variables
        Symbolic variables to adjust to minimize the loss.
    inputs : list of Theano variables
        Symbolic variables required to compute the loss.
    updates : list of update pairs, optional
        A list of pairs providing updates for the internal of the loss
        computation. Normally this is empty, but it can be provided if the loss,
        for example, requires an update to an internal random number generator.
    monitors : dict or sequence of (str, Theano expression) tuples, optional
        Additional values to monitor during optimization. These must be provided
        as either a sequence of (name, expression) tuples, or as a dictionary
        mapping string names to Theano expressions.
    monitor_gradients : bool, optional
        If True, add monitors to log the norms of the parameter gradients during
        optimization. Defaults to False.
    '''

    def __init__(self, loss, params, inputs, updates=(), monitors=(),
                 monitor_gradients=False):
        self._loss = loss
        self._params = params
        self._inputs = inputs
        self._updates = updates
        if hasattr(updates, 'items') and callable(updates.items):
            self._updates = updates.items()

        self._shapes = [p.get_value(borrow=True).shape for p in self._params]
        self._counts = [np.prod(s) for s in self._shapes]
        self._starts = np.cumsum([0] + self._counts)[:-1]
        self._dtype = self._params[0].get_value().dtype

        self._curr_iter = 0
        self._best_iter = 0
        self._best_loss = 1e100
        self._best_params = [p.get_value().copy() for p in self._params]

        if hasattr(monitors, 'items') and callable(monitors.items):
            monitors = monitors.items()
        self._monitor_exprs = [self._loss]
        self._monitor_names = ['loss']
        for name, monitor in monitors:
            self._monitor_names.append(name)
            self._monitor_exprs.append(monitor)
        if monitor_gradients:
            for p, g in zip(self._params, TT.grad(self._loss, self._params)):
                self._monitor_names.append('∂{}'.format(p.name))
                self._monitor_exprs.append((g * g).sum())

    def _compile(self):
        '''Compile the Theano functions for evaluating and updating our model.
        '''
        logging.info('compiling evaluation function')
        self.f_eval = theano.function(
            self._inputs, self._monitor_exprs, updates=self._updates)
        logging.info('compiling %s step function', self.__class__.__name__)
        updates = list(self._updates) + list(self._get_updates())
        self.f_step = theano.function(
            self._inputs, self._monitor_exprs, updates=updates)

    def _get_updates(self):
        '''Get parameter update expressions for performing optimization.

        Returns
        -------
        updates : sequence of (parameter, expression) tuples
            A sequence of parameter updates to be applied during optimization.
        '''
        for param, grad in self._differentiate():
            for var, expr in self._get_updates_for(param, grad):
                if self.momentum == 0 or var != param:
                    yield var, expr
                    continue
                delta = expr - param
                vel_tm1 = util.shared_like(param, 'vel')
                vel_t = self.momentum * vel_tm1 + delta
                yield vel_tm1, vel_t
                if self.nesterov:
                    # see http://arxiv.org/pdf/1212.0901v2.pdf (eq 7) and
                    # https://github.com/lisa-lab/pylearn2/pull/136#issuecomment-10381617
                    yield param, (param + self.momentum ** 2 * vel_tm1
                                  + (1 + self.momentum) * delta)
                else:
                    yield param, param + vel_t

    def _get_updates_for(self, param, grad):
        '''Generate some update pairs for the given model parameter.

        Returns
        -------
        updates : sequence of (parameter, expression) tuples
            A sequence of parameter updates to be applied during optimization.
        '''
        raise NotImplementedError

    def _differentiate(self, params=None):
        '''Return a sequence of gradients for our parameters.

        This method applies gradient norm clipping, so if a gradient has a norm
        that exceeds the threshold, it will be rescaled to fit within the norm
        threshold.

        Parameters
        ----------
        params : list of Theano variables, optional
            Return the gradient with respect to these parameters. Defaults to
            all parameters that the optimizer knows about.

        Returns
        -------
        pairs : sequence of (param, grad) tuples
            Generates a sequence of tuples representing each of the parameters
            requested and the corresponding Theano gradient expressions.
        '''
        if params is None:
            params = self._params
        for param, grad in zip(params, TT.grad(self._loss, params)):
            norm = TT.sqrt((grad * grad).sum())
            yield param, TT.clip(
                grad * TT.minimum(1, self.max_gradient_norm / norm),
                -self.max_gradient_clip, self.max_gradient_clip)

    def set_params(self, targets):
        '''Set the values of the parameters to the given target values.

        Parameters
        ----------
        targets : sequence of ndarray
            Arrays for setting the parameters of our model.
        '''
        for param, target in zip(self._params, targets):
            param.set_value(target)

    def _log(self, monitors, iteration, label='', suffix=''):
        '''Log the state of the optimizer through the logging system.

        Parameters
        ----------
        monitors : OrderedDict
            A dictionary of monitor names mapped to values. These names and
            values are what is being logged.
        iteration : int
            Optimization iteration that we are logging.
        label : str, optional
            A label for the name of the optimizer creating the log line.
            Defaults to the name of the current class.
        suffix : str, optional
            A suffix to add to the end of the log line, if any.
        '''
        label = label or self.__class__.__name__
        fields = (('{}={:.6f}').format(k, v) for k, v in monitors.items())
        logging.info('%s %i %s%s', label, iteration, ' '.join(fields), suffix)

    def evaluate(self, dataset):
        '''Evaluate the current model parameters on a dataset.

        Parameters
        ----------
        dataset : :class:`Dataset <downhill.dataset.Dataset>`
            A set of data to use for evaluating the model.

        Returns
        -------
        monitors : OrderedDict
            A dictionary mapping monitor names to values. Monitors are
            quantities of interest during optimization---for example, loss
            function, accuracy, or whatever the optimization task requires.
        '''
        values = [self.f_eval(*x) for x in dataset]
        monitors = zip(self._monitor_names, np.mean(values, axis=0))
        return collections.OrderedDict(monitors)

    def _test_patience(self, monitors):
        '''Test whether our patience with optimization has elapsed.

        Parameters
        ----------
        monitors : dict
            A dictionary mapping monitor names to values. The 'loss' key from
            this dictionary will be used to evaluate optimization progress.

        Returns
        -------
        elapsed : bool
            True iff our patience has elapsed and the model is no longer
            improving.
        '''
        self._curr_iter += 1
        marker = ''
        loss = monitors['loss']
        if self._best_loss - loss > self._best_loss * self.min_improvement:
            self._best_loss = loss
            self._best_iter = self._curr_iter
            self._best_params = [p.get_value().copy() for p in self._params]
            marker = ' *'
        self._log(monitors, self._curr_iter - 1, 'validation', marker)
        return self._curr_iter - self._best_iter > self.patience

    def _prepare(self, **kwargs):
        '''Set up properties for optimization.

        This method can be overridden by base classes to provide parameters that
        are specific to a particular optimization technique (e.g., setting up a
        learning rate value).
        '''
        pass

    def iteropt(self,
                train,
                valid=None,
                patience=5,
                validate_every=10,
                min_improvement=0,
                max_gradient_norm=1e10,
                max_gradient_clip=1e10,
                learning_rate=1e-4,
                momentum=0,
                nesterov=False,
                **kwargs):
        r'''Optimize a loss iteratively using a training and validation dataset.

        This method yields a series of monitor values to the caller. After every
        optimization epoch, a pair of monitor dictionaries is generated: one
        evaluated on the training dataset during the epoch, and another
        evaluated on the validation dataset at the most recent validation epoch.

        The validation monitors might not be updated during every optimization
        iteration; in this case, the most recent validation monitors will be
        yielded along with the training monitors.

        Parameters
        ----------
        train : sequence or :class:`Dataset <downhill.dataset.Dataset>`
            A set of training data for computing updates to model parameters.
        valid : sequence or :class:`Dataset <downhill.dataset.Dataset>`, optional
            A set of validation data for computing monitor values and
            determining when the loss has stopped improving. Defaults to the
            training data.
        patience : int, optional
            Number of validation "failures" that we are willing to tolerate
            before stopping the optimization process. A validation failure
            happens whenever the loss on the validation dataset decreases by
            less than ``min_improvement`` (relative) over the previous best
            validation loss. Defaults to 5.
        validate_every : int, optional
            Evaluate the loss on the validation dataset after making this many
            passes over the training data. Defaults to 10.
        min_improvement : float, optional
            Insist that the validation loss must improve by this relative amount
            before considering that the optimization has made progress. The
            optimization process halts when ``patience`` validations have failed
            to make this relative improvement. Defaults to 0; set to a larger
            value (e.g., 0.01 for 1% improvement) to halt the optimization
            process sooner.
        max_gradient_norm : float, optional
            Rescale each parameter's gradient so that it has at most this L2
            norm. Defaults to 1e10, i.e., very little rescaling.
        max_gradient_clip : float, optional
            Perform elementwise clipping on gradient values (this happens after
            rescaling). Defaults to 1e10, i.e., very little clipping.
        learning_rate : float, optional
            Many SGD-based optimization algorithms require a learning rate
            hyperparameter that scales the gradient step. Defaults to 1e-4.
        momentum : float, optional
            Apply momentum to the parameter updates for this optimizer, with the
            given strength. Typically this value ranges from 0 (no momentum) to
            :math:`1 - \epsilon` (large momentum). Defaults to 0.
        nesterov : bool, optional
            If True, and momentum is nonzero, apply Nesterov-style momentum to
            parameter updates for this optimizer. If False and momentum is
            nonzero, "regular" momentum is applied. See
            :class:`NAG <downhill.NAG>` for a description of Nesterov momentum.

        Returns
        -------
        train_monitors : dict
            A dictionary mapping monitor names to values, evaluated on the
            training dataset.
        valid_monitors : dict
            A dictionary containing monitor values evaluated on the validation
            dataset.
        '''
        self.patience = patience
        self.validate_every = validate_every
        self.min_improvement = min_improvement
        self.max_gradient_norm = util.as_float(max_gradient_norm)
        self.max_gradient_clip = util.as_float(max_gradient_clip)
        self.learning_rate = util.as_float(learning_rate)
        self.momentum = util.as_float(momentum)
        self.nesterov = nesterov
        logging.info('-- patience = %s', patience)
        logging.info('-- validate_every = %s', validate_every)
        logging.info('-- min_improvement = %s', min_improvement)
        logging.info('-- max_gradient_norm = %s', max_gradient_norm)
        logging.info('-- max_gradient_clip = %s', max_gradient_clip)
        logging.info('-- learning_rate = %s', learning_rate)
        logging.info('-- momentum = %s', momentum)
        logging.info('-- nesterov = %s', nesterov)

        self._prepare(**kwargs)
        self._compile()

        if valid is None:
            valid = train
        iteration = 0
        training = validation = None
        while True:
            if not iteration % self.validate_every:
                try:
                    validation = self.evaluate(valid)
                except KeyboardInterrupt:
                    logging.info('interrupted!')
                    break
                if self._test_patience(validation):
                    logging.info('patience elapsed!')
                    break
            try:
                training = self._step(train)
            except KeyboardInterrupt:
                logging.info('interrupted!')
                break
            iteration += 1
            self._log(training, iteration)
            yield training, validation
        self.set_params(self._best_params)

    def minimize(self, *args, **kwargs):
        '''Optimize our loss exhaustively.

        This method is a thin wrapper over the :func:`iteropt` method. It simply
        exhausts the iterative optimization process and returns the final
        monitor values.

        Returns
        -------
        train_monitors : dict
            A dictionary mapping monitor names to values, evaluated on the
            training dataset.
        valid_monitors : dict
            A dictionary containing monitor values evaluated on the validation
            dataset.
        '''
        monitors = None
        for monitors in self.iteropt(*args, **kwargs):
            pass
        return monitors

    def _step(self, dataset):
        '''Advance the state of the optimizer by one step.

        Parameters
        ----------
        dataset : :class:`Dataset <downhill.dataset.Dataset>`
            A dataset for optimizing the model.

        Returns
        -------
        train_monitors : dict
            A dictionary mapping monitor names to values.
        '''
        values = [self.f_step(*x) for x in dataset]
        return collections.OrderedDict(
            zip(self._monitor_names, np.mean(values, axis=0)))
