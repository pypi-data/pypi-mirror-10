documentationtools.GraphvizTable
================================

.. autoclass:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable

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
           "documentationtools.GraphvizTable" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>GraphvizTable</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeContainer" -> "documentationtools.GraphvizTable";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.append
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.attributes
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.children
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.depth
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.depthwise_inventory
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.extend
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.graph_order
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.improper_parentage
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.index
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.insert
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.leaves
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.name
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.nodes
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.parent
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.pop
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.proper_parentage
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.remove
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.root
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__contains__
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__copy__
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__deepcopy__
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__delitem__
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__eq__
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__format__
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__getitem__
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__hash__
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__iter__
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__len__
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__ne__
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__repr__
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__setitem__
      ~abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__str__

Bases
-----

- :py:class:`datastructuretools.TreeContainer <abjad.tools.datastructuretools.TreeContainer.TreeContainer>`

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.attributes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.children
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.leaves
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.nodes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.append
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.extend
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.index
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.insert
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.pop
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.remove
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__contains__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__delitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__getitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__iter__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__len__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__repr__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__setitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTable.GraphvizTable.__str__
   :noindex:
