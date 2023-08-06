pitchtools.PitchClassSegment
============================

.. autoclass:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment

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
           "pitchtools.PitchClassSegment" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>PitchClassSegment</B>>,
               shape=box,
               style="filled, rounded"];
           "pitchtools.Segment" [color=4,
               group=3,
               label=Segment,
               shape=oval,
               style=bold];
           "pitchtools.TwelveToneRow" [color=4,
               group=3,
               label=TwelveToneRow,
               shape=box];
           "pitchtools.PitchClassSegment" -> "pitchtools.TwelveToneRow";
           "pitchtools.Segment" -> "pitchtools.PitchClassSegment";
       }
       subgraph cluster_tonalanalysistools {
           graph [label=tonalanalysistools];
           "tonalanalysistools.Scale" [color=5,
               group=4,
               label=Scale,
               shape=box];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedTuple" -> "pitchtools.Segment";
       "pitchtools.PitchClassSegment" -> "tonalanalysistools.Scale";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.alpha
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.count
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.from_selection
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.has_duplicates
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.index
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.invert
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.is_equivalent_under_transposition
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.item_class
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.items
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.make_notes
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.multiply
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.retrograde
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.rotate
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.transpose
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.voice_horizontally
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.voice_vertically
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__add__
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__contains__
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__eq__
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__format__
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__getitem__
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__getslice__
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__hash__
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__iter__
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__len__
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__mul__
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__ne__
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__radd__
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__repr__
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__rmul__
      ~abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__str__

Bases
-----

- :py:class:`pitchtools.Segment <abjad.tools.pitchtools.Segment.Segment>`

- :py:class:`datastructuretools.TypedTuple <abjad.tools.datastructuretools.TypedTuple.TypedTuple>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.has_duplicates
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.item_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.items
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.alpha
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.count
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.index
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.invert
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.is_equivalent_under_transposition
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.make_notes
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.multiply
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.retrograde
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.rotate
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.transpose
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.voice_horizontally
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.voice_vertically
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.from_selection
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__add__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__contains__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__getitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__getslice__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__iter__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__len__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__mul__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__radd__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__rmul__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment.__str__
   :noindex:
