.. currentmodule:: signalyzer

.. testsetup:: *

    from signalyzer import *

.. _first-order lag:

First-order Lag
===============

The signal :attr:`~Trace.samples` of a :ref:`signal trace <signal trace>` can be
processed with a first-order lag over a number of signal :attr:`~Trace.samples`
or with a smoothing factor.

Sample Based Smoothing
----------------------

You can smooth the signal :attr:`~Trace.samples` with a first-order lag by
calling the method :meth:`~Trace.lag` and define the *time constant*
:math:`\tau` of the first-order lag by the number of signal samples.

  >>> # smooth the signal samples sample based [.., 1:transparent, ..]
  >>> Trace('Signal', [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]).lag(2)
  Trace(label='Signal:lag',
        samples=[0.0, 0.5, 0.75, 0.875, 0.9375, 0.96875, 0.984375,
                 0.9921875, 0.99609375, 0.998046875, 0.9990234375])

.. plotly::

  from signalyzer import Trace

  signal = Trace('Signal', [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
  trace = signal.lag(2)
  fig = go.Figure([signal.digital.plot(),
                   trace.plot(mode='lines+markers')])
  fig.show()

Factor Based Smoothing
----------------------

You can smooth the signal :attr:`~Trace.samples` with a first-order lag by
calling the method :meth:`~Trace.lag` and define the inverted *time constant*
:math:`\frac{1}{\tau}` of the first-order lag with a smoothing factor between
``0.0`` and ``1.0``.

  >>> # smooth the signal samples factor based [0.0:freeze..1.0:transparent]
  >>> Trace('Signal', [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]).lag(0.5)
  Trace(label='Signal:lag',
        samples=[0.0, 0.5, 0.75, 0.875, 0.9375, 0.96875, 0.984375,
                 0.9921875, 0.99609375, 0.998046875, 0.9990234375])

.. plotly::

  from signalyzer import Trace

  signal = Trace('Signal', [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
  trace = signal.lag(0.5)
  fig = go.Figure([signal.digital.plot(),
                   trace.plot(mode='lines+markers')])
  fig.show()
