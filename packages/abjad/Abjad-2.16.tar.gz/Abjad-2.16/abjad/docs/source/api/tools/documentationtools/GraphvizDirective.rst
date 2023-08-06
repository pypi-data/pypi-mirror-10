documentationtools.GraphvizDirective
====================================

.. autoclass:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective

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
           "documentationtools.GraphvizDirective" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>GraphvizDirective</B>>,
               shape=box,
               style="filled, rounded"];
           "documentationtools.ReSTDirective" [color=4,
               group=3,
               label=ReSTDirective,
               shape=box];
           "documentationtools.ReSTDirective" -> "documentationtools.GraphvizDirective";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeContainer" -> "documentationtools.ReSTDirective";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.append
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.argument
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.children
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.depth
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.depthwise_inventory
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.directive
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.extend
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.graph
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.graph_order
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.improper_parentage
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.index
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.insert
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.leaves
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.name
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.node_class
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.nodes
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.options
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.parent
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.pop
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.proper_parentage
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.remove
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.rest_format
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.root
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__contains__
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__copy__
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__deepcopy__
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__delitem__
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__eq__
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__format__
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__getitem__
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__hash__
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__iter__
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__len__
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__ne__
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__repr__
      ~abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__setitem__

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

.. autoattribute:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.children
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.directive
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.graph
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.leaves
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.node_class
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.nodes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.options
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.rest_format
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.argument
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.append
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.extend
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.index
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.insert
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.pop
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.remove
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__contains__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__delitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__getitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__iter__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__len__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__repr__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizDirective.GraphvizDirective.__setitem__
   :noindex:
