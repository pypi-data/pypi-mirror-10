documentationtools.GraphvizSubgraph
===================================

.. autoclass:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph

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
           "datastructuretools.TreeNode" [color=3,
               group=2,
               label=TreeNode,
               shape=box];
           "datastructuretools.TreeNode" -> "datastructuretools.TreeContainer";
       }
       subgraph cluster_documentationtools {
           graph [label=documentationtools];
           "documentationtools.GraphvizGraph" [color=4,
               group=3,
               label=GraphvizGraph,
               shape=box];
           "documentationtools.GraphvizObject" [color=4,
               group=3,
               label=GraphvizObject,
               shape=oval,
               style=bold];
           "documentationtools.GraphvizSubgraph" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>GraphvizSubgraph</B>>,
               shape=box,
               style="filled, rounded"];
           "documentationtools.GraphvizGraph" -> "documentationtools.GraphvizSubgraph";
           "documentationtools.GraphvizObject" -> "documentationtools.GraphvizGraph";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "abctools.AbjadObject" -> "documentationtools.GraphvizObject";
       "datastructuretools.TreeContainer" -> "documentationtools.GraphvizGraph";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.append
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.attributes
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.canonical_name
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.children
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.depth
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.depthwise_inventory
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.edge_attributes
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.edges
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.extend
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.graph_order
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.improper_parentage
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.index
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.insert
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.is_cluster
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.is_digraph
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.leaves
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.name
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.node_attributes
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.nodes
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.parent
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.pop
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.proper_parentage
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.remove
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.root
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.unflattened_graphviz_format
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__contains__
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__copy__
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__deepcopy__
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__delitem__
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__eq__
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__format__
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__getitem__
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__graph__
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__hash__
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__iter__
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__len__
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__ne__
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__repr__
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__setitem__
      ~abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__str__

Bases
-----

- :py:class:`documentationtools.GraphvizGraph <abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph>`

- :py:class:`datastructuretools.TreeContainer <abjad.tools.datastructuretools.TreeContainer.TreeContainer>`

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`documentationtools.GraphvizObject <abjad.tools.documentationtools.GraphvizObject.GraphvizObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.attributes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.canonical_name
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.children
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.edge_attributes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.edges
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.leaves
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.node_attributes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.nodes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.root
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.unflattened_graphviz_format
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.is_cluster
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.is_digraph
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.append
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.extend
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.index
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.insert
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.pop
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.remove
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__contains__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__delitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__getitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__graph__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__iter__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__len__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__repr__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__setitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizSubgraph.GraphvizSubgraph.__str__
   :noindex:
