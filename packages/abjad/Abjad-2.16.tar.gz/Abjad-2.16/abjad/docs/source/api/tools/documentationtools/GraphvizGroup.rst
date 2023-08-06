documentationtools.GraphvizGroup
================================

.. autoclass:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup

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
           "documentationtools.GraphvizGroup" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>GraphvizGroup</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeContainer" -> "documentationtools.GraphvizGroup";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.append
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.children
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.depth
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.depthwise_inventory
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.extend
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.graph_order
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.improper_parentage
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.index
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.insert
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.leaves
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.name
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.nodes
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.parent
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.pop
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.proper_parentage
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.remove
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.root
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__contains__
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__copy__
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__deepcopy__
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__delitem__
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__eq__
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__format__
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__getitem__
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__hash__
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__iter__
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__len__
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__ne__
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__repr__
      ~abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__setitem__

Bases
-----

- :py:class:`datastructuretools.TreeContainer <abjad.tools.datastructuretools.TreeContainer.TreeContainer>`

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.children
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.depth
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.graph_order
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.leaves
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.nodes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.parent
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.root
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.append
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.extend
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.index
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.insert
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.pop
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.remove
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__contains__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__copy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__delitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__getitem__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__iter__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__len__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__repr__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizGroup.GraphvizGroup.__setitem__
   :noindex:
