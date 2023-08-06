rhythmmakertools.SilenceMask
============================

.. autoclass:: abjad.tools.rhythmmakertools.SilenceMask.SilenceMask

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
           "rhythmmakertools.BooleanPattern" [color=3,
               group=2,
               label=BooleanPattern,
               shape=box];
           "rhythmmakertools.SilenceMask" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>SilenceMask</B>>,
               shape=box,
               style="filled, rounded"];
           "rhythmmakertools.BooleanPattern" -> "rhythmmakertools.SilenceMask";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "rhythmmakertools.BooleanPattern";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.from_sequence
      ~abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.indices
      ~abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.invert
      ~abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.matches_index
      ~abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.payload
      ~abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.period
      ~abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.use_multimeasure_rests
      ~abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.__copy__
      ~abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.__eq__
      ~abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.__format__
      ~abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.__hash__
      ~abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.__ne__
      ~abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.__repr__

Bases
-----

- :py:class:`rhythmmakertools.BooleanPattern <abjad.tools.rhythmmakertools.BooleanPattern.BooleanPattern>`

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.indices
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.invert
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.payload
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.period
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.use_multimeasure_rests
   :noindex:

Methods
-------

.. automethod:: abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.matches_index
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.from_sequence
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.__copy__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.SilenceMask.SilenceMask.__repr__
   :noindex:
