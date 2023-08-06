documentationtools.ReSTHeading
==============================

.. autoclass:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading

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
           "documentationtools.ReSTHeading" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>ReSTHeading</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeNode" -> "documentationtools.ReSTHeading";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.depth
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.depthwise_inventory
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.graph_order
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.heading_characters
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.improper_parentage
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.level
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.name
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.parent
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.proper_parentage
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.rest_format
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.root
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.text
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.__copy__
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.__deepcopy__
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.__eq__
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.__format__
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.__hash__
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.__ne__
      ~abjad.tools.documentationtools.ReSTHeading.ReSTHeading.__repr__

Bases
-----

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.heading_characters
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.rest_format
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.level
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.name
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.text
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTHeading.ReSTHeading.__repr__
   :noindex:
