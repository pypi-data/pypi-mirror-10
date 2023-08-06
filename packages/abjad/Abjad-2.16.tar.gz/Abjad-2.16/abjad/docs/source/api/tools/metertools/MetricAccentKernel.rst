metertools.MetricAccentKernel
=============================

.. autoclass:: abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel

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
           "metertools.MetricAccentKernel" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>MetricAccentKernel</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "metertools.MetricAccentKernel";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.count_offsets_in_expr
      ~abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.duration
      ~abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.from_meter
      ~abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.kernel
      ~abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.__call__
      ~abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.__copy__
      ~abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.__eq__
      ~abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.__format__
      ~abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.__hash__
      ~abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.__ne__
      ~abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.__repr__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.duration
   :noindex:

.. autoattribute:: abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.kernel
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.count_offsets_in_expr
   :noindex:

.. automethod:: abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.from_meter
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.__call__
   :noindex:

.. automethod:: abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.__copy__
   :noindex:

.. automethod:: abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.__eq__
   :noindex:

.. automethod:: abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.__format__
   :noindex:

.. automethod:: abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.__hash__
   :noindex:

.. automethod:: abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.__ne__
   :noindex:

.. automethod:: abjad.tools.metertools.MetricAccentKernel.MetricAccentKernel.__repr__
   :noindex:
