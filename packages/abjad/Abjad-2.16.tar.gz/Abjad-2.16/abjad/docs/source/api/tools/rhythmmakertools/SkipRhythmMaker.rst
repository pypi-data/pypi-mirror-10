rhythmmakertools.SkipRhythmMaker
================================

.. autoclass:: abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker

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
           "rhythmmakertools.SkipRhythmMaker" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>SkipRhythmMaker</B>>,
               shape=box,
               style="filled, rounded"];
           "rhythmmakertools.RhythmMaker" -> "rhythmmakertools.SkipRhythmMaker";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "rhythmmakertools.RhythmMaker";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.beam_specifier
      ~abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.duration_spelling_specifier
      ~abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.output_masks
      ~abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.tie_specifier
      ~abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.tuplet_spelling_specifier
      ~abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.__call__
      ~abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.__copy__
      ~abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.__eq__
      ~abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.__format__
      ~abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.__hash__
      ~abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.__illustrate__
      ~abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.__ne__
      ~abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.__repr__

Bases
-----

- :py:class:`rhythmmakertools.RhythmMaker <abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker>`

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.beam_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.duration_spelling_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.output_masks
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.tie_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.tuplet_spelling_specifier
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.__call__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.__copy__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.__illustrate__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.SkipRhythmMaker.SkipRhythmMaker.__repr__
   :noindex:
