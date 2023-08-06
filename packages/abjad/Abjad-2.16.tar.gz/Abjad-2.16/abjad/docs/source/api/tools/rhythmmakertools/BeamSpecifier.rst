rhythmmakertools.BeamSpecifier
==============================

.. autoclass:: abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier

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
           "rhythmmakertools.BeamSpecifier" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>BeamSpecifier</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "rhythmmakertools.BeamSpecifier";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.beam_divisions_together
      ~abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.beam_each_division
      ~abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.use_feather_beams
      ~abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.__copy__
      ~abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.__eq__
      ~abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.__format__
      ~abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.__hash__
      ~abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.__ne__
      ~abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.__repr__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.beam_divisions_together
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.beam_each_division
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.use_feather_beams
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.__copy__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BeamSpecifier.BeamSpecifier.__repr__
   :noindex:
