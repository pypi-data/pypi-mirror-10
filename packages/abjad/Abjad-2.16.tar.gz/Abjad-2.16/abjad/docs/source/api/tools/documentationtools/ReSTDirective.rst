documentationtools.ReSTDirective
================================

.. autoclass:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective

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
           "documentationtools.GraphvizDirective" [color=4,
               group=3,
               label=GraphvizDirective,
               shape=box];
           "documentationtools.ReSTAutodocDirective" [color=4,
               group=3,
               label=ReSTAutodocDirective,
               shape=box];
           "documentationtools.ReSTAutosummaryDirective" [color=4,
               group=3,
               label=ReSTAutosummaryDirective,
               shape=box];
           "documentationtools.ReSTDirective" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>ReSTDirective</B>>,
               shape=box,
               style="filled, rounded"];
           "documentationtools.ReSTInheritanceDiagram" [color=4,
               group=3,
               label=ReSTInheritanceDiagram,
               shape=box];
           "documentationtools.ReSTLineageDirective" [color=4,
               group=3,
               label=ReSTLineageDirective,
               shape=box];
           "documentationtools.ReSTOnlyDirective" [color=4,
               group=3,
               label=ReSTOnlyDirective,
               shape=box];
           "documentationtools.ReSTTOCDirective" [color=4,
               group=3,
               label=ReSTTOCDirective,
               shape=box];
           "documentationtools.ReSTDirective" -> "documentationtools.GraphvizDirective";
           "documentationtools.ReSTDirective" -> "documentationtools.ReSTAutodocDirective";
           "documentationtools.ReSTDirective" -> "documentationtools.ReSTAutosummaryDirective";
           "documentationtools.ReSTDirective" -> "documentationtools.ReSTInheritanceDiagram";
           "documentationtools.ReSTDirective" -> "documentationtools.ReSTLineageDirective";
           "documentationtools.ReSTDirective" -> "documentationtools.ReSTOnlyDirective";
           "documentationtools.ReSTDirective" -> "documentationtools.ReSTTOCDirective";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeContainer" -> "documentationtools.ReSTDirective";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.append
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.argument
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.children
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.depth
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.depthwise_inventory
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.directive
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.extend
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.graph_order
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.improper_parentage
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.index
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.insert
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.leaves
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.name
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.node_class
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.nodes
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.options
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.parent
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.pop
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.proper_parentage
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.remove
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.rest_format
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.root
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__contains__
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__copy__
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__deepcopy__
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__delitem__
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__eq__
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__format__
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__getitem__
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__hash__
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__iter__
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__len__
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__ne__
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__repr__
      ~abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__setitem__

Bases
-----

- :py:class:`datastructuretools.TreeContainer <abjad.tools.datastructuretools.TreeContainer.TreeContainer>`

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.children
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.leaves
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.node_class
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.nodes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.options
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.rest_format
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.argument
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.directive
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.append
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.extend
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.index
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.insert
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.pop
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.remove
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__contains__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__delitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__getitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__iter__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__len__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__repr__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDirective.ReSTDirective.__setitem__
   :noindex:
