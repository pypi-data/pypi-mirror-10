mathtools.Ratio
===============

.. autoclass:: abjad.tools.mathtools.Ratio.Ratio

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
       subgraph cluster_mathtools {
           graph [label=mathtools];
           "mathtools.NonreducedRatio" [color=4,
               group=3,
               label=NonreducedRatio,
               shape=box];
           "mathtools.Ratio" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>Ratio</B>>,
               shape=box,
               style="filled, rounded"];
           "mathtools.NonreducedRatio" -> "mathtools.Ratio";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedTuple" -> "mathtools.NonreducedRatio";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.mathtools.Ratio.Ratio.count
      ~abjad.tools.mathtools.Ratio.Ratio.index
      ~abjad.tools.mathtools.Ratio.Ratio.item_class
      ~abjad.tools.mathtools.Ratio.Ratio.items
      ~abjad.tools.mathtools.Ratio.Ratio.multipliers
      ~abjad.tools.mathtools.Ratio.Ratio.__add__
      ~abjad.tools.mathtools.Ratio.Ratio.__contains__
      ~abjad.tools.mathtools.Ratio.Ratio.__eq__
      ~abjad.tools.mathtools.Ratio.Ratio.__format__
      ~abjad.tools.mathtools.Ratio.Ratio.__getitem__
      ~abjad.tools.mathtools.Ratio.Ratio.__getslice__
      ~abjad.tools.mathtools.Ratio.Ratio.__hash__
      ~abjad.tools.mathtools.Ratio.Ratio.__iter__
      ~abjad.tools.mathtools.Ratio.Ratio.__len__
      ~abjad.tools.mathtools.Ratio.Ratio.__mul__
      ~abjad.tools.mathtools.Ratio.Ratio.__ne__
      ~abjad.tools.mathtools.Ratio.Ratio.__radd__
      ~abjad.tools.mathtools.Ratio.Ratio.__repr__
      ~abjad.tools.mathtools.Ratio.Ratio.__rmul__
      ~abjad.tools.mathtools.Ratio.Ratio.__str__

Bases
-----

- :py:class:`mathtools.NonreducedRatio <abjad.tools.mathtools.NonreducedRatio.NonreducedRatio>`

- :py:class:`datastructuretools.TypedTuple <abjad.tools.datastructuretools.TypedTuple.TypedTuple>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.mathtools.Ratio.Ratio.item_class
   :noindex:

.. autoattribute:: abjad.tools.mathtools.Ratio.Ratio.items
   :noindex:

.. autoattribute:: abjad.tools.mathtools.Ratio.Ratio.multipliers
   :noindex:

Methods
-------

.. automethod:: abjad.tools.mathtools.Ratio.Ratio.count
   :noindex:

.. automethod:: abjad.tools.mathtools.Ratio.Ratio.index
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.mathtools.Ratio.Ratio.__add__
   :noindex:

.. automethod:: abjad.tools.mathtools.Ratio.Ratio.__contains__
   :noindex:

.. automethod:: abjad.tools.mathtools.Ratio.Ratio.__eq__
   :noindex:

.. automethod:: abjad.tools.mathtools.Ratio.Ratio.__format__
   :noindex:

.. automethod:: abjad.tools.mathtools.Ratio.Ratio.__getitem__
   :noindex:

.. automethod:: abjad.tools.mathtools.Ratio.Ratio.__getslice__
   :noindex:

.. automethod:: abjad.tools.mathtools.Ratio.Ratio.__hash__
   :noindex:

.. automethod:: abjad.tools.mathtools.Ratio.Ratio.__iter__
   :noindex:

.. automethod:: abjad.tools.mathtools.Ratio.Ratio.__len__
   :noindex:

.. automethod:: abjad.tools.mathtools.Ratio.Ratio.__mul__
   :noindex:

.. automethod:: abjad.tools.mathtools.Ratio.Ratio.__ne__
   :noindex:

.. automethod:: abjad.tools.mathtools.Ratio.Ratio.__radd__
   :noindex:

.. automethod:: abjad.tools.mathtools.Ratio.Ratio.__repr__
   :noindex:

.. automethod:: abjad.tools.mathtools.Ratio.Ratio.__rmul__
   :noindex:

.. automethod:: abjad.tools.mathtools.Ratio.Ratio.__str__
   :noindex:
