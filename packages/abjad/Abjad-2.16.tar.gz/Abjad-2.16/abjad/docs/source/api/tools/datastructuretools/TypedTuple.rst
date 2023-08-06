datastructuretools.TypedTuple
=============================

.. autoclass:: abjad.tools.datastructuretools.TypedTuple.TypedTuple

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
       subgraph cluster_datastructuretools {
           graph [label=datastructuretools];
           "datastructuretools.TypedCollection" [color=3,
               group=2,
               label=TypedCollection,
               shape=oval,
               style=bold];
           "datastructuretools.TypedTuple" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>TypedTuple</B>>,
               shape=box,
               style="filled, rounded"];
           "datastructuretools.TypedCollection" -> "datastructuretools.TypedTuple";
       }
       subgraph cluster_mathtools {
           graph [label=mathtools];
           "mathtools.NonreducedRatio" [color=4,
               group=3,
               label=NonreducedRatio,
               shape=box];
           "mathtools.Ratio" [color=4,
               group=3,
               label=Ratio,
               shape=box];
           "mathtools.NonreducedRatio" -> "mathtools.Ratio";
       }
       subgraph cluster_pitchtools {
           graph [label=pitchtools];
           "pitchtools.IntervalClassSegment" [color=5,
               group=4,
               label=IntervalClassSegment,
               shape=box];
           "pitchtools.IntervalSegment" [color=5,
               group=4,
               label=IntervalSegment,
               shape=box];
           "pitchtools.PitchClassSegment" [color=5,
               group=4,
               label=PitchClassSegment,
               shape=box];
           "pitchtools.PitchSegment" [color=5,
               group=4,
               label=PitchSegment,
               shape=box];
           "pitchtools.Segment" [color=5,
               group=4,
               label=Segment,
               shape=oval,
               style=bold];
           "pitchtools.TwelveToneRow" [color=5,
               group=4,
               label=TwelveToneRow,
               shape=box];
           "pitchtools.PitchClassSegment" -> "pitchtools.TwelveToneRow";
           "pitchtools.Segment" -> "pitchtools.IntervalClassSegment";
           "pitchtools.Segment" -> "pitchtools.IntervalSegment";
           "pitchtools.Segment" -> "pitchtools.PitchClassSegment";
           "pitchtools.Segment" -> "pitchtools.PitchSegment";
       }
       subgraph cluster_rhythmmakertools {
           graph [label=rhythmmakertools];
           "rhythmmakertools.BooleanPatternInventory" [color=6,
               group=5,
               label=BooleanPatternInventory,
               shape=box];
       }
       subgraph cluster_tonalanalysistools {
           graph [label=tonalanalysistools];
           "tonalanalysistools.RootlessChordClass" [color=7,
               group=6,
               label=RootlessChordClass,
               shape=box];
           "tonalanalysistools.Scale" [color=7,
               group=6,
               label=Scale,
               shape=box];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedTuple" -> "mathtools.NonreducedRatio";
       "datastructuretools.TypedTuple" -> "pitchtools.Segment";
       "datastructuretools.TypedTuple" -> "rhythmmakertools.BooleanPatternInventory";
       "pitchtools.IntervalSegment" -> "tonalanalysistools.RootlessChordClass";
       "pitchtools.PitchClassSegment" -> "tonalanalysistools.Scale";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.count
      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.index
      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.item_class
      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.items
      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.__add__
      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.__contains__
      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.__eq__
      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.__format__
      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.__getitem__
      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.__getslice__
      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.__hash__
      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.__iter__
      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.__len__
      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.__mul__
      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.__ne__
      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.__radd__
      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.__repr__
      ~abjad.tools.datastructuretools.TypedTuple.TypedTuple.__rmul__

Bases
-----

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.item_class
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.items
   :noindex:

Methods
-------

.. automethod:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.count
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.index
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.__add__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.__contains__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.__eq__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.__format__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.__getitem__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.__getslice__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.__hash__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.__iter__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.__len__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.__mul__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.__ne__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.__radd__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.__repr__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedTuple.TypedTuple.__rmul__
   :noindex:
