quantizationtools.QGridLeaf
===========================

.. autoclass:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf

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
           "quantizationtools.QGridLeaf" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>QGridLeaf</B>>,
               shape=box,
               style="filled, rounded"];
       }
       subgraph cluster_rhythmtreetools {
           graph [label=rhythmtreetools];
           "rhythmtreetools.RhythmTreeNode" [color=5,
               group=4,
               label=RhythmTreeNode,
               shape=oval,
               style=bold];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TreeNode";
       "datastructuretools.TreeNode" -> "rhythmtreetools.RhythmTreeNode";
       "rhythmtreetools.RhythmTreeNode" -> "quantizationtools.QGridLeaf";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.depth
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.depthwise_inventory
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.duration
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.graph_order
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.improper_parentage
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.is_divisible
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.name
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.parent
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.parentage_ratios
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.preceding_q_event_proxies
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.preprolated_duration
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.pretty_rtm_format
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.prolation
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.prolations
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.proper_parentage
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.q_event_proxies
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.root
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.rtm_format
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.start_offset
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.stop_offset
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.succeeding_q_event_proxies
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__call__
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__copy__
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__deepcopy__
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__eq__
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__format__
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__graph__
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__hash__
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__ne__
      ~abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__repr__

Bases
-----

- :py:class:`rhythmtreetools.RhythmTreeNode <abjad.tools.rhythmtreetools.RhythmTreeNode.RhythmTreeNode>`

- :py:class:`datastructuretools.TreeNode <abjad.tools.datastructuretools.TreeNode.TreeNode>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.depth
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.depthwise_inventory
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.duration
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.graph_order
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.parent
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.parentage_ratios
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.preceding_q_event_proxies
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.pretty_rtm_format
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.prolation
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.prolations
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.q_event_proxies
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.root
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.rtm_format
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.start_offset
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.stop_offset
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.succeeding_q_event_proxies
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.is_divisible
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.name
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.preprolated_duration
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__copy__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__graph__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QGridLeaf.QGridLeaf.__repr__
   :noindex:
