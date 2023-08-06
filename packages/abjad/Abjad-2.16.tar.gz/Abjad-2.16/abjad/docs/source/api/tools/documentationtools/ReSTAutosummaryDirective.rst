documentationtools.ReSTAutosummaryDirective
===========================================

.. autoclass:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective

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
           "documentationtools.ReSTAutosummaryDirective" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>ReSTAutosummaryDirective</B>>,
               shape=box,
               style="filled, rounded"];
           "documentationtools.ReSTDirective" [color=4,
               group=3,
               label=ReSTDirective,
               shape=box];
           "documentationtools.ReSTDirective" -> "documentationtools.ReSTAutosummaryDirective";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeContainer" -> "documentationtools.ReSTDirective";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.append
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.argument
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.children
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.depth
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.depthwise_inventory
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.directive
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.extend
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.graph_order
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.improper_parentage
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.index
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.insert
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.leaves
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.name
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.node_class
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.nodes
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.options
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.parent
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.pop
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.proper_parentage
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.remove
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.rest_format
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.root
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__contains__
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__copy__
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__deepcopy__
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__delitem__
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__eq__
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__format__
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__getitem__
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__hash__
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__iter__
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__len__
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__ne__
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__repr__
      ~abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__setitem__

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

.. autoattribute:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.children
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.directive
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.leaves
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.node_class
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.nodes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.options
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.rest_format
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.argument
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.append
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.extend
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.index
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.insert
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.pop
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.remove
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__contains__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__delitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__getitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__iter__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__len__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__repr__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTAutosummaryDirective.ReSTAutosummaryDirective.__setitem__
   :noindex:
