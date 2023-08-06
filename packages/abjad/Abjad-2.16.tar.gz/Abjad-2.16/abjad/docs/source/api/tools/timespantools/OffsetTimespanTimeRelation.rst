timespantools.OffsetTimespanTimeRelation
========================================

.. autoclass:: abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation

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
           "abctools.AbjadObject.AbstractBase" -> "abctools.AbjadObject";
       }
       subgraph cluster_timespantools {
           graph [label=timespantools];
           "timespantools.OffsetTimespanTimeRelation" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>OffsetTimespanTimeRelation</B>>,
               shape=box,
               style="filled, rounded"];
           "timespantools.TimeRelation" [color=3,
               group=2,
               label=TimeRelation,
               shape=oval,
               style=bold];
           "timespantools.TimeRelation" -> "timespantools.OffsetTimespanTimeRelation";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "timespantools.TimeRelation";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.inequality
      ~abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.is_fully_loaded
      ~abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.is_fully_unloaded
      ~abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.offset
      ~abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.timespan
      ~abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.__call__
      ~abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.__eq__
      ~abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.__format__
      ~abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.__hash__
      ~abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.__ne__
      ~abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.__repr__

Bases
-----

- :py:class:`timespantools.TimeRelation <abjad.tools.timespantools.TimeRelation.TimeRelation>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.inequality
   :noindex:

.. autoattribute:: abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.is_fully_loaded
   :noindex:

.. autoattribute:: abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.is_fully_unloaded
   :noindex:

.. autoattribute:: abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.offset
   :noindex:

.. autoattribute:: abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.timespan
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.__call__
   :noindex:

.. automethod:: abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.__eq__
   :noindex:

.. automethod:: abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.__format__
   :noindex:

.. automethod:: abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.__hash__
   :noindex:

.. automethod:: abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.__ne__
   :noindex:

.. automethod:: abjad.tools.timespantools.OffsetTimespanTimeRelation.OffsetTimespanTimeRelation.__repr__
   :noindex:
