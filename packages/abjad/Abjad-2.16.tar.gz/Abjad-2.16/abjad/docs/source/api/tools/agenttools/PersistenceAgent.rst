agenttools.PersistenceAgent
===========================

.. autoclass:: abjad.tools.agenttools.PersistenceAgent.PersistenceAgent

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
           "agenttools.PersistenceAgent" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>PersistenceAgent</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "agenttools.PersistenceAgent";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.as_ly
      ~abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.as_midi
      ~abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.as_module
      ~abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.as_pdf
      ~abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.as_png
      ~abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.client
      ~abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.__eq__
      ~abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.__format__
      ~abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.__hash__
      ~abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.__ne__
      ~abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.client
   :noindex:

Methods
-------

.. automethod:: abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.as_ly
   :noindex:

.. automethod:: abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.as_midi
   :noindex:

.. automethod:: abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.as_module
   :noindex:

.. automethod:: abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.as_pdf
   :noindex:

.. automethod:: abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.as_png
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.__eq__
   :noindex:

.. automethod:: abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.__format__
   :noindex:

.. automethod:: abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.__hash__
   :noindex:

.. automethod:: abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.__ne__
   :noindex:

.. automethod:: abjad.tools.agenttools.PersistenceAgent.PersistenceAgent.__repr__
   :noindex:
