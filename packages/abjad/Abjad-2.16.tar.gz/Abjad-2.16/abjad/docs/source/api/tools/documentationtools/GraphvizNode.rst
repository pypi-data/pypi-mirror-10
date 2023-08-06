documentationtools.GraphvizNode
===============================

.. autoclass:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode

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
           "documentationtools.GraphvizNode" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>GraphvizNode</B>>,
               shape=box,
               style="filled, rounded"];
           "documentationtools.GraphvizObject" [color=4,
               group=3,
               label=GraphvizObject,
               shape=oval,
               style=bold];
           "documentationtools.GraphvizObject" -> "documentationtools.GraphvizNode";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "abctools.AbjadObject" -> "documentationtools.GraphvizObject";
       "datastructuretools.TreeContainer" -> "documentationtools.GraphvizNode";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.all_edges
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.append
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.attributes
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.canonical_name
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.children
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.depth
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.depthwise_inventory
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.edges
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.extend
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.graph_order
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.improper_parentage
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.index
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.insert
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.leaves
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.name
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.nodes
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.parent
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.pop
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.proper_parentage
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.remove
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.root
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__contains__
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__copy__
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__deepcopy__
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__delitem__
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__eq__
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__format__
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__getitem__
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__hash__
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__iter__
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__len__
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__ne__
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__repr__
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__setitem__
      ~abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__str__

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

.. autoattribute:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.all_edges
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.attributes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.canonical_name
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.children
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.edges
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.leaves
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.nodes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.append
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.extend
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.index
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.insert
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.pop
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.remove
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__contains__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__delitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__getitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__iter__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__len__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__repr__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__setitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizNode.GraphvizNode.__str__
   :noindex:
