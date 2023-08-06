documentationtools.GraphvizField
================================

.. autoclass:: abjad.tools.documentationtools.GraphvizField.GraphvizField

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
           "documentationtools.GraphvizField" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>GraphvizField</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeNode" -> "documentationtools.GraphvizField";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.canonical_name
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.depth
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.depthwise_inventory
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.edges
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.field_name
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.graph_order
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.improper_parentage
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.label
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.name
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.parent
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.proper_parentage
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.root
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.struct
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.__copy__
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.__deepcopy__
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.__eq__
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.__format__
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.__hash__
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.__ne__
      ~abjad.tools.documentationtools.GraphvizField.GraphvizField.__repr__

Bases
-----

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizField.GraphvizField.canonical_name
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizField.GraphvizField.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizField.GraphvizField.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizField.GraphvizField.edges
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizField.GraphvizField.field_name
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizField.GraphvizField.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizField.GraphvizField.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizField.GraphvizField.label
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizField.GraphvizField.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizField.GraphvizField.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizField.GraphvizField.root
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizField.GraphvizField.struct
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizField.GraphvizField.name
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.GraphvizField.GraphvizField.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizField.GraphvizField.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizField.GraphvizField.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizField.GraphvizField.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizField.GraphvizField.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizField.GraphvizField.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizField.GraphvizField.__repr__
   :noindex:
