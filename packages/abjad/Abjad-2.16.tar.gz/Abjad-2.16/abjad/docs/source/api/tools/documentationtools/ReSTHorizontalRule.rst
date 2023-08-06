documentationtools.ReSTHorizontalRule
=====================================

.. autoclass:: abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule

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
           "documentationtools.ReSTHorizontalRule" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>ReSTHorizontalRule</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeNode" -> "documentationtools.ReSTHorizontalRule";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.depth
      ~abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.depthwise_inventory
      ~abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.graph_order
      ~abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.improper_parentage
      ~abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.name
      ~abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.parent
      ~abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.proper_parentage
      ~abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.rest_format
      ~abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.root
      ~abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.__copy__
      ~abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.__deepcopy__
      ~abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.__eq__
      ~abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.__format__
      ~abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.__hash__
      ~abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.__ne__
      ~abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.__repr__

Bases
-----

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.rest_format
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.name
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTHorizontalRule.ReSTHorizontalRule.__repr__
   :noindex:
