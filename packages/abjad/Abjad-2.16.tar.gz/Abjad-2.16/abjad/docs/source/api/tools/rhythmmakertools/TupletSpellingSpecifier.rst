rhythmmakertools.TupletSpellingSpecifier
========================================

.. autoclass:: abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier

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
           "rhythmmakertools.TupletSpellingSpecifier" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>TupletSpellingSpecifier</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "rhythmmakertools.TupletSpellingSpecifier";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.avoid_dots
      ~abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.flatten_trivial_tuplets
      ~abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.is_diminution
      ~abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.simplify_tuplets
      ~abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.use_note_duration_bracket
      ~abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.__copy__
      ~abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.__eq__
      ~abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.__format__
      ~abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.__hash__
      ~abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.__ne__
      ~abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.__repr__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.avoid_dots
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.flatten_trivial_tuplets
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.is_diminution
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.simplify_tuplets
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.use_note_duration_bracket
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.__copy__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.TupletSpellingSpecifier.TupletSpellingSpecifier.__repr__
   :noindex:
