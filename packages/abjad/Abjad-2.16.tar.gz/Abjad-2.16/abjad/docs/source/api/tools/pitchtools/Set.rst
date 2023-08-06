pitchtools.Set
==============

.. autoclass:: abjad.tools.pitchtools.Set.Set

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
           "pitchtools.Set" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>Set</B>>,
               shape=oval,
               style="filled, rounded"];
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

      ~abjad.tools.pitchtools.Set.Set.copy
      ~abjad.tools.pitchtools.Set.Set.difference
      ~abjad.tools.pitchtools.Set.Set.from_selection
      ~abjad.tools.pitchtools.Set.Set.intersection
      ~abjad.tools.pitchtools.Set.Set.isdisjoint
      ~abjad.tools.pitchtools.Set.Set.issubset
      ~abjad.tools.pitchtools.Set.Set.issuperset
      ~abjad.tools.pitchtools.Set.Set.item_class
      ~abjad.tools.pitchtools.Set.Set.items
      ~abjad.tools.pitchtools.Set.Set.symmetric_difference
      ~abjad.tools.pitchtools.Set.Set.union
      ~abjad.tools.pitchtools.Set.Set.__and__
      ~abjad.tools.pitchtools.Set.Set.__contains__
      ~abjad.tools.pitchtools.Set.Set.__eq__
      ~abjad.tools.pitchtools.Set.Set.__format__
      ~abjad.tools.pitchtools.Set.Set.__ge__
      ~abjad.tools.pitchtools.Set.Set.__gt__
      ~abjad.tools.pitchtools.Set.Set.__hash__
      ~abjad.tools.pitchtools.Set.Set.__iter__
      ~abjad.tools.pitchtools.Set.Set.__le__
      ~abjad.tools.pitchtools.Set.Set.__len__
      ~abjad.tools.pitchtools.Set.Set.__lt__
      ~abjad.tools.pitchtools.Set.Set.__ne__
      ~abjad.tools.pitchtools.Set.Set.__or__
      ~abjad.tools.pitchtools.Set.Set.__repr__
      ~abjad.tools.pitchtools.Set.Set.__str__
      ~abjad.tools.pitchtools.Set.Set.__sub__
      ~abjad.tools.pitchtools.Set.Set.__xor__

Bases
-----

- :py:class:`datastructuretools.TypedFrozenset <abjad.tools.datastructuretools.TypedFrozenset.TypedFrozenset>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.Set.Set.item_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Set.Set.items
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.Set.Set.copy
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.difference
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.from_selection
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.intersection
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.isdisjoint
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.issubset
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.issuperset
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.symmetric_difference
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.union
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.Set.Set.__and__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.__contains__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.__ge__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.__gt__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.__iter__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.__le__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.__len__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.__lt__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.__or__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.__str__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.__sub__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Set.Set.__xor__
   :noindex:
