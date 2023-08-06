rhythmtreetools.RhythmTreeContainer
===================================

.. autoclass:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer

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
       subgraph cluster_quantizationtools {
           graph [label=quantizationtools];
           "quantizationtools.QGridContainer" [color=4,
               group=3,
               label=QGridContainer,
               shape=box];
       }
       subgraph cluster_rhythmtreetools {
           graph [label=rhythmtreetools];
           "rhythmtreetools.RhythmTreeContainer" [color=black,
               fontcolor=white,
               group=4,
               label=<<B>RhythmTreeContainer</B>>,
               shape=box,
               style="filled, rounded"];
           "rhythmtreetools.RhythmTreeNode" [color=5,
               group=4,
               label=RhythmTreeNode,
               shape=oval,
               style=bold];
           "rhythmtreetools.RhythmTreeNode" -> "rhythmtreetools.RhythmTreeContainer";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeContainer" -> "rhythmtreetools.RhythmTreeContainer";
       "datastructuretools.TreeNode" -> "rhythmtreetools.RhythmTreeNode";
       "rhythmtreetools.RhythmTreeContainer" -> "quantizationtools.QGridContainer";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.append
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.children
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.depth
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.depthwise_inventory
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.duration
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.extend
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.graph_order
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.improper_parentage
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.index
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.insert
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.leaves
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.name
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.nodes
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.parent
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.parentage_ratios
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.pop
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.preprolated_duration
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.pretty_rtm_format
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.prolation
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.prolations
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.proper_parentage
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.remove
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.root
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.rtm_format
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.start_offset
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.stop_offset
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__add__
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__call__
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__contains__
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__copy__
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__deepcopy__
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__delitem__
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__eq__
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__format__
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__getitem__
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__graph__
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__hash__
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__iter__
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__len__
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__ne__
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__repr__
      ~abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__setitem__

Bases
-----

- :py:class:`rhythmtreetools.RhythmTreeNode <abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode>`

- :py:class:`datastructuretools.TreeContainer <abjad.tools.datastructuretools.TreeContainer.TreeContainer>`

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.children
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.depth
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.duration
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.graph_order
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.leaves
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.nodes
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.parent
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.parentage_ratios
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.pretty_rtm_format
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.prolation
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.prolations
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.root
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.rtm_format
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.start_offset
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.stop_offset
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.name
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.preprolated_duration
   :noindex:

Methods
-------

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.append
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.extend
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.index
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.insert
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.pop
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.remove
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__add__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__call__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__contains__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__copy__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__delitem__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__getitem__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__graph__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__iter__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__len__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__repr__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeContainer.RhythmTreeContainer.__setitem__
   :noindex:
