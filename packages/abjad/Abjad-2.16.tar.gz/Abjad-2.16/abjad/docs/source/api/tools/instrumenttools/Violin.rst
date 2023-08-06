instrumenttools.Violin
======================

.. autoclass:: abjad.tools.instrumenttools.Violin.Violin

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
           "abctools.AbjadObject.AbstractBase" -> "abctools.AbjadObject";
       }
       subgraph cluster_instrumenttools {
           graph [label=instrumenttools];
           "instrumenttools.Instrument" [color=3,
               group=2,
               label=Instrument,
               shape=box];
           "instrumenttools.Violin" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Violin</B>>,
               shape=box,
               style="filled, rounded"];
           "instrumenttools.Instrument" -> "instrumenttools.Violin";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "instrumenttools.Instrument";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.instrumenttools.Violin.Violin.allowable_clefs
      ~abjad.tools.instrumenttools.Violin.Violin.default_tuning
      ~abjad.tools.instrumenttools.Violin.Violin.instrument_name
      ~abjad.tools.instrumenttools.Violin.Violin.instrument_name_markup
      ~abjad.tools.instrumenttools.Violin.Violin.pitch_range
      ~abjad.tools.instrumenttools.Violin.Violin.short_instrument_name
      ~abjad.tools.instrumenttools.Violin.Violin.short_instrument_name_markup
      ~abjad.tools.instrumenttools.Violin.Violin.sounding_pitch_of_written_middle_c
      ~abjad.tools.instrumenttools.Violin.Violin.transpose_from_sounding_pitch_to_written_pitch
      ~abjad.tools.instrumenttools.Violin.Violin.transpose_from_written_pitch_to_sounding_pitch
      ~abjad.tools.instrumenttools.Violin.Violin.__copy__
      ~abjad.tools.instrumenttools.Violin.Violin.__eq__
      ~abjad.tools.instrumenttools.Violin.Violin.__format__
      ~abjad.tools.instrumenttools.Violin.Violin.__hash__
      ~abjad.tools.instrumenttools.Violin.Violin.__ne__
      ~abjad.tools.instrumenttools.Violin.Violin.__repr__

Bases
-----

- :py:class:`instrumenttools.Instrument <abjad.tools.instrumenttools.Instrument.Instrument>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.instrumenttools.Violin.Violin.allowable_clefs
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Violin.Violin.default_tuning
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Violin.Violin.instrument_name
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Violin.Violin.instrument_name_markup
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Violin.Violin.pitch_range
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Violin.Violin.short_instrument_name
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Violin.Violin.short_instrument_name_markup
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Violin.Violin.sounding_pitch_of_written_middle_c
   :noindex:

Methods
-------

.. automethod:: abjad.tools.instrumenttools.Violin.Violin.transpose_from_sounding_pitch_to_written_pitch
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Violin.Violin.transpose_from_written_pitch_to_sounding_pitch
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.instrumenttools.Violin.Violin.__copy__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Violin.Violin.__eq__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Violin.Violin.__format__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Violin.Violin.__hash__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Violin.Violin.__ne__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Violin.Violin.__repr__
   :noindex:
