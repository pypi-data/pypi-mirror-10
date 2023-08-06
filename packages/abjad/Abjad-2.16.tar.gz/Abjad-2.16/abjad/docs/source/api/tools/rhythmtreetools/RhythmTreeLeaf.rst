rhythmtreetools.RhythmTreeLeaf
==============================

.. autoclass:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf

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
       subgraph cluster_rhythmtreetools {
           graph [label=rhythmtreetools];
           "rhythmtreetools.RhythmTreeLeaf" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>RhythmTreeLeaf</B>>,
               shape=box,
               style="filled, rounded"];
           "rhythmtreetools.RhythmTreeNode" [color=4,
               group=3,
               label=RhythmTreeNode,
               shape=oval,
               style=bold];
           "rhythmtreetools.RhythmTreeNode" -> "rhythmtreetools.RhythmTreeLeaf";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeNode" -> "rhythmtreetools.RhythmTreeNode";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.depth
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.depthwise_inventory
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.duration
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.graph_order
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.improper_parentage
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.is_pitched
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.name
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.parent
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.parentage_ratios
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.preprolated_duration
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.pretty_rtm_format
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.prolation
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.prolations
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.proper_parentage
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.root
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.rtm_format
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.start_offset
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.stop_offset
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__call__
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__copy__
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__deepcopy__
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__eq__
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__format__
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__graph__
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__hash__
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__ne__
      ~abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__repr__

Bases
-----

- :py:class:`rhythmtreetools.RhythmTreeNode <abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode>`

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.depth
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.duration
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.graph_order
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.parent
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.parentage_ratios
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.pretty_rtm_format
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.prolation
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.prolations
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.root
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.rtm_format
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.start_offset
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.stop_offset
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.is_pitched
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.name
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.preprolated_duration
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__call__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__copy__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__graph__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeLeaf.RhythmTreeLeaf.__repr__
   :noindex:
