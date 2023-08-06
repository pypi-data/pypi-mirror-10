pitchtools.IntervalSegment
==========================

.. autoclass:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment

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
           "pitchtools.IntervalSegment" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>IntervalSegment</B>>,
               shape=box,
               style="filled, rounded"];
           "pitchtools.Segment" [color=4,
               group=3,
               label=Segment,
               shape=oval,
               style=bold];
           "pitchtools.Segment" -> "pitchtools.IntervalSegment";
       }
       subgraph cluster_tonalanalysistools {
           graph [label=tonalanalysistools];
           "tonalanalysistools.RootlessChordClass" [color=5,
               group=4,
               label=RootlessChordClass,
               shape=box];
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

      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.count
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.from_selection
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.has_duplicates
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.index
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.item_class
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.items
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.rotate
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.slope
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.spread
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__add__
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__contains__
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__eq__
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__format__
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__getitem__
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__getslice__
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__hash__
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__iter__
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__len__
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__mul__
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__ne__
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__radd__
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__repr__
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__rmul__
      ~abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__str__

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

.. autoattribute:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.has_duplicates
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.item_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.items
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.slope
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.spread
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.count
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.index
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.rotate
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.from_selection
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__add__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__contains__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__getitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__getslice__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__iter__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__len__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__mul__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__radd__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__rmul__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalSegment.IntervalSegment.__str__
   :noindex:
