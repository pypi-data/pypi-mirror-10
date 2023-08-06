documentationtools.GraphvizTableCell
====================================

.. autoclass:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell

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
           "datastructuretools.TreeNode" [color=3,
               group=2,
               label=TreeNode,
               shape=box];
       }
       subgraph cluster_documentationtools {
           graph [label=documentationtools];
           "documentationtools.GraphvizTableCell" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>GraphvizTableCell</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeNode" -> "documentationtools.GraphvizTableCell";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.attributes
      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.depth
      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.depthwise_inventory
      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.graph_order
      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.improper_parentage
      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.label
      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.name
      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.parent
      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.proper_parentage
      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.root
      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.__copy__
      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.__deepcopy__
      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.__eq__
      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.__format__
      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.__hash__
      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.__ne__
      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.__repr__
      ~abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.__str__

Bases
-----

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.attributes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.label
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.name
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.__repr__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableCell.GraphvizTableCell.__str__
   :noindex:
