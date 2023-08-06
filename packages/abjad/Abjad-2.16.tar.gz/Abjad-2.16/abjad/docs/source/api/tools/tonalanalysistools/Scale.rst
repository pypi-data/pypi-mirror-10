tonalanalysistools.Scale
========================

.. autoclass:: abjad.tools.tonalanalysistools.Scale.Scale

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
           "pitchtools.PitchClassSegment" [color=4,
               group=3,
               label=PitchClassSegment,
               shape=box];
           "pitchtools.Segment" [color=4,
               group=3,
               label=Segment,
               shape=oval,
               style=bold];
           "pitchtools.Segment" -> "pitchtools.PitchClassSegment";
       }
       subgraph cluster_tonalanalysistools {
           graph [label=tonalanalysistools];
           "tonalanalysistools.Scale" [color=black,
               fontcolor=white,
               group=4,
               label=<<B>Scale</B>>,
               shape=box,
               style="filled, rounded"];
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

      ~abjad.tools.tonalanalysistools.Scale.Scale.alpha
      ~abjad.tools.tonalanalysistools.Scale.Scale.count
      ~abjad.tools.tonalanalysistools.Scale.Scale.create_named_pitch_set_in_pitch_range
      ~abjad.tools.tonalanalysistools.Scale.Scale.dominant
      ~abjad.tools.tonalanalysistools.Scale.Scale.from_selection
      ~abjad.tools.tonalanalysistools.Scale.Scale.has_duplicates
      ~abjad.tools.tonalanalysistools.Scale.Scale.index
      ~abjad.tools.tonalanalysistools.Scale.Scale.invert
      ~abjad.tools.tonalanalysistools.Scale.Scale.is_equivalent_under_transposition
      ~abjad.tools.tonalanalysistools.Scale.Scale.item_class
      ~abjad.tools.tonalanalysistools.Scale.Scale.items
      ~abjad.tools.tonalanalysistools.Scale.Scale.key_signature
      ~abjad.tools.tonalanalysistools.Scale.Scale.leading_tone
      ~abjad.tools.tonalanalysistools.Scale.Scale.make_notes
      ~abjad.tools.tonalanalysistools.Scale.Scale.make_score
      ~abjad.tools.tonalanalysistools.Scale.Scale.mediant
      ~abjad.tools.tonalanalysistools.Scale.Scale.multiply
      ~abjad.tools.tonalanalysistools.Scale.Scale.named_interval_class_segment
      ~abjad.tools.tonalanalysistools.Scale.Scale.named_pitch_class_to_scale_degree
      ~abjad.tools.tonalanalysistools.Scale.Scale.retrograde
      ~abjad.tools.tonalanalysistools.Scale.Scale.rotate
      ~abjad.tools.tonalanalysistools.Scale.Scale.scale_degree_to_named_pitch_class
      ~abjad.tools.tonalanalysistools.Scale.Scale.subdominant
      ~abjad.tools.tonalanalysistools.Scale.Scale.submediant
      ~abjad.tools.tonalanalysistools.Scale.Scale.superdominant
      ~abjad.tools.tonalanalysistools.Scale.Scale.tonic
      ~abjad.tools.tonalanalysistools.Scale.Scale.transpose
      ~abjad.tools.tonalanalysistools.Scale.Scale.voice_horizontally
      ~abjad.tools.tonalanalysistools.Scale.Scale.voice_scale_degrees_in_open_position
      ~abjad.tools.tonalanalysistools.Scale.Scale.voice_vertically
      ~abjad.tools.tonalanalysistools.Scale.Scale.__add__
      ~abjad.tools.tonalanalysistools.Scale.Scale.__contains__
      ~abjad.tools.tonalanalysistools.Scale.Scale.__eq__
      ~abjad.tools.tonalanalysistools.Scale.Scale.__format__
      ~abjad.tools.tonalanalysistools.Scale.Scale.__getitem__
      ~abjad.tools.tonalanalysistools.Scale.Scale.__getslice__
      ~abjad.tools.tonalanalysistools.Scale.Scale.__hash__
      ~abjad.tools.tonalanalysistools.Scale.Scale.__iter__
      ~abjad.tools.tonalanalysistools.Scale.Scale.__len__
      ~abjad.tools.tonalanalysistools.Scale.Scale.__mul__
      ~abjad.tools.tonalanalysistools.Scale.Scale.__ne__
      ~abjad.tools.tonalanalysistools.Scale.Scale.__radd__
      ~abjad.tools.tonalanalysistools.Scale.Scale.__repr__
      ~abjad.tools.tonalanalysistools.Scale.Scale.__rmul__
      ~abjad.tools.tonalanalysistools.Scale.Scale.__str__

Bases
-----

- :py:class:`pitchtools.PitchClassSegment <abjad.tools.pitchtools.PitchClassSegment.PitchClassSegment>`

- :py:class:`pitchtools.Segment <abjad.tools.pitchtools.Segment.Segment>`

- :py:class:`datastructuretools.TypedTuple <abjad.tools.datastructuretools.TypedTuple.TypedTuple>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.tonalanalysistools.Scale.Scale.dominant
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.Scale.Scale.has_duplicates
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.Scale.Scale.item_class
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.Scale.Scale.items
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.Scale.Scale.key_signature
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.Scale.Scale.leading_tone
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.Scale.Scale.mediant
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.Scale.Scale.named_interval_class_segment
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.Scale.Scale.subdominant
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.Scale.Scale.submediant
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.Scale.Scale.superdominant
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.Scale.Scale.tonic
   :noindex:

Methods
-------

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.alpha
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.count
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.create_named_pitch_set_in_pitch_range
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.index
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.invert
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.is_equivalent_under_transposition
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.make_notes
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.make_score
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.multiply
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.named_pitch_class_to_scale_degree
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.retrograde
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.rotate
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.scale_degree_to_named_pitch_class
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.transpose
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.voice_horizontally
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.voice_scale_degrees_in_open_position
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.voice_vertically
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.from_selection
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.__add__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.__contains__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.__eq__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.__format__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.__getitem__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.__getslice__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.__hash__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.__iter__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.__len__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.__mul__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.__ne__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.__radd__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.__repr__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.__rmul__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.Scale.Scale.__str__
   :noindex:
