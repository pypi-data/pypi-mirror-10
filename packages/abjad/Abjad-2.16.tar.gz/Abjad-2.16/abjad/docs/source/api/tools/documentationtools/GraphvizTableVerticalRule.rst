documentationtools.GraphvizTableVerticalRule
============================================

.. autoclass:: abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule

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
           "documentationtools.GraphvizTableVerticalRule" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>GraphvizTableVerticalRule</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeNode" -> "documentationtools.GraphvizTableVerticalRule";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.depth
      ~abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.depthwise_inventory
      ~abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.graph_order
      ~abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.improper_parentage
      ~abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.name
      ~abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.parent
      ~abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.proper_parentage
      ~abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.root
      ~abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.__copy__
      ~abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.__deepcopy__
      ~abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.__eq__
      ~abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.__format__
      ~abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.__hash__
      ~abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.__ne__
      ~abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.__repr__
      ~abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.__str__

Bases
-----

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.name
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.__repr__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizTableVerticalRule.GraphvizTableVerticalRule.__str__
   :noindex:
