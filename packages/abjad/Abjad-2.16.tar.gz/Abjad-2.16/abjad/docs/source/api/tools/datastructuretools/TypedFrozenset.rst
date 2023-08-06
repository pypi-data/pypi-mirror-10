datastructuretools.TypedFrozenset
=================================

.. autoclass:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset

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
           "datastructuretools.TypedFrozenset" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>TypedFrozenset</B>>,
               shape=box,
               style="filled, rounded"];
           "datastructuretools.TypedCollection" -> "datastructuretools.TypedFrozenset";
       }
       subgraph cluster_pitchtools {
           graph [label=pitchtools];
           "pitchtools.IntervalClassSet" [color=4,
               group=3,
               label=IntervalClassSet,
               shape=box];
           "pitchtools.IntervalSet" [color=4,
               group=3,
               label=IntervalSet,
               shape=box];
           "pitchtools.PitchClassSet" [color=4,
               group=3,
               label=PitchClassSet,
               shape=box];
           "pitchtools.PitchSet" [color=4,
               group=3,
               label=PitchSet,
               shape=box];
           "pitchtools.Set" [color=4,
               group=3,
               label=Set,
               shape=oval,
               style=bold];
           "pitchtools.Set" -> "pitchtools.IntervalClassSet";
           "pitchtools.Set" -> "pitchtools.IntervalSet";
           "pitchtools.Set" -> "pitchtools.PitchClassSet";
           "pitchtools.Set" -> "pitchtools.PitchSet";
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

      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.copy
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.difference
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.intersection
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.isdisjoint
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.issubset
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.issuperset
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.item_class
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.items
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.symmetric_difference
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.union
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__and__
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__contains__
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__eq__
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__format__
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__ge__
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__gt__
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__hash__
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__iter__
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__le__
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__len__
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__lt__
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__ne__
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__or__
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__repr__
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__sub__
      ~abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__xor__

Bases
-----

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.item_class
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.items
   :noindex:

Methods
-------

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.copy
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.difference
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.intersection
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.isdisjoint
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.issubset
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.issuperset
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.symmetric_difference
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.union
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__and__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__contains__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__eq__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__format__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__ge__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__gt__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__hash__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__iter__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__le__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__len__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__lt__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__ne__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__or__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__repr__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__sub__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset.__xor__
   :noindex:
