documentationtools.ReSTDocument
===============================

.. autoclass:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument

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
           "documentationtools.ReSTDocument" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>ReSTDocument</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeContainer" -> "documentationtools.ReSTDocument";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.append
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.children
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.depth
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.depthwise_inventory
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.extend
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.graph_order
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.improper_parentage
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.index
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.insert
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.leaves
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.name
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.node_class
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.nodes
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.parent
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.pop
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.proper_parentage
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.remove
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.rest_format
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.root
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__contains__
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__copy__
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__deepcopy__
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__delitem__
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__eq__
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__format__
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__getitem__
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__hash__
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__iter__
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__len__
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__ne__
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__repr__
      ~abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__setitem__

Bases
-----

- :py:class:`datastructuretools.TreeContainer <abjad.tools.datastructuretools.TreeContainer.TreeContainer>`

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.children
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.leaves
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.node_class
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.nodes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.rest_format
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.append
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.extend
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.index
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.insert
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.pop
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.remove
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__contains__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__delitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__getitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__iter__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__len__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__repr__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ReSTDocument.ReSTDocument.__setitem__
   :noindex:
