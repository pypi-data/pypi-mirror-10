systemtools.WellformednessManager
=================================

.. autoclass:: abjad.tools.systemtools.WellformednessManager.WellformednessManager

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
           "systemtools.WellformednessManager" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>WellformednessManager</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "systemtools.WellformednessManager";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_beamed_quarter_notes
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_conflicting_clefs
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_discontiguous_spanners
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_duplicate_ids
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_empty_containers
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_intermarked_hairpins
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_misdurated_measures
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_misfilled_measures
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_mispitched_ties
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_misrepresented_flags
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_missing_parents
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_nested_measures
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_overlapping_beams
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_overlapping_glissandi
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_overlapping_octavation_spanners
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_short_hairpins
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.__call__
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.__eq__
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.__format__
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.__hash__
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.__ne__
      ~abjad.tools.systemtools.WellformednessManager.WellformednessManager.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Methods
-------

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_beamed_quarter_notes
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_conflicting_clefs
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_discontiguous_spanners
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_duplicate_ids
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_empty_containers
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_intermarked_hairpins
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_misdurated_measures
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_misfilled_measures
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_mispitched_ties
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_misrepresented_flags
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_missing_parents
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_nested_measures
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_overlapping_beams
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_overlapping_glissandi
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_overlapping_octavation_spanners
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.check_short_hairpins
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.__call__
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.__eq__
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.__format__
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.__hash__
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.__ne__
   :noindex:

.. automethod:: abjad.tools.systemtools.WellformednessManager.WellformednessManager.__repr__
   :noindex:
