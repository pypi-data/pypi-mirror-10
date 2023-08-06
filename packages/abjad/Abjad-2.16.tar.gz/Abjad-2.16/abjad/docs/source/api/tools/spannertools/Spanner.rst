spannertools.Spanner
====================

.. autoclass:: abjad.tools.spannertools.Spanner.Spanner

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
       subgraph cluster_spannertools {
           graph [label=spannertools];
           "spannertools.Beam" [color=3,
               group=2,
               label=Beam,
               shape=box];
           "spannertools.BowContactSpanner" [color=3,
               group=2,
               label=BowContactSpanner,
               shape=box];
           "spannertools.ComplexBeam" [color=3,
               group=2,
               label=ComplexBeam,
               shape=box];
           "spannertools.ComplexTrillSpanner" [color=3,
               group=2,
               label=ComplexTrillSpanner,
               shape=box];
           "spannertools.Crescendo" [color=3,
               group=2,
               label=Crescendo,
               shape=box];
           "spannertools.Decrescendo" [color=3,
               group=2,
               label=Decrescendo,
               shape=box];
           "spannertools.DuratedComplexBeam" [color=3,
               group=2,
               label=DuratedComplexBeam,
               shape=box];
           "spannertools.GeneralizedBeam" [color=3,
               group=2,
               label=GeneralizedBeam,
               shape=box];
           "spannertools.Glissando" [color=3,
               group=2,
               label=Glissando,
               shape=box];
           "spannertools.Hairpin" [color=3,
               group=2,
               label=Hairpin,
               shape=box];
           "spannertools.HiddenStaffSpanner" [color=3,
               group=2,
               label=HiddenStaffSpanner,
               shape=box];
           "spannertools.HorizontalBracketSpanner" [color=3,
               group=2,
               label=HorizontalBracketSpanner,
               shape=box];
           "spannertools.MeasuredComplexBeam" [color=3,
               group=2,
               label=MeasuredComplexBeam,
               shape=box];
           "spannertools.MultipartBeam" [color=3,
               group=2,
               label=MultipartBeam,
               shape=box];
           "spannertools.OctavationSpanner" [color=3,
               group=2,
               label=OctavationSpanner,
               shape=box];
           "spannertools.PhrasingSlur" [color=3,
               group=2,
               label=PhrasingSlur,
               shape=box];
           "spannertools.PianoPedalSpanner" [color=3,
               group=2,
               label=PianoPedalSpanner,
               shape=box];
           "spannertools.Slur" [color=3,
               group=2,
               label=Slur,
               shape=box];
           "spannertools.Spanner" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Spanner</B>>,
               shape=box,
               style="filled, rounded"];
           "spannertools.StaffLinesSpanner" [color=3,
               group=2,
               label=StaffLinesSpanner,
               shape=box];
           "spannertools.StemTremoloSpanner" [color=3,
               group=2,
               label=StemTremoloSpanner,
               shape=box];
           "spannertools.TempoSpanner" [color=3,
               group=2,
               label=TempoSpanner,
               shape=box];
           "spannertools.TextSpanner" [color=3,
               group=2,
               label=TextSpanner,
               shape=box];
           "spannertools.Tie" [color=3,
               group=2,
               label=Tie,
               shape=box];
           "spannertools.TrillSpanner" [color=3,
               group=2,
               label=TrillSpanner,
               shape=box];
           "spannertools.Beam" -> "spannertools.ComplexBeam";
           "spannertools.Beam" -> "spannertools.MultipartBeam";
           "spannertools.ComplexBeam" -> "spannertools.DuratedComplexBeam";
           "spannertools.ComplexBeam" -> "spannertools.MeasuredComplexBeam";
           "spannertools.Hairpin" -> "spannertools.Crescendo";
           "spannertools.Hairpin" -> "spannertools.Decrescendo";
           "spannertools.Spanner" -> "spannertools.Beam";
           "spannertools.Spanner" -> "spannertools.BowContactSpanner";
           "spannertools.Spanner" -> "spannertools.ComplexTrillSpanner";
           "spannertools.Spanner" -> "spannertools.GeneralizedBeam";
           "spannertools.Spanner" -> "spannertools.Glissando";
           "spannertools.Spanner" -> "spannertools.Hairpin";
           "spannertools.Spanner" -> "spannertools.HiddenStaffSpanner";
           "spannertools.Spanner" -> "spannertools.HorizontalBracketSpanner";
           "spannertools.Spanner" -> "spannertools.OctavationSpanner";
           "spannertools.Spanner" -> "spannertools.PhrasingSlur";
           "spannertools.Spanner" -> "spannertools.PianoPedalSpanner";
           "spannertools.Spanner" -> "spannertools.Slur";
           "spannertools.Spanner" -> "spannertools.StaffLinesSpanner";
           "spannertools.Spanner" -> "spannertools.StemTremoloSpanner";
           "spannertools.Spanner" -> "spannertools.TempoSpanner";
           "spannertools.Spanner" -> "spannertools.TextSpanner";
           "spannertools.Spanner" -> "spannertools.Tie";
           "spannertools.Spanner" -> "spannertools.TrillSpanner";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "spannertools.Spanner";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.spannertools.Spanner.Spanner.components
      ~abjad.tools.spannertools.Spanner.Spanner.name
      ~abjad.tools.spannertools.Spanner.Spanner.overrides
      ~abjad.tools.spannertools.Spanner.Spanner.__contains__
      ~abjad.tools.spannertools.Spanner.Spanner.__copy__
      ~abjad.tools.spannertools.Spanner.Spanner.__eq__
      ~abjad.tools.spannertools.Spanner.Spanner.__format__
      ~abjad.tools.spannertools.Spanner.Spanner.__getitem__
      ~abjad.tools.spannertools.Spanner.Spanner.__hash__
      ~abjad.tools.spannertools.Spanner.Spanner.__len__
      ~abjad.tools.spannertools.Spanner.Spanner.__lt__
      ~abjad.tools.spannertools.Spanner.Spanner.__ne__
      ~abjad.tools.spannertools.Spanner.Spanner.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.spannertools.Spanner.Spanner.components
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Spanner.Spanner.name
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Spanner.Spanner.overrides
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.spannertools.Spanner.Spanner.__contains__
   :noindex:

.. automethod:: abjad.tools.spannertools.Spanner.Spanner.__copy__
   :noindex:

.. automethod:: abjad.tools.spannertools.Spanner.Spanner.__eq__
   :noindex:

.. automethod:: abjad.tools.spannertools.Spanner.Spanner.__format__
   :noindex:

.. automethod:: abjad.tools.spannertools.Spanner.Spanner.__getitem__
   :noindex:

.. automethod:: abjad.tools.spannertools.Spanner.Spanner.__hash__
   :noindex:

.. automethod:: abjad.tools.spannertools.Spanner.Spanner.__len__
   :noindex:

.. automethod:: abjad.tools.spannertools.Spanner.Spanner.__lt__
   :noindex:

.. automethod:: abjad.tools.spannertools.Spanner.Spanner.__ne__
   :noindex:

.. automethod:: abjad.tools.spannertools.Spanner.Spanner.__repr__
   :noindex:
