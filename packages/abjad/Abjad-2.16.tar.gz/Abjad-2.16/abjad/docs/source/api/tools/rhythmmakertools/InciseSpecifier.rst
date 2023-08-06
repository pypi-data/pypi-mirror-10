rhythmmakertools.InciseSpecifier
================================

.. autoclass:: abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier

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
           "rhythmmakertools.InciseSpecifier" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>InciseSpecifier</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "rhythmmakertools.InciseSpecifier";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.body_ratio
      ~abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.fill_with_notes
      ~abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.outer_divisions_only
      ~abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.prefix_counts
      ~abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.prefix_talea
      ~abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.suffix_counts
      ~abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.suffix_talea
      ~abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.talea_denominator
      ~abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.__copy__
      ~abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.__eq__
      ~abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.__format__
      ~abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.__hash__
      ~abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.__ne__
      ~abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.__repr__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.body_ratio
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.fill_with_notes
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.outer_divisions_only
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.prefix_counts
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.prefix_talea
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.suffix_counts
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.suffix_talea
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.talea_denominator
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.__copy__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.InciseSpecifier.InciseSpecifier.__repr__
   :noindex:
