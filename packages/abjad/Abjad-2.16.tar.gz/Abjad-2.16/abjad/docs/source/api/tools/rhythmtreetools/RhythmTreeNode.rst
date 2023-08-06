rhythmtreetools.RhythmTreeNode
==============================

.. autoclass:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode

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
       subgraph cluster_quantizationtools {
           graph [label=quantizationtools];
           "quantizationtools.QGridContainer" [color=4,
               group=3,
               label=QGridContainer,
               shape=box];
           "quantizationtools.QGridLeaf" [color=4,
               group=3,
               label=QGridLeaf,
               shape=box];
       }
       subgraph cluster_rhythmtreetools {
           graph [label=rhythmtreetools];
           "rhythmtreetools.RhythmTreeContainer" [color=5,
               group=4,
               label=RhythmTreeContainer,
               shape=box];
           "rhythmtreetools.RhythmTreeLeaf" [color=5,
               group=4,
               label=RhythmTreeLeaf,
               shape=box];
           "rhythmtreetools.RhythmTreeNode" [color=black,
               fontcolor=white,
               group=4,
               label=<<B>RhythmTreeNode</B>>,
               shape=oval,
               style="filled, rounded"];
           "rhythmtreetools.RhythmTreeNode" -> "rhythmtreetools.RhythmTreeContainer";
           "rhythmtreetools.RhythmTreeNode" -> "rhythmtreetools.RhythmTreeLeaf";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeNode" -> "rhythmtreetools.RhythmTreeNode";
       "rhythmtreetools.RhythmTreeContainer" -> "quantizationtools.QGridContainer";
       "rhythmtreetools.RhythmTreeNode" -> "quantizationtools.QGridLeaf";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.depth
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.depthwise_inventory
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.duration
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.graph_order
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.improper_parentage
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.name
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.parent
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.parentage_ratios
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.preprolated_duration
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.pretty_rtm_format
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.prolation
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.prolations
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.proper_parentage
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.root
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.rtm_format
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.start_offset
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.stop_offset
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.__call__
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.__copy__
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.__deepcopy__
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.__eq__
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.__format__
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.__hash__
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.__ne__
      ~abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.__repr__

Bases
-----

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.depth
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.duration
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.graph_order
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.parent
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.parentage_ratios
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.pretty_rtm_format
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.prolation
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.prolations
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.root
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.rtm_format
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.start_offset
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.stop_offset
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.name
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.preprolated_duration
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.__call__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.__copy__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode.__repr__
   :noindex:
