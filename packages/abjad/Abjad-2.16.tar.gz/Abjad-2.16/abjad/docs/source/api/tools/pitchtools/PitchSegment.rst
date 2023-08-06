pitchtools.PitchSegment
=======================

.. autoclass:: abjad.tools.pitchtools.PitchSegment.PitchSegment

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
           "pitchtools.PitchSegment" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>PitchSegment</B>>,
               shape=box,
               style="filled, rounded"];
           "pitchtools.Segment" [color=4,
               group=3,
               label=Segment,
               shape=oval,
               style=bold];
           "pitchtools.Segment" -> "pitchtools.PitchSegment";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedTuple" -> "pitchtools.Segment";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.count
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.from_selection
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.has_duplicates
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.hertz
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.index
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.inflection_point_count
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.invert
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.is_equivalent_under_transposition
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.item_class
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.items
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.local_maxima
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.local_minima
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.make_notes
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.multiply
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.retrograde
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.rotate
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.transpose
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.__add__
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.__contains__
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.__eq__
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.__format__
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.__getitem__
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.__getslice__
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.__hash__
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.__illustrate__
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.__iter__
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.__len__
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.__mul__
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.__ne__
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.__radd__
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.__repr__
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.__rmul__
      ~abjad.tools.pitchtools.PitchSegment.PitchSegment.__str__

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

.. autoattribute:: abjad.tools.pitchtools.PitchSegment.PitchSegment.has_duplicates
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchSegment.PitchSegment.hertz
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchSegment.PitchSegment.inflection_point_count
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchSegment.PitchSegment.item_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchSegment.PitchSegment.items
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchSegment.PitchSegment.local_maxima
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchSegment.PitchSegment.local_minima
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.count
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.index
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.invert
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.is_equivalent_under_transposition
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.make_notes
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.multiply
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.retrograde
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.rotate
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.transpose
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.from_selection
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.__add__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.__contains__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.__getitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.__getslice__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.__illustrate__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.__iter__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.__len__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.__mul__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.__radd__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.__rmul__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchSegment.PitchSegment.__str__
   :noindex:
