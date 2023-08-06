rhythmmakertools.IncisedRhythmMaker
===================================

.. autoclass:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker

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
           "rhythmmakertools.IncisedRhythmMaker" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>IncisedRhythmMaker</B>>,
               shape=box,
               style="filled, rounded"];
           "rhythmmakertools.RhythmMaker" [color=3,
               group=2,
               label=RhythmMaker,
               shape=oval,
               style=bold];
           "rhythmmakertools.RhythmMaker" -> "rhythmmakertools.IncisedRhythmMaker";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "rhythmmakertools.RhythmMaker";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.beam_specifier
      ~abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.duration_spelling_specifier
      ~abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.extra_counts_per_division
      ~abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.helper_functions
      ~abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.incise_specifier
      ~abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.output_masks
      ~abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.split_divisions_by_counts
      ~abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.tie_specifier
      ~abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.tuplet_spelling_specifier
      ~abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.__call__
      ~abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.__copy__
      ~abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.__eq__
      ~abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.__format__
      ~abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.__hash__
      ~abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.__illustrate__
      ~abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.__ne__
      ~abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.__repr__

Bases
-----

- :py:class:`rhythmmakertools.RhythmMaker <abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker>`

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.beam_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.duration_spelling_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.extra_counts_per_division
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.helper_functions
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.incise_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.output_masks
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.split_divisions_by_counts
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.tie_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.tuplet_spelling_specifier
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.__call__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.__copy__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.__illustrate__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.IncisedRhythmMaker.IncisedRhythmMaker.__repr__
   :noindex:
