datastructuretools.TreeNode
===========================

.. autoclass:: abjad.tools.datastructuretools.TreeNode.TreeNode

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
           "datastructuretools.TreeContainer" [color=3,
               group=2,
               label=TreeContainer,
               shape=box];
           "datastructuretools.TreeNode" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>TreeNode</B>>,
               shape=box,
               style="filled, rounded"];
           "datastructuretools.TreeNode" -> "datastructuretools.TreeContainer";
       }
       subgraph cluster_documentationtools {
           graph [label=documentationtools];
           "documentationtools.GraphvizField" [color=4,
               group=3,
               label=GraphvizField,
               shape=box];
           "documentationtools.GraphvizGraph" [color=4,
               group=3,
               label=" ",
               shape=invis,
               style=transparent];
           "documentationtools.GraphvizGroup" [color=4,
               group=3,
               label=" ",
               shape=invis,
               style=transparent];
           "documentationtools.GraphvizNode" [color=4,
               group=3,
               label=" ",
               shape=invis,
               style=transparent];
           "documentationtools.GraphvizTable" [color=4,
               group=3,
               label=" ",
               shape=invis,
               style=transparent];
           "documentationtools.GraphvizTableCell" [color=4,
               group=3,
               label=GraphvizTableCell,
               shape=box];
           "documentationtools.GraphvizTableHorizontalRule" [color=4,
               group=3,
               label=GraphvizTableHorizontalRule,
               shape=box];
           "documentationtools.GraphvizTableRow" [color=4,
               group=3,
               label=" ",
               shape=invis,
               style=transparent];
           "documentationtools.GraphvizTableVerticalRule" [color=4,
               group=3,
               label=GraphvizTableVerticalRule,
               shape=box];
           "documentationtools.ReSTAutosummaryItem" [color=4,
               group=3,
               label=ReSTAutosummaryItem,
               shape=box];
           "documentationtools.ReSTDirective" [color=4,
               group=3,
               label=" ",
               shape=invis,
               style=transparent];
           "documentationtools.ReSTDocument" [color=4,
               group=3,
               label=" ",
               shape=invis,
               style=transparent];
           "documentationtools.ReSTHeading" [color=4,
               group=3,
               label=ReSTHeading,
               shape=box];
           "documentationtools.ReSTHorizontalRule" [color=4,
               group=3,
               label=ReSTHorizontalRule,
               shape=box];
           "documentationtools.ReSTParagraph" [color=4,
               group=3,
               label=ReSTParagraph,
               shape=box];
           "documentationtools.ReSTTOCItem" [color=4,
               group=3,
               label=ReSTTOCItem,
               shape=box];
       }
       subgraph cluster_quantizationtools {
           graph [label=quantizationtools];
           "quantizationtools.QGridLeaf" [color=5,
               group=4,
               label=" ",
               shape=invis,
               style=transparent];
       }
       subgraph cluster_rhythmtreetools {
           graph [label=rhythmtreetools];
           "rhythmtreetools.RhythmTreeContainer" [color=6,
               group=5,
               label=" ",
               shape=invis,
               style=transparent];
           "rhythmtreetools.RhythmTreeLeaf" [color=6,
               group=5,
               label=" ",
               shape=invis,
               style=transparent];
           "rhythmtreetools.RhythmTreeNode" [color=6,
               group=5,
               label=RhythmTreeNode,
               shape=oval,
               style=bold];
           "rhythmtreetools.RhythmTreeNode" -> "rhythmtreetools.RhythmTreeContainer";
           "rhythmtreetools.RhythmTreeNode" -> "rhythmtreetools.RhythmTreeLeaf";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeContainer" -> "documentationtools.GraphvizGraph";
       "datastructuretools.TreeContainer" -> "documentationtools.GraphvizGroup";
       "datastructuretools.TreeContainer" -> "documentationtools.GraphvizNode";
       "datastructuretools.TreeContainer" -> "documentationtools.GraphvizTable";
       "datastructuretools.TreeContainer" -> "documentationtools.GraphvizTableRow";
       "datastructuretools.TreeContainer" -> "documentationtools.ReSTDirective";
       "datastructuretools.TreeContainer" -> "documentationtools.ReSTDocument";
       "datastructuretools.TreeContainer" -> "rhythmtreetools.RhythmTreeContainer";
       "datastructuretools.TreeNode" -> "documentationtools.GraphvizField";
       "datastructuretools.TreeNode" -> "documentationtools.GraphvizTableCell";
       "datastructuretools.TreeNode" -> "documentationtools.GraphvizTableHorizontalRule";
       "datastructuretools.TreeNode" -> "documentationtools.GraphvizTableVerticalRule";
       "datastructuretools.TreeNode" -> "documentationtools.ReSTAutosummaryItem";
       "datastructuretools.TreeNode" -> "documentationtools.ReSTHeading";
       "datastructuretools.TreeNode" -> "documentationtools.ReSTHorizontalRule";
       "datastructuretools.TreeNode" -> "documentationtools.ReSTParagraph";
       "datastructuretools.TreeNode" -> "documentationtools.ReSTTOCItem";
       "datastructuretools.TreeNode" -> "rhythmtreetools.RhythmTreeNode";
       "rhythmtreetools.RhythmTreeNode" -> "quantizationtools.QGridLeaf";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.datastructuretools.TreeNode.TreeNode.depth
      ~abjad.tools.datastructuretools.TreeNode.TreeNode.depthwise_inventory
      ~abjad.tools.datastructuretools.TreeNode.TreeNode.graph_order
      ~abjad.tools.datastructuretools.TreeNode.TreeNode.improper_parentage
      ~abjad.tools.datastructuretools.TreeNode.TreeNode.name
      ~abjad.tools.datastructuretools.TreeNode.TreeNode.parent
      ~abjad.tools.datastructuretools.TreeNode.TreeNode.proper_parentage
      ~abjad.tools.datastructuretools.TreeNode.TreeNode.root
      ~abjad.tools.datastructuretools.TreeNode.TreeNode.__copy__
      ~abjad.tools.datastructuretools.TreeNode.TreeNode.__deepcopy__
      ~abjad.tools.datastructuretools.TreeNode.TreeNode.__eq__
      ~abjad.tools.datastructuretools.TreeNode.TreeNode.__format__
      ~abjad.tools.datastructuretools.TreeNode.TreeNode.__hash__
      ~abjad.tools.datastructuretools.TreeNode.TreeNode.__ne__
      ~abjad.tools.datastructuretools.TreeNode.TreeNode.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.datastructuretools.TreeNode.TreeNode.depth
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TreeNode.TreeNode.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TreeNode.TreeNode.graph_order
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TreeNode.TreeNode.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TreeNode.TreeNode.parent
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TreeNode.TreeNode.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TreeNode.TreeNode.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.datastructuretools.TreeNode.TreeNode.name
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.datastructuretools.TreeNode.TreeNode.__copy__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeNode.TreeNode.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeNode.TreeNode.__eq__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeNode.TreeNode.__format__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeNode.TreeNode.__hash__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeNode.TreeNode.__ne__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeNode.TreeNode.__repr__
   :noindex:
