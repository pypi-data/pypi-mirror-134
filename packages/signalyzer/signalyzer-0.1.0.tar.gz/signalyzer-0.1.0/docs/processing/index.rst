.. currentmodule:: signalyzer

.. _signal processing:

Signal Processing
=================

The :class:`Trace` class has *methods* for `signal processing`_  the
:attr:`~Trace.samples` of a :class:`Trace`.

.. toctree::
   :maxdepth: 3
   :caption: Signal Processing
   :hidden:

   clipping
   first-order-lag
   exponential-smoothing
   iir-filters
   window-generator
   moving-differentiation
   moving-averages
   moving-linear-regression


Clipping
--------

.. csv-table::
   :header: "Method", "Name", "Label"
   :widths: 20, 80, 20
   :align: left

   :meth:`~Trace.clip`, :ref:`Clip <clip>`, ``'clip'``
   :meth:`~Trace.clamp`, :ref:`Clamp <clamp>`, ``'clamp'``


Smoothing
---------

.. csv-table::
   :header: "Method", "Name", "Label"
   :widths: 20, 80, 20
   :align: left

   :meth:`~Trace.lag`, :ref:`First-order lag <first-order lag>`, ``'lag'``
   :meth:`~Trace.exponential`, :ref:`Exponential smoothing <second-order exponential smoothing>`, ``'exponential'``


Filtering
---------

.. csv-table::
   :header: "Method", "Name", "Label"
   :widths: 20, 80, 20
   :align: left

   :meth:`~Trace.band_pass`, :ref:`High-Pass filter <band-pass>`, ``'band-pass'``
   :meth:`~Trace.low_pass`, :ref:`Low-Pass filter <low-pass>`, ``'low-pass'``
   :meth:`~Trace.high_pass`, :ref:`High-Pass filter <high-pass>`, ``'high-pass'``
   :meth:`~Trace.notch`, :ref:`Notch filter <notch>`, ``'notch'``
   :meth:`~Trace.all_pass`, :ref:`All-Pass filter <all-pass>`, ``'all-pass'``


Moving Window Functions
-----------------------

.. csv-table::
   :header: "Method", "Name", "Label"
   :widths: 20, 80, 20
   :align: left

   :meth:`~Trace.window`, :ref:`Moving window generator <moving window>`,
   :meth:`~Trace.moving_average`, :ref:`Moving averages <moving average>`, ``'average'``
   :meth:`~Trace.moving_differential`, :ref:`Moving differentiation <moving differentiation>`,  ``'differential'``
   :meth:`~Trace.moving_regression`, :ref:`Moving linear regression <moving linear regression>`,  ``'regression'``
