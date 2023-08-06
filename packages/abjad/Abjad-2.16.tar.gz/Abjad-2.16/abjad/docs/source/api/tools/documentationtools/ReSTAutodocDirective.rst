documentationtools.ReSTAutodocDirective
=======================================

.. autoclass:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective

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
           "documentationtools.ReSTAutodocDirective" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>ReSTAutodocDirective</B>>,
               shape=box,
               style="filled, rounded"];
           "documentationtools.ReSTDirective" [color=4,
               group=3,
               label=ReSTDirective,
               shape=box];
           "documentationtools.ReSTDirective" -> "documentationtools.ReSTAutodocDirective";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeContainer" -> "documentationtools.ReSTDirective";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.append
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.argument
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.children
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.depth
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.depthwise_inventory
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.directive
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.extend
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.graph_order
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.improper_parentage
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.index
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.insert
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.leaves
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.name
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.node_class
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.nodes
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.options
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.parent
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.pop
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.proper_parentage
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.remove
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.rest_format
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.root
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__contains__
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__copy__
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__deepcopy__
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__delitem__
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__eq__
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__format__
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__getitem__
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__hash__
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__iter__
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__len__
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__ne__
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__repr__
      ~abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__setitem__

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

.. autoattribute:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.children
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.leaves
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.node_class
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.nodes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.options
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.rest_format
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.argument
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.directive
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.append
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.extend
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.index
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.insert
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.pop
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.remove
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__contains__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__delitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__getitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__iter__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__len__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__repr__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutodocDirective.ReSTAutodocDirective.__setitem__
   :noindex:
