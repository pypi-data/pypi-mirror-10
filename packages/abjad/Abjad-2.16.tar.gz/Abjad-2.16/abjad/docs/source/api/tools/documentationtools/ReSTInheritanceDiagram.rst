documentationtools.ReSTInheritanceDiagram
=========================================

.. autoclass:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram

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
           "documentationtools.ReSTDirective" [color=4,
               group=3,
               label=ReSTDirective,
               shape=box];
           "documentationtools.ReSTInheritanceDiagram" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>ReSTInheritanceDiagram</B>>,
               shape=box,
               style="filled, rounded"];
           "documentationtools.ReSTDirective" -> "documentationtools.ReSTInheritanceDiagram";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeContainer" -> "documentationtools.ReSTDirective";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.append
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.argument
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.children
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.depth
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.depthwise_inventory
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.directive
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.extend
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.graph_order
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.improper_parentage
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.index
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.insert
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.leaves
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.name
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.node_class
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.nodes
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.options
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.parent
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.pop
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.proper_parentage
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.remove
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.rest_format
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.root
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__contains__
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__copy__
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__deepcopy__
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__delitem__
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__eq__
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__format__
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__getitem__
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__hash__
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__iter__
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__len__
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__ne__
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__repr__
      ~abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__setitem__

Bases
-----

- :py:class:`documentationtools.ReSTDirective <abjad.tools.documentationtools.ReSTDirective.ReSTDirective>`

- :py:class:`datastructuretools.TreeContainer <abjad.tools.datastructuretools.TreeContainer.TreeContainer>`

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.children
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.directive
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.leaves
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.node_class
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.nodes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.options
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.rest_format
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.argument
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.append
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.extend
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.index
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.insert
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.pop
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.remove
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__contains__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__delitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__getitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__iter__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__len__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__repr__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTInheritanceDiagram.ReSTInheritanceDiagram.__setitem__
   :noindex:
