pitchtools.PitchClassSet
========================

.. autoclass:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet

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
           "pitchtools.PitchClassSet" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>PitchClassSet</B>>,
               shape=box,
               style="filled, rounded"];
           "pitchtools.Set" [color=4,
               group=3,
               label=Set,
               shape=oval,
               style=bold];
           "pitchtools.Set" -> "pitchtools.PitchClassSet";
       }
       subgraph cluster_tonalanalysistools {
           graph [label=tonalanalysistools];
           "tonalanalysistools.RootedChordClass" [color=5,
               group=4,
               label=RootedChordClass,
               shape=box];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedFrozenset" -> "pitchtools.Set";
       "pitchtools.PitchClassSet" -> "tonalanalysistools.RootedChordClass";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.copy
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.difference
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.from_selection
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.intersection
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.invert
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.is_transposed_subset
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.is_transposed_superset
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.isdisjoint
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.issubset
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.issuperset
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.item_class
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.items
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.multiply
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.order_by
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.symmetric_difference
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.transpose
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.union
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__and__
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__contains__
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__eq__
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__format__
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__ge__
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__gt__
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__hash__
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__iter__
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__le__
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__len__
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__lt__
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__ne__
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__or__
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__repr__
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__str__
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__sub__
      ~abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__xor__

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

.. autoattribute:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.item_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.items
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.copy
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.difference
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.intersection
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.invert
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.is_transposed_subset
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.is_transposed_superset
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.isdisjoint
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.issubset
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.issuperset
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.multiply
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.order_by
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.symmetric_difference
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.transpose
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.union
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.from_selection
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__and__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__contains__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__ge__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__gt__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__iter__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__le__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__len__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__lt__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__or__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__str__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__sub__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassSet.PitchClassSet.__xor__
   :noindex:
