templatetools.GroupedRhythmicStavesScoreTemplate
================================================

.. autoclass:: abjad.tools.templatetools.GroupedRhythmicStavesScoreTemplate.GroupedRhythmicStavesScoreTemplate

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
       subgraph cluster_templatetools {
           graph [label=templatetools];
           "templatetools.GroupedRhythmicStavesScoreTemplate" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>GroupedRhythmicStavesScoreTemplate</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "templatetools.GroupedRhythmicStavesScoreTemplate";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.templatetools.GroupedRhythmicStavesScoreTemplate.GroupedRhythmicStavesScoreTemplate.staff_count
      ~abjad.tools.templatetools.GroupedRhythmicStavesScoreTemplate.GroupedRhythmicStavesScoreTemplate.with_clefs
      ~abjad.tools.templatetools.GroupedRhythmicStavesScoreTemplate.GroupedRhythmicStavesScoreTemplate.__call__
      ~abjad.tools.templatetools.GroupedRhythmicStavesScoreTemplate.GroupedRhythmicStavesScoreTemplate.__eq__
      ~abjad.tools.templatetools.GroupedRhythmicStavesScoreTemplate.GroupedRhythmicStavesScoreTemplate.__format__
      ~abjad.tools.templatetools.GroupedRhythmicStavesScoreTemplate.GroupedRhythmicStavesScoreTemplate.__hash__
      ~abjad.tools.templatetools.GroupedRhythmicStavesScoreTemplate.GroupedRhythmicStavesScoreTemplate.__ne__
      ~abjad.tools.templatetools.GroupedRhythmicStavesScoreTemplate.GroupedRhythmicStavesScoreTemplate.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.templatetools.GroupedRhythmicStavesScoreTemplate.GroupedRhythmicStavesScoreTemplate.staff_count
   :noindex:

.. autoattribute:: abjad.tools.templatetools.GroupedRhythmicStavesScoreTemplate.GroupedRhythmicStavesScoreTemplate.with_clefs
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.templatetools.GroupedRhythmicStavesScoreTemplate.GroupedRhythmicStavesScoreTemplate.__call__
   :noindex:

.. automethod:: abjad.tools.templatetools.GroupedRhythmicStavesScoreTemplate.GroupedRhythmicStavesScoreTemplate.__eq__
   :noindex:

.. automethod:: abjad.tools.templatetools.GroupedRhythmicStavesScoreTemplate.GroupedRhythmicStavesScoreTemplate.__format__
   :noindex:

.. automethod:: abjad.tools.templatetools.GroupedRhythmicStavesScoreTemplate.GroupedRhythmicStavesScoreTemplate.__hash__
   :noindex:

.. automethod:: abjad.tools.templatetools.GroupedRhythmicStavesScoreTemplate.GroupedRhythmicStavesScoreTemplate.__ne__
   :noindex:

.. automethod:: abjad.tools.templatetools.GroupedRhythmicStavesScoreTemplate.GroupedRhythmicStavesScoreTemplate.__repr__
   :noindex:
