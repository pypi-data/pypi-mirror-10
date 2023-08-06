pitchtools.Segment
==================

.. autoclass:: abjad.tools.pitchtools.Segment.Segment

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
           "datastructuretools.TypedTuple" [color=3,
               group=2,
               label=TypedTuple,
               shape=box];
           "datastructuretools.TypedCollection" -> "datastructuretools.TypedTuple";
       }
       subgraph cluster_pitchtools {
           graph [label=pitchtools];
           "pitchtools.IntervalClassSegment" [color=4,
               group=3,
               label=IntervalClassSegment,
               shape=box];
           "pitchtools.IntervalSegment" [color=4,
               group=3,
               label=IntervalSegment,
               shape=box];
           "pitchtools.PitchClassSegment" [color=4,
               group=3,
               label=PitchClassSegment,
               shape=box];
           "pitchtools.PitchSegment" [color=4,
               group=3,
               label=PitchSegment,
               shape=box];
           "pitchtools.Segment" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>Segment</B>>,
               shape=oval,
               style="filled, rounded"];
           "pitchtools.TwelveToneRow" [color=4,
               group=3,
               label=TwelveToneRow,
               shape=box];
           "pitchtools.PitchClassSegment" -> "pitchtools.TwelveToneRow";
           "pitchtools.Segment" -> "pitchtools.IntervalClassSegment";
           "pitchtools.Segment" -> "pitchtools.IntervalSegment";
           "pitchtools.Segment" -> "pitchtools.PitchClassSegment";
           "pitchtools.Segment" -> "pitchtools.PitchSegment";
       }
       subgraph cluster_tonalanalysistools {
           graph [label=tonalanalysistools];
           "tonalanalysistools.RootlessChordClass" [color=5,
               group=4,
               label=RootlessChordClass,
               shape=box];
           "tonalanalysistools.Scale" [color=5,
               group=4,
               label=Scale,
               shape=box];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedTuple" -> "pitchtools.Segment";
       "pitchtools.IntervalSegment" -> "tonalanalysistools.RootlessChordClass";
       "pitchtools.PitchClassSegment" -> "tonalanalysistools.Scale";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.Segment.Segment.count
      ~abjad.tools.pitchtools.Segment.Segment.from_selection
      ~abjad.tools.pitchtools.Segment.Segment.has_duplicates
      ~abjad.tools.pitchtools.Segment.Segment.index
      ~abjad.tools.pitchtools.Segment.Segment.item_class
      ~abjad.tools.pitchtools.Segment.Segment.items
      ~abjad.tools.pitchtools.Segment.Segment.__add__
      ~abjad.tools.pitchtools.Segment.Segment.__contains__
      ~abjad.tools.pitchtools.Segment.Segment.__eq__
      ~abjad.tools.pitchtools.Segment.Segment.__format__
      ~abjad.tools.pitchtools.Segment.Segment.__getitem__
      ~abjad.tools.pitchtools.Segment.Segment.__getslice__
      ~abjad.tools.pitchtools.Segment.Segment.__hash__
      ~abjad.tools.pitchtools.Segment.Segment.__iter__
      ~abjad.tools.pitchtools.Segment.Segment.__len__
      ~abjad.tools.pitchtools.Segment.Segment.__mul__
      ~abjad.tools.pitchtools.Segment.Segment.__ne__
      ~abjad.tools.pitchtools.Segment.Segment.__radd__
      ~abjad.tools.pitchtools.Segment.Segment.__repr__
      ~abjad.tools.pitchtools.Segment.Segment.__rmul__
      ~abjad.tools.pitchtools.Segment.Segment.__str__

Bases
-----

- :py:class:`datastructuretools.TypedTuple <abjad.tools.datastructuretools.TypedTuple.TypedTuple>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.Segment.Segment.has_duplicates
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Segment.Segment.item_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Segment.Segment.items
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.Segment.Segment.count
   :noindex:

.. automethod:: abjad.tools.pitchtools.Segment.Segment.from_selection
   :noindex:

.. automethod:: abjad.tools.pitchtools.Segment.Segment.index
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.Segment.Segment.__add__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Segment.Segment.__contains__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Segment.Segment.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Segment.Segment.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Segment.Segment.__getitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Segment.Segment.__getslice__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Segment.Segment.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Segment.Segment.__iter__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Segment.Segment.__len__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Segment.Segment.__mul__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Segment.Segment.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Segment.Segment.__radd__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Segment.Segment.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Segment.Segment.__rmul__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Segment.Segment.__str__
   :noindex:
