pitchtools.IntervalClassSegment
===============================

.. autoclass:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment

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
           "pitchtools.IntervalClassSegment" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>IntervalClassSegment</B>>,
               shape=box,
               style="filled, rounded"];
           "pitchtools.Segment" [color=4,
               group=3,
               label=Segment,
               shape=oval,
               style=bold];
           "pitchtools.Segment" -> "pitchtools.IntervalClassSegment";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedTuple" -> "pitchtools.Segment";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.count
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.from_selection
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.has_duplicates
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.index
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.is_tertian
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.item_class
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.items
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__add__
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__contains__
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__eq__
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__format__
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__getitem__
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__getslice__
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__hash__
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__iter__
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__len__
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__mul__
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__ne__
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__radd__
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__repr__
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__rmul__
      ~abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__str__

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

.. autoattribute:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.has_duplicates
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.is_tertian
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.item_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.items
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.count
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.index
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.from_selection
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__add__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__contains__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__getitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__getslice__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__iter__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__len__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__mul__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__radd__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__rmul__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSegment.IntervalClassSegment.__str__
   :noindex:
