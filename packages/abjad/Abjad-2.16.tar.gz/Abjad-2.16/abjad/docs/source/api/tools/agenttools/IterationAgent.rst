agenttools.IterationAgent
=========================

.. autoclass:: abjad.tools.agenttools.IterationAgent.IterationAgent

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
       subgraph cluster_agenttools {
           graph [label=agenttools];
           "agenttools.IterationAgent" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>IterationAgent</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "agenttools.IterationAgent";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.agenttools.IterationAgent.IterationAgent.by_class
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.by_components_and_grace_containers
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.by_leaf_pair
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.by_logical_tie
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.by_logical_voice
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.by_logical_voice_from_component
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.by_run
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.by_semantic_voice
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.by_timeline
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.by_timeline_from_component
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.by_topmost_logical_ties_and_components
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.by_vertical_moment
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.client
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.depth_first
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.__eq__
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.__format__
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.__hash__
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.__ne__
      ~abjad.tools.agenttools.IterationAgent.IterationAgent.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.agenttools.IterationAgent.IterationAgent.client
   :noindex:

Methods
-------

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.by_class
   :noindex:

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.by_components_and_grace_containers
   :noindex:

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.by_leaf_pair
   :noindex:

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.by_logical_tie
   :noindex:

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.by_logical_voice
   :noindex:

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.by_logical_voice_from_component
   :noindex:

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.by_run
   :noindex:

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.by_semantic_voice
   :noindex:

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.by_timeline
   :noindex:

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.by_timeline_from_component
   :noindex:

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.by_topmost_logical_ties_and_components
   :noindex:

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.by_vertical_moment
   :noindex:

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.depth_first
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.__eq__
   :noindex:

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.__format__
   :noindex:

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.__hash__
   :noindex:

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.__ne__
   :noindex:

.. automethod:: abjad.tools.agenttools.IterationAgent.IterationAgent.__repr__
   :noindex:
