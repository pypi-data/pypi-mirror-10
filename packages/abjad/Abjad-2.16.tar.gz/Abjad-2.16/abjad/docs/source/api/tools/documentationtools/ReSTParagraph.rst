documentationtools.ReSTParagraph
================================

.. autoclass:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph

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
           "documentationtools.ReSTParagraph" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>ReSTParagraph</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeNode" -> "documentationtools.ReSTParagraph";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.depth
      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.depthwise_inventory
      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.graph_order
      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.improper_parentage
      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.name
      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.parent
      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.proper_parentage
      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.rest_format
      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.root
      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.text
      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.wrap
      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.__copy__
      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.__deepcopy__
      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.__eq__
      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.__format__
      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.__hash__
      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.__ne__
      ~abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.__repr__

Bases
-----

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.rest_format
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.name
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.text
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.wrap
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTParagraph.ReSTParagraph.__repr__
   :noindex:
