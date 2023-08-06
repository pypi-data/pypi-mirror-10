metertools.MeterFittingSession
==============================

.. autoclass:: abjad.tools.metertools.MeterFittingSession.MeterFittingSession

Lineage
-------

.. graphviz::

   digraph InheritanceGraph {
       graph [background=transparent,
           color=lightslategrey,
           fontname=Arial,
           outputorder=edgesfirst,
           overlap=prism,
           penwidth=2,
           rankdir=LR,
           root="__builtin__.object",
           splines=spline,
           style="dotted, rounded"];
       node [colorscheme=pastel19,
           fontname=Arial,
           fontsize=12,
           penwidth=2,
           style="filled, rounded"];
       edge [color=lightsteelblue2,
           penwidth=2];
       subgraph cluster___builtin__ {
           graph [label=__builtin__];
           "__builtin__.object" [color=1,
               group=0,
               label=object,
               shape=box];
       }
       subgraph cluster_abctools {
           graph [label=abctools];
           "abctools.AbjadObject" [color=2,
               group=1,
               label=AbjadObject,
               shape=box];
           "abctools.AbjadObject.AbstractBase" [color=2,
               group=1,
               label=AbstractBase,
               shape=box];
           "abctools.AbjadValueObject" [color=2,
               group=1,
               label=AbjadValueObject,
               shape=box];
           "abctools.AbjadObject" -> "abctools.AbjadValueObject";
           "abctools.AbjadObject.AbstractBase" -> "abctools.AbjadObject";
       }
       subgraph cluster_metertools {
           graph [label=metertools];
           "metertools.MeterFittingSession" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>MeterFittingSession</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "metertools.MeterFittingSession";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.metertools.MeterFittingSession.MeterFittingSession.cached_offset_counters
      ~abjad.tools.metertools.MeterFittingSession.MeterFittingSession.kernel_denominator
      ~abjad.tools.metertools.MeterFittingSession.MeterFittingSession.kernels
      ~abjad.tools.metertools.MeterFittingSession.MeterFittingSession.longest_kernel
      ~abjad.tools.metertools.MeterFittingSession.MeterFittingSession.maximum_run_length
      ~abjad.tools.metertools.MeterFittingSession.MeterFittingSession.meters
      ~abjad.tools.metertools.MeterFittingSession.MeterFittingSession.offset_counter
      ~abjad.tools.metertools.MeterFittingSession.MeterFittingSession.ordered_offsets
      ~abjad.tools.metertools.MeterFittingSession.MeterFittingSession.__call__
      ~abjad.tools.metertools.MeterFittingSession.MeterFittingSession.__copy__
      ~abjad.tools.metertools.MeterFittingSession.MeterFittingSession.__eq__
      ~abjad.tools.metertools.MeterFittingSession.MeterFittingSession.__format__
      ~abjad.tools.metertools.MeterFittingSession.MeterFittingSession.__hash__
      ~abjad.tools.metertools.MeterFittingSession.MeterFittingSession.__ne__
      ~abjad.tools.metertools.MeterFittingSession.MeterFittingSession.__repr__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.metertools.MeterFittingSession.MeterFittingSession.cached_offset_counters
   :noindex:

.. autoattribute:: abjad.tools.metertools.MeterFittingSession.MeterFittingSession.kernel_denominator
   :noindex:

.. autoattribute:: abjad.tools.metertools.MeterFittingSession.MeterFittingSession.kernels
   :noindex:

.. autoattribute:: abjad.tools.metertools.MeterFittingSession.MeterFittingSession.longest_kernel
   :noindex:

.. autoattribute:: abjad.tools.metertools.MeterFittingSession.MeterFittingSession.maximum_run_length
   :noindex:

.. autoattribute:: abjad.tools.metertools.MeterFittingSession.MeterFittingSession.meters
   :noindex:

.. autoattribute:: abjad.tools.metertools.MeterFittingSession.MeterFittingSession.offset_counter
   :noindex:

.. autoattribute:: abjad.tools.metertools.MeterFittingSession.MeterFittingSession.ordered_offsets
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.metertools.MeterFittingSession.MeterFittingSession.__call__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterFittingSession.MeterFittingSession.__copy__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterFittingSession.MeterFittingSession.__eq__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterFittingSession.MeterFittingSession.__format__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterFittingSession.MeterFittingSession.__hash__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterFittingSession.MeterFittingSession.__ne__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterFittingSession.MeterFittingSession.__repr__
   :noindex:
