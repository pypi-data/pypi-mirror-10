agenttools.MutationAgent
========================

.. autoclass:: abjad.tools.agenttools.MutationAgent.MutationAgent

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
           "agenttools.MutationAgent" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>MutationAgent</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "agenttools.MutationAgent";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.agenttools.MutationAgent.MutationAgent.client
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.copy
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.extract
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.fuse
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.replace
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.replace_measure_contents
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.respell_with_flats
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.respell_with_sharps
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.rewrite_meter
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.scale
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.splice
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.split
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.swap
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.transpose
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.__eq__
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.__format__
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.__hash__
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.__ne__
      ~abjad.tools.agenttools.MutationAgent.MutationAgent.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.agenttools.MutationAgent.MutationAgent.client
   :noindex:

Methods
-------

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.copy
   :noindex:

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.extract
   :noindex:

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.fuse
   :noindex:

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.replace
   :noindex:

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.replace_measure_contents
   :noindex:

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.respell_with_flats
   :noindex:

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.respell_with_sharps
   :noindex:

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.rewrite_meter
   :noindex:

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.scale
   :noindex:

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.splice
   :noindex:

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.split
   :noindex:

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.swap
   :noindex:

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.transpose
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.__eq__
   :noindex:

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.__format__
   :noindex:

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.__hash__
   :noindex:

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.__ne__
   :noindex:

.. automethod:: abjad.tools.agenttools.MutationAgent.MutationAgent.__repr__
   :noindex:
