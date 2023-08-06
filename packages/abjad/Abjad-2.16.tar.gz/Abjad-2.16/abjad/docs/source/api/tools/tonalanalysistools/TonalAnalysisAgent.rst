tonalanalysistools.TonalAnalysisAgent
=====================================

.. autoclass:: abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent

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
       subgraph cluster_tonalanalysistools {
           graph [label=tonalanalysistools];
           "tonalanalysistools.TonalAnalysisAgent" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>TonalAnalysisAgent</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "tonalanalysistools.TonalAnalysisAgent";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.analyze_chords
      ~abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.analyze_incomplete_chords
      ~abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.analyze_incomplete_tonal_functions
      ~abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.analyze_neighbor_notes
      ~abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.analyze_passing_tones
      ~abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.analyze_tonal_functions
      ~abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.are_scalar_notes
      ~abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.are_stepwise_ascending_notes
      ~abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.are_stepwise_descending_notes
      ~abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.are_stepwise_notes
      ~abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.client
      ~abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.__eq__
      ~abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.__format__
      ~abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.__hash__
      ~abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.__ne__
      ~abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.client
   :noindex:

Methods
-------

.. automethod:: abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.analyze_chords
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.analyze_incomplete_chords
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.analyze_incomplete_tonal_functions
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.analyze_neighbor_notes
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.analyze_passing_tones
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.analyze_tonal_functions
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.are_scalar_notes
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.are_stepwise_ascending_notes
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.are_stepwise_descending_notes
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.are_stepwise_notes
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.__eq__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.__format__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.__hash__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.__ne__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.TonalAnalysisAgent.TonalAnalysisAgent.__repr__
   :noindex:
