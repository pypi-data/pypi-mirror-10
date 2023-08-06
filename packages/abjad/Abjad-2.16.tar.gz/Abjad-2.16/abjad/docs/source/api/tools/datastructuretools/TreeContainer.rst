datastructuretools.TreeContainer
================================

.. autoclass:: abjad.tools.datastructuretools.TreeContainer.TreeContainer

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
           "datastructuretools.TreeContainer" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>TreeContainer</B>>,
               shape=box,
               style="filled, rounded"];
           "datastructuretools.TreeNode" [color=3,
               group=2,
               label=TreeNode,
               shape=box];
           "datastructuretools.TreeNode" -> "datastructuretools.TreeContainer";
       }
       subgraph cluster_documentationtools {
           graph [label=documentationtools];
           "documentationtools.GraphvizDirective" [color=4,
               group=3,
               label=GraphvizDirective,
               shape=box];
           "documentationtools.GraphvizGraph" [color=4,
               group=3,
               label=GraphvizGraph,
               shape=box];
           "documentationtools.GraphvizGroup" [color=4,
               group=3,
               label=GraphvizGroup,
               shape=box];
           "documentationtools.GraphvizNode" [color=4,
               group=3,
               label=GraphvizNode,
               shape=box];
           "documentationtools.GraphvizSubgraph" [color=4,
               group=3,
               label=GraphvizSubgraph,
               shape=box];
           "documentationtools.GraphvizTable" [color=4,
               group=3,
               label=GraphvizTable,
               shape=box];
           "documentationtools.GraphvizTableRow" [color=4,
               group=3,
               label=GraphvizTableRow,
               shape=box];
           "documentationtools.ReSTAutodocDirective" [color=4,
               group=3,
               label=ReSTAutodocDirective,
               shape=box];
           "documentationtools.ReSTAutosummaryDirective" [color=4,
               group=3,
               label=ReSTAutosummaryDirective,
               shape=box];
           "documentationtools.ReSTDirective" [color=4,
               group=3,
               label=ReSTDirective,
               shape=box];
           "documentationtools.ReSTDocument" [color=4,
               group=3,
               label=ReSTDocument,
               shape=box];
           "documentationtools.ReSTInheritanceDiagram" [color=4,
               group=3,
               label=ReSTInheritanceDiagram,
               shape=box];
           "documentationtools.ReSTLineageDirective" [color=4,
               group=3,
               label=ReSTLineageDirective,
               shape=box];
           "documentationtools.ReSTOnlyDirective" [color=4,
               group=3,
               label=ReSTOnlyDirective,
               shape=box];
           "documentationtools.ReSTTOCDirective" [color=4,
               group=3,
               label=ReSTTOCDirective,
               shape=box];
           "documentationtools.GraphvizGraph" -> "documentationtools.GraphvizSubgraph";
           "documentationtools.ReSTDirective" -> "documentationtools.GraphvizDirective";
           "documentationtools.ReSTDirective" -> "documentationtools.ReSTAutodocDirective";
           "documentationtools.ReSTDirective" -> "documentationtools.ReSTAutosummaryDirective";
           "documentationtools.ReSTDirective" -> "documentationtools.ReSTInheritanceDiagram";
           "documentationtools.ReSTDirective" -> "documentationtools.ReSTLineageDirective";
           "documentationtools.ReSTDirective" -> "documentationtools.ReSTOnlyDirective";
           "documentationtools.ReSTDirective" -> "documentationtools.ReSTTOCDirective";
       }
       subgraph cluster_quantizationtools {
           graph [label=quantizationtools];
           "quantizationtools.QGridContainer" [color=5,
               group=4,
               label=QGridContainer,
               shape=box];
       }
       subgraph cluster_rhythmtreetools {
           graph [label=rhythmtreetools];
           "rhythmtreetools.RhythmTreeContainer" [color=6,
               group=5,
               label=RhythmTreeContainer,
               shape=box];
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
       "rhythmtreetools.RhythmTreeContainer" -> "quantizationtools.QGridContainer";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.append
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.children
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.depth
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.depthwise_inventory
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.extend
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.graph_order
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.improper_parentage
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.index
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.insert
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.leaves
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.name
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.nodes
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.parent
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.pop
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.proper_parentage
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.remove
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.root
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.__contains__
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.__copy__
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.__deepcopy__
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.__delitem__
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.__eq__
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.__format__
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.__getitem__
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.__hash__
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.__iter__
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.__len__
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.__ne__
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.__repr__
      ~abjad.tools.datastructuretools.TreeContainer.TreeContainer.__setitem__

Bases
-----

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.children
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.depth
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.graph_order
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.leaves
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.nodes
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.parent
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.append
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.extend
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.index
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.insert
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.pop
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.remove
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.__contains__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.__copy__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.__delitem__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.__eq__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.__format__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.__getitem__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.__hash__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.__iter__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.__len__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.__ne__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.__repr__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TreeContainer.TreeContainer.__setitem__
   :noindex:
