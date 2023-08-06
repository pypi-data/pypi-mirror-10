rhythmmakertools.TupletRhythmMaker
==================================

.. autoclass:: abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker

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
           "rhythmmakertools.TupletRhythmMaker" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>TupletRhythmMaker</B>>,
               shape=box,
               style="filled, rounded"];
           "rhythmmakertools.RhythmMaker" -> "rhythmmakertools.TupletRhythmMaker";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "rhythmmakertools.RhythmMaker";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.beam_specifier
      ~abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.duration_spelling_specifier
      ~abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.output_masks
      ~abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.preferred_denominator
      ~abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.tie_specifier
      ~abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.tuplet_ratios
      ~abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.tuplet_spelling_specifier
      ~abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.__call__
      ~abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.__copy__
      ~abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.__eq__
      ~abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.__format__
      ~abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.__hash__
      ~abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.__illustrate__
      ~abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.__ne__
      ~abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.__repr__

Bases
-----

- :py:class:`rhythmmakertools.RhythmMaker <abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker>`

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.beam_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.duration_spelling_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.output_masks
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.preferred_denominator
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.tie_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.tuplet_ratios
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.tuplet_spelling_specifier
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.__call__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.__copy__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.__illustrate__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TupletRhythmMaker.TupletRhythmMaker.__repr__
   :noindex:
