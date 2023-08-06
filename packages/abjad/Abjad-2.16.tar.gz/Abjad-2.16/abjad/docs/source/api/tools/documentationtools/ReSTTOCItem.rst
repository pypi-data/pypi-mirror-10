documentationtools.ReSTTOCItem
==============================

.. autoclass:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem

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
           "documentationtools.ReSTTOCItem" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>ReSTTOCItem</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeNode" -> "documentationtools.ReSTTOCItem";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.depth
      ~abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.depthwise_inventory
      ~abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.graph_order
      ~abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.improper_parentage
      ~abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.name
      ~abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.parent
      ~abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.proper_parentage
      ~abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.rest_format
      ~abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.root
      ~abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.text
      ~abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.__copy__
      ~abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.__deepcopy__
      ~abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.__eq__
      ~abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.__format__
      ~abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.__hash__
      ~abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.__ne__
      ~abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.__repr__

Bases
-----

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.rest_format
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.name
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.text
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCItem.ReSTTOCItem.__repr__
   :noindex:
