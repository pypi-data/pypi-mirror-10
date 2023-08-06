documentationtools.GraphvizGraph
================================

.. autoclass:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph

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
           "documentationtools.GraphvizGraph" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>GraphvizGraph</B>>,
               shape=box,
               style="filled, rounded"];
           "documentationtools.GraphvizObject" [color=4,
               group=3,
               label=GraphvizObject,
               shape=oval,
               style=bold];
           "documentationtools.GraphvizSubgraph" [color=4,
               group=3,
               label=GraphvizSubgraph,
               shape=box];
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

      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.append
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.attributes
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.canonical_name
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.children
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.depth
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.depthwise_inventory
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.edge_attributes
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.extend
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.graph_order
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.improper_parentage
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.index
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.insert
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.is_digraph
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.leaves
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.name
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.node_attributes
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.nodes
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.parent
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.pop
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.proper_parentage
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.remove
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.root
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.unflattened_graphviz_format
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__contains__
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__copy__
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__deepcopy__
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__delitem__
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__eq__
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__format__
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__getitem__
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__graph__
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__hash__
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__iter__
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__len__
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__ne__
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__repr__
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__setitem__
      ~abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__str__

Bases
-----

- :py:class:`datastructuretools.TreeContainer <abjad.tools.datastructuretools.TreeContainer.TreeContainer>`

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`documentationtools.GraphvizObject <abjad.tools.documentationtools.GraphvizObject.GraphvizObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.attributes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.canonical_name
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.children
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.edge_attributes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.leaves
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.node_attributes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.nodes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.root
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.unflattened_graphviz_format
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.is_digraph
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.append
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.extend
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.index
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.insert
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.pop
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.remove
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__contains__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__delitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__getitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__graph__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__iter__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__len__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__repr__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__setitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGraph.GraphvizGraph.__str__
   :noindex:
