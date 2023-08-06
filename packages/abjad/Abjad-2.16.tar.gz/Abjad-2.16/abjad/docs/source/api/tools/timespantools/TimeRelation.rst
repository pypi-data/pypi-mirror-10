timespantools.TimeRelation
==========================

.. autoclass:: abjad.tools.timespantools.TimeRelation.TimeRelation

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
           "timespantools.OffsetTimespanTimeRelation" [color=3,
               group=2,
               label=OffsetTimespanTimeRelation,
               shape=box];
           "timespantools.TimeRelation" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>TimeRelation</B>>,
               shape=oval,
               style="filled, rounded"];
           "timespantools.TimespanTimespanTimeRelation" [color=3,
               group=2,
               label=TimespanTimespanTimeRelation,
               shape=box];
           "timespantools.TimeRelation" -> "timespantools.OffsetTimespanTimeRelation";
           "timespantools.TimeRelation" -> "timespantools.TimespanTimespanTimeRelation";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "timespantools.TimeRelation";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.timespantools.TimeRelation.TimeRelation.inequality
      ~abjad.tools.timespantools.TimeRelation.TimeRelation.is_fully_loaded
      ~abjad.tools.timespantools.TimeRelation.TimeRelation.is_fully_unloaded
      ~abjad.tools.timespantools.TimeRelation.TimeRelation.__call__
      ~abjad.tools.timespantools.TimeRelation.TimeRelation.__eq__
      ~abjad.tools.timespantools.TimeRelation.TimeRelation.__format__
      ~abjad.tools.timespantools.TimeRelation.TimeRelation.__hash__
      ~abjad.tools.timespantools.TimeRelation.TimeRelation.__ne__
      ~abjad.tools.timespantools.TimeRelation.TimeRelation.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.timespantools.TimeRelation.TimeRelation.inequality
   :noindex:

.. autoattribute:: abjad.tools.timespantools.TimeRelation.TimeRelation.is_fully_loaded
   :noindex:

.. autoattribute:: abjad.tools.timespantools.TimeRelation.TimeRelation.is_fully_unloaded
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.timespantools.TimeRelation.TimeRelation.__call__
   :noindex:

.. automethod:: abjad.tools.timespantools.TimeRelation.TimeRelation.__eq__
   :noindex:

.. automethod:: abjad.tools.timespantools.TimeRelation.TimeRelation.__format__
   :noindex:

.. automethod:: abjad.tools.timespantools.TimeRelation.TimeRelation.__hash__
   :noindex:

.. automethod:: abjad.tools.timespantools.TimeRelation.TimeRelation.__ne__
   :noindex:

.. automethod:: abjad.tools.timespantools.TimeRelation.TimeRelation.__repr__
   :noindex:
