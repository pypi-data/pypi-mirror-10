timespantools.TimespanTimespanTimeRelation
==========================================

.. autoclass:: abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation

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
           "timespantools.TimeRelation" [color=3,
               group=2,
               label=TimeRelation,
               shape=oval,
               style=bold];
           "timespantools.TimespanTimespanTimeRelation" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>TimespanTimespanTimeRelation</B>>,
               shape=box,
               style="filled, rounded"];
           "timespantools.TimeRelation" -> "timespantools.TimespanTimespanTimeRelation";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "timespantools.TimeRelation";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.get_counttime_components
      ~abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.get_offset_indices
      ~abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.inequality
      ~abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.is_fully_loaded
      ~abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.is_fully_unloaded
      ~abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.timespan_1
      ~abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.timespan_2
      ~abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.__call__
      ~abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.__eq__
      ~abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.__format__
      ~abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.__hash__
      ~abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.__ne__
      ~abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.__repr__

Bases
-----

- :py:class:`timespantools.TimeRelation <abjad.tools.timespantools.TimeRelation.TimeRelation>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.inequality
   :noindex:

.. autoattribute:: abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.is_fully_loaded
   :noindex:

.. autoattribute:: abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.is_fully_unloaded
   :noindex:

.. autoattribute:: abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.timespan_1
   :noindex:

.. autoattribute:: abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.timespan_2
   :noindex:

Methods
-------

.. automethod:: abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.get_counttime_components
   :noindex:

.. automethod:: abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.get_offset_indices
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.__call__
   :noindex:

.. automethod:: abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.__eq__
   :noindex:

.. automethod:: abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.__format__
   :noindex:

.. automethod:: abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.__hash__
   :noindex:

.. automethod:: abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.__ne__
   :noindex:

.. automethod:: abjad.tools.timespantools.TimespanTimespanTimeRelation.TimespanTimespanTimeRelation.__repr__
   :noindex:
