documentationtools.GraphvizTableHorizontalRule
==============================================

.. autoclass:: abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule

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
           "documentationtools.GraphvizTableHorizontalRule" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>GraphvizTableHorizontalRule</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeNode" -> "documentationtools.GraphvizTableHorizontalRule";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.depth
      ~abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.depthwise_inventory
      ~abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.graph_order
      ~abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.improper_parentage
      ~abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.name
      ~abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.parent
      ~abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.proper_parentage
      ~abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.root
      ~abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.__copy__
      ~abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.__deepcopy__
      ~abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.__eq__
      ~abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.__format__
      ~abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.__hash__
      ~abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.__ne__
      ~abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.__repr__
      ~abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.__str__

Bases
-----

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.name
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.__repr__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableHorizontalRule.GraphvizTableHorizontalRule.__str__
   :noindex:
