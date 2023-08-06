systemtools.BenchmarkScoreMaker
===============================

.. autoclass:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker

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
       subgraph cluster_systemtools {
           graph [label=systemtools];
           "systemtools.BenchmarkScoreMaker" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>BenchmarkScoreMaker</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "systemtools.BenchmarkScoreMaker";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_bound_hairpin_score_01
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_bound_hairpin_score_02
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_bound_hairpin_score_03
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_hairpin_score_01
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_hairpin_score_02
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_hairpin_score_03
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_score_00
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_score_with_indicators_01
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_score_with_indicators_02
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_score_with_indicators_03
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_01
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_02
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_03
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_04
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_05
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_06
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_07
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_08
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_09
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.__eq__
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.__format__
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.__hash__
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.__ne__
      ~abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Methods
-------

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_bound_hairpin_score_01
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_bound_hairpin_score_02
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_bound_hairpin_score_03
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_hairpin_score_01
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_hairpin_score_02
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_hairpin_score_03
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_score_00
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_score_with_indicators_01
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_score_with_indicators_02
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_score_with_indicators_03
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_01
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_02
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_03
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_04
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_05
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_06
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_07
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_08
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.make_spanner_score_09
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.__eq__
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.__format__
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.__hash__
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.__ne__
   :noindex:

.. automethod:: abjad.tools.systemtools.BenchmarkScoreMaker.BenchmarkScoreMaker.__repr__
   :noindex:
