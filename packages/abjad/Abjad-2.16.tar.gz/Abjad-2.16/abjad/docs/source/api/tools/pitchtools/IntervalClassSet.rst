pitchtools.IntervalClassSet
===========================

.. autoclass:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet

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
           "datastructuretools.TypedFrozenset" [color=3,
               group=2,
               label=TypedFrozenset,
               shape=box];
           "datastructuretools.TypedCollection" -> "datastructuretools.TypedFrozenset";
       }
       subgraph cluster_pitchtools {
           graph [label=pitchtools];
           "pitchtools.IntervalClassSet" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>IntervalClassSet</B>>,
               shape=box,
               style="filled, rounded"];
           "pitchtools.Set" [color=4,
               group=3,
               label=Set,
               shape=oval,
               style=bold];
           "pitchtools.Set" -> "pitchtools.IntervalClassSet";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedFrozenset" -> "pitchtools.Set";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.copy
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.difference
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.from_selection
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.intersection
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.isdisjoint
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.issubset
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.issuperset
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.item_class
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.items
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.symmetric_difference
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.union
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__and__
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__contains__
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__eq__
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__format__
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__ge__
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__gt__
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__hash__
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__iter__
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__le__
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__len__
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__lt__
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__ne__
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__or__
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__repr__
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__str__
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__sub__
      ~abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__xor__

Bases
-----

- :py:class:`pitchtools.Set <abjad.tools.pitchtools.Set.Set>`

- :py:class:`datastructuretools.TypedFrozenset <abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.item_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.items
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.copy
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.difference
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.intersection
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.isdisjoint
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.issubset
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.issuperset
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.symmetric_difference
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.union
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.from_selection
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__and__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__contains__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__ge__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__gt__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__iter__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__le__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__len__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__lt__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__or__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__str__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__sub__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassSet.IntervalClassSet.__xor__
   :noindex:
