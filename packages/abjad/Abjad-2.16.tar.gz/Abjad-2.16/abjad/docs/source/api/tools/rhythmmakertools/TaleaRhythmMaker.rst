rhythmmakertools.TaleaRhythmMaker
=================================

.. autoclass:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker

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
       subgraph cluster_rhythmmakertools {
           graph [label=rhythmmakertools];
           "rhythmmakertools.RhythmMaker" [color=3,
               group=2,
               label=RhythmMaker,
               shape=oval,
               style=bold];
           "rhythmmakertools.TaleaRhythmMaker" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>TaleaRhythmMaker</B>>,
               shape=box,
               style="filled, rounded"];
           "rhythmmakertools.RhythmMaker" -> "rhythmmakertools.TaleaRhythmMaker";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "rhythmmakertools.RhythmMaker";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.beam_specifier
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.burnish_specifier
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.duration_spelling_specifier
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.extra_counts_per_division
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.helper_functions
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.output_masks
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.rest_tied_notes
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.split_divisions_by_counts
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.talea
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.tie_specifier
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.tie_split_notes
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.tuplet_spelling_specifier
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.__call__
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.__copy__
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.__eq__
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.__format__
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.__hash__
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.__illustrate__
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.__ne__
      ~abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.__repr__

Bases
-----

- :py:class:`rhythmmakertools.RhythmMaker <abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker>`

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.beam_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.burnish_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.duration_spelling_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.extra_counts_per_division
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.helper_functions
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.output_masks
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.rest_tied_notes
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.split_divisions_by_counts
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.talea
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.tie_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.tie_split_notes
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.tuplet_spelling_specifier
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.__call__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.__copy__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.__illustrate__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TaleaRhythmMaker.TaleaRhythmMaker.__repr__
   :noindex:
