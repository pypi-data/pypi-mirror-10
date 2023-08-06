mathtools.NonreducedRatio
=========================

.. autoclass:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio

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
           "mathtools.NonreducedRatio" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>NonreducedRatio</B>>,
               shape=box,
               style="filled, rounded"];
           "mathtools.Ratio" [color=4,
               group=3,
               label=Ratio,
               shape=box];
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

      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.count
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.index
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.item_class
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.items
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.multipliers
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__add__
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__contains__
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__eq__
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__format__
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__getitem__
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__getslice__
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__hash__
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__iter__
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__len__
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__mul__
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__ne__
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__radd__
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__repr__
      ~abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__rmul__

Bases
-----

- :py:class:`datastructuretools.TypedTuple <abjad.tools.datastructuretools.TypedTuple.TypedTuple>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.item_class
   :noindex:

.. autoattribute:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.items
   :noindex:

.. autoattribute:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.multipliers
   :noindex:

Methods
-------

.. automethod:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.count
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.index
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__add__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__contains__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__eq__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__format__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__getitem__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__getslice__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__hash__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__iter__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__len__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__mul__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__ne__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__radd__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__repr__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedRatio.NonreducedRatio.__rmul__
   :noindex:
