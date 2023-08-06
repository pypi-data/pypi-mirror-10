documentationtools.ReSTTOCDirective
===================================

.. autoclass:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective

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
           "documentationtools.ReSTTOCDirective" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>ReSTTOCDirective</B>>,
               shape=box,
               style="filled, rounded"];
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

      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.append
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.argument
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.children
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.depth
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.depthwise_inventory
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.directive
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.extend
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.graph_order
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.improper_parentage
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.index
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.insert
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.leaves
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.name
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.node_class
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.nodes
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.options
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.parent
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.pop
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.proper_parentage
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.remove
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.rest_format
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.root
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__contains__
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__copy__
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__deepcopy__
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__delitem__
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__eq__
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__format__
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__getitem__
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__hash__
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__iter__
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__len__
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__ne__
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__repr__
      ~abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__setitem__

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

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.children
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.directive
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.leaves
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.node_class
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.nodes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.options
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.rest_format
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.argument
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.append
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.extend
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.index
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.insert
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.pop
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.remove
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__contains__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__delitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__getitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__iter__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__len__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__repr__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTTOCDirective.ReSTTOCDirective.__setitem__
   :noindex:
