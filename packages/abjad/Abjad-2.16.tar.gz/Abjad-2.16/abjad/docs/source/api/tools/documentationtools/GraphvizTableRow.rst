documentationtools.GraphvizTableRow
===================================

.. autoclass:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow

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
           "documentationtools.GraphvizTableRow" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>GraphvizTableRow</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeContainer" -> "documentationtools.GraphvizTableRow";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.append
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.children
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.depth
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.depthwise_inventory
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.extend
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.graph_order
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.improper_parentage
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.index
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.insert
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.leaves
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.name
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.nodes
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.parent
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.pop
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.proper_parentage
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.remove
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.root
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__contains__
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__copy__
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__deepcopy__
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__delitem__
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__eq__
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__format__
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__getitem__
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__hash__
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__iter__
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__len__
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__ne__
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__repr__
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__setitem__
      ~abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__str__

Bases
-----

- :py:class:`datastructuretools.TreeContainer <abjad.tools.datastructuretools.TreeContainer.TreeContainer>`

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.children
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.leaves
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.nodes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.append
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.extend
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.index
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.insert
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.pop
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.remove
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__contains__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__delitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__getitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__iter__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__len__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__repr__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__setitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableRow.GraphvizTableRow.__str__
   :noindex:
