rhythmmakertools.DurationSpellingSpecifier
==========================================

.. autoclass:: abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier

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
           "rhythmmakertools.DurationSpellingSpecifier" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>DurationSpellingSpecifier</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "rhythmmakertools.DurationSpellingSpecifier";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.decrease_durations_monotonically
      ~abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.forbid_meter_rewriting
      ~abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.forbidden_written_duration
      ~abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.rewrite_meter
      ~abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.spell_metrically
      ~abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.__copy__
      ~abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.__eq__
      ~abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.__format__
      ~abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.__hash__
      ~abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.__ne__
      ~abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.__repr__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.decrease_durations_monotonically
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.forbid_meter_rewriting
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.forbidden_written_duration
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.rewrite_meter
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.spell_metrically
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.__copy__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.DurationSpellingSpecifier.DurationSpellingSpecifier.__repr__
   :noindex:
