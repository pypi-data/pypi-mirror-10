handlertools.Handler
====================

.. autoclass:: abjad.tools.handlertools.Handler.Handler

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
           "abctools.AbjadValueObject" [color=2,
               group=1,
               label=AbjadValueObject,
               shape=box];
           "abctools.AbjadObject" -> "abctools.AbjadValueObject";
           "abctools.AbjadObject.AbstractBase" -> "abctools.AbjadObject";
       }
       subgraph cluster_handlertools {
           graph [label=handlertools];
           "handlertools.ArticulationHandler" [color=3,
               group=2,
               label=ArticulationHandler,
               shape=oval,
               style=bold];
           "handlertools.DiatonicClusterHandler" [color=3,
               group=2,
               label=DiatonicClusterHandler,
               shape=box];
           "handlertools.DynamicHandler" [color=3,
               group=2,
               label=DynamicHandler,
               shape=oval,
               style=bold];
           "handlertools.Handler" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Handler</B>>,
               shape=oval,
               style="filled, rounded"];
           "handlertools.NoteAndChordHairpinHandler" [color=3,
               group=2,
               label=NoteAndChordHairpinHandler,
               shape=box];
           "handlertools.NoteAndChordHairpinsHandler" [color=3,
               group=2,
               label=NoteAndChordHairpinsHandler,
               shape=box];
           "handlertools.OctaveTranspositionHandler" [color=3,
               group=2,
               label=OctaveTranspositionHandler,
               shape=box];
           "handlertools.OverrideHandler" [color=3,
               group=2,
               label=OverrideHandler,
               shape=box];
           "handlertools.PatternedArticulationsHandler" [color=3,
               group=2,
               label=PatternedArticulationsHandler,
               shape=box];
           "handlertools.ReiteratedArticulationHandler" [color=3,
               group=2,
               label=ReiteratedArticulationHandler,
               shape=box];
           "handlertools.ReiteratedDynamicHandler" [color=3,
               group=2,
               label=ReiteratedDynamicHandler,
               shape=box];
           "handlertools.RepeatedMarkupHandler" [color=3,
               group=2,
               label=RepeatedMarkupHandler,
               shape=box];
           "handlertools.RestTerminatedMantenimentiHandler" [color=3,
               group=2,
               label=RestTerminatedMantenimentiHandler,
               shape=box];
           "handlertools.StemTremoloHandler" [color=3,
               group=2,
               label=StemTremoloHandler,
               shape=box];
           "handlertools.TerracedDynamicsHandler" [color=3,
               group=2,
               label=TerracedDynamicsHandler,
               shape=box];
           "handlertools.TimewisePitchClassHandler" [color=3,
               group=2,
               label=TimewisePitchClassHandler,
               shape=box];
           "handlertools.TwoStageHairpinHandler" [color=3,
               group=2,
               label=TwoStageHairpinHandler,
               shape=box];
           "handlertools.ArticulationHandler" -> "handlertools.PatternedArticulationsHandler";
           "handlertools.ArticulationHandler" -> "handlertools.ReiteratedArticulationHandler";
           "handlertools.ArticulationHandler" -> "handlertools.RepeatedMarkupHandler";
           "handlertools.DynamicHandler" -> "handlertools.NoteAndChordHairpinHandler";
           "handlertools.DynamicHandler" -> "handlertools.NoteAndChordHairpinsHandler";
           "handlertools.DynamicHandler" -> "handlertools.ReiteratedDynamicHandler";
           "handlertools.DynamicHandler" -> "handlertools.RestTerminatedMantenimentiHandler";
           "handlertools.DynamicHandler" -> "handlertools.TerracedDynamicsHandler";
           "handlertools.DynamicHandler" -> "handlertools.TwoStageHairpinHandler";
           "handlertools.Handler" -> "handlertools.ArticulationHandler";
           "handlertools.Handler" -> "handlertools.DiatonicClusterHandler";
           "handlertools.Handler" -> "handlertools.DynamicHandler";
           "handlertools.Handler" -> "handlertools.OctaveTranspositionHandler";
           "handlertools.Handler" -> "handlertools.OverrideHandler";
           "handlertools.Handler" -> "handlertools.StemTremoloHandler";
           "handlertools.Handler" -> "handlertools.TimewisePitchClassHandler";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "handlertools.Handler";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.handlertools.Handler.Handler.__copy__
      ~abjad.tools.handlertools.Handler.Handler.__eq__
      ~abjad.tools.handlertools.Handler.Handler.__format__
      ~abjad.tools.handlertools.Handler.Handler.__hash__
      ~abjad.tools.handlertools.Handler.Handler.__ne__
      ~abjad.tools.handlertools.Handler.Handler.__repr__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.handlertools.Handler.Handler.__copy__
   :noindex:

.. automethod:: abjad.tools.handlertools.Handler.Handler.__eq__
   :noindex:

.. automethod:: abjad.tools.handlertools.Handler.Handler.__format__
   :noindex:

.. automethod:: abjad.tools.handlertools.Handler.Handler.__hash__
   :noindex:

.. automethod:: abjad.tools.handlertools.Handler.Handler.__ne__
   :noindex:

.. automethod:: abjad.tools.handlertools.Handler.Handler.__repr__
   :noindex:
