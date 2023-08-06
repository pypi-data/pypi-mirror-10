rhythmmakertools.RhythmMaker
============================

.. autoclass:: abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker

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
           "rhythmmakertools.AccelerandoRhythmMaker" [color=3,
               group=2,
               label=AccelerandoRhythmMaker,
               shape=box];
           "rhythmmakertools.EvenDivisionRhythmMaker" [color=3,
               group=2,
               label=EvenDivisionRhythmMaker,
               shape=box];
           "rhythmmakertools.EvenRunRhythmMaker" [color=3,
               group=2,
               label=EvenRunRhythmMaker,
               shape=box];
           "rhythmmakertools.IncisedRhythmMaker" [color=3,
               group=2,
               label=IncisedRhythmMaker,
               shape=box];
           "rhythmmakertools.NoteRhythmMaker" [color=3,
               group=2,
               label=NoteRhythmMaker,
               shape=box];
           "rhythmmakertools.RhythmMaker" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>RhythmMaker</B>>,
               shape=oval,
               style="filled, rounded"];
           "rhythmmakertools.SkipRhythmMaker" [color=3,
               group=2,
               label=SkipRhythmMaker,
               shape=box];
           "rhythmmakertools.TaleaRhythmMaker" [color=3,
               group=2,
               label=TaleaRhythmMaker,
               shape=box];
           "rhythmmakertools.TupletRhythmMaker" [color=3,
               group=2,
               label=TupletRhythmMaker,
               shape=box];
           "rhythmmakertools.RhythmMaker" -> "rhythmmakertools.AccelerandoRhythmMaker";
           "rhythmmakertools.RhythmMaker" -> "rhythmmakertools.EvenDivisionRhythmMaker";
           "rhythmmakertools.RhythmMaker" -> "rhythmmakertools.EvenRunRhythmMaker";
           "rhythmmakertools.RhythmMaker" -> "rhythmmakertools.IncisedRhythmMaker";
           "rhythmmakertools.RhythmMaker" -> "rhythmmakertools.NoteRhythmMaker";
           "rhythmmakertools.RhythmMaker" -> "rhythmmakertools.SkipRhythmMaker";
           "rhythmmakertools.RhythmMaker" -> "rhythmmakertools.TaleaRhythmMaker";
           "rhythmmakertools.RhythmMaker" -> "rhythmmakertools.TupletRhythmMaker";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "rhythmmakertools.RhythmMaker";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.beam_specifier
      ~abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.duration_spelling_specifier
      ~abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.output_masks
      ~abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.tie_specifier
      ~abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.tuplet_spelling_specifier
      ~abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.__call__
      ~abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.__copy__
      ~abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.__eq__
      ~abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.__format__
      ~abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.__hash__
      ~abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.__illustrate__
      ~abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.__ne__
      ~abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.__repr__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.beam_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.duration_spelling_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.output_masks
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.tie_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.tuplet_spelling_specifier
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.__call__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.__copy__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.__illustrate__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker.__repr__
   :noindex:
