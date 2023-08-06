tonalanalysistools.RootlessChordClass
=====================================

.. autoclass:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass

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
           "pitchtools.IntervalSegment" [color=4,
               group=3,
               label=IntervalSegment,
               shape=box];
           "pitchtools.Segment" [color=4,
               group=3,
               label=Segment,
               shape=oval,
               style=bold];
           "pitchtools.Segment" -> "pitchtools.IntervalSegment";
       }
       subgraph cluster_tonalanalysistools {
           graph [label=tonalanalysistools];
           "tonalanalysistools.RootlessChordClass" [color=black,
               fontcolor=white,
               group=4,
               label=<<B>RootlessChordClass</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedTuple" -> "pitchtools.Segment";
       "pitchtools.IntervalSegment" -> "tonalanalysistools.RootlessChordClass";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.cardinality
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.count
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.extent
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.extent_name
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.from_interval_class_segment
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.from_selection
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.has_duplicates
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.index
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.inversion
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.item_class
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.items
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.position
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.quality_string
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.rotate
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.rotation
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.slope
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.spread
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__add__
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__contains__
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__eq__
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__format__
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__getitem__
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__getslice__
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__hash__
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__iter__
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__len__
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__mul__
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__ne__
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__radd__
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__repr__
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__rmul__
      ~abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__str__

Bases
-----

- :py:class:`pitchtools.IntervalSegment <abjad.tools.pitchtools.IntervalSegment.IntervalSegment>`

- :py:class:`pitchtools.Segment <abjad.tools.pitchtools.Segment.Segment>`

- :py:class:`datastructuretools.TypedTuple <abjad.tools.datastructuretools.TypedTuple.TypedTuple>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.cardinality
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.extent
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.extent_name
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.has_duplicates
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.inversion
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.item_class
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.items
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.position
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.quality_string
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.rotation
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.slope
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.spread
   :noindex:

Methods
-------

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.count
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.index
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.rotate
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.from_selection
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.from_interval_class_segment
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__add__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__contains__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__eq__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__format__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__getitem__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__getslice__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__hash__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__iter__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__len__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__mul__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__ne__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__radd__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__repr__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__rmul__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RootlessChordClass.RootlessChordClass.__str__
   :noindex:
