rhythmmakertools.NoteRhythmMaker
================================

.. autoclass:: abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker

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
           "rhythmmakertools.NoteRhythmMaker" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>NoteRhythmMaker</B>>,
               shape=box,
               style="filled, rounded"];
           "rhythmmakertools.RhythmMaker" [color=3,
               group=2,
               label=RhythmMaker,
               shape=oval,
               style=bold];
           "rhythmmakertools.RhythmMaker" -> "rhythmmakertools.NoteRhythmMaker";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "rhythmmakertools.RhythmMaker";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.beam_specifier
      ~abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.burnish_specifier
      ~abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.duration_spelling_specifier
      ~abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.output_masks
      ~abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.tie_specifier
      ~abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.tuplet_spelling_specifier
      ~abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.__call__
      ~abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.__copy__
      ~abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.__eq__
      ~abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.__format__
      ~abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.__hash__
      ~abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.__illustrate__
      ~abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.__ne__
      ~abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.__repr__

Bases
-----

- :py:class:`rhythmmakertools.RhythmMaker <abjad.tools.rhythmmakertools.RhythmMaker.RhythmMaker>`

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.beam_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.burnish_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.duration_spelling_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.output_masks
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.tie_specifier
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.tuplet_spelling_specifier
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.__call__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.__copy__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.__illustrate__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.NoteRhythmMaker.NoteRhythmMaker.__repr__
   :noindex:
