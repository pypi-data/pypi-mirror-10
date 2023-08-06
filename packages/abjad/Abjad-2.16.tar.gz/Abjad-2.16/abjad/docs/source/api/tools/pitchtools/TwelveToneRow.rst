pitchtools.TwelveToneRow
========================

.. autoclass:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow

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
           "pitchtools.TwelveToneRow" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>TwelveToneRow</B>>,
               shape=box,
               style="filled, rounded"];
           "pitchtools.PitchClassSegment" -> "pitchtools.TwelveToneRow";
           "pitchtools.Segment" -> "pitchtools.PitchClassSegment";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedTuple" -> "pitchtools.Segment";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.alpha
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.count
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.from_selection
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.has_duplicates
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.index
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.invert
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.is_equivalent_under_transposition
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.item_class
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.items
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.make_notes
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.multiply
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.permute
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.retrograde
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.rotate
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.transpose
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.voice_horizontally
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.voice_vertically
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__add__
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__contains__
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__eq__
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__format__
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__getitem__
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__getslice__
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__hash__
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__iter__
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__len__
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__mul__
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__ne__
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__radd__
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__repr__
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__rmul__
      ~abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__str__

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

.. autoattribute:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.has_duplicates
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.item_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.items
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.alpha
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.count
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.index
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.invert
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.is_equivalent_under_transposition
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.make_notes
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.multiply
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.permute
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.retrograde
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.rotate
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.transpose
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.voice_horizontally
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.voice_vertically
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.from_selection
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__add__
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__contains__
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__getitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__getslice__
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__iter__
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__len__
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__mul__
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__radd__
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__rmul__
   :noindex:

.. automethod:: abjad.tools.pitchtools.TwelveToneRow.TwelveToneRow.__str__
   :noindex:
