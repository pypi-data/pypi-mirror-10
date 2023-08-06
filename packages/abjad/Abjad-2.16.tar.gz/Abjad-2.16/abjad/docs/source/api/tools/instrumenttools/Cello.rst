instrumenttools.Cello
=====================

.. autoclass:: abjad.tools.instrumenttools.Cello.Cello

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
           "instrumenttools.Cello" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Cello</B>>,
               shape=box,
               style="filled, rounded"];
           "instrumenttools.Instrument" [color=3,
               group=2,
               label=Instrument,
               shape=box];
           "instrumenttools.Instrument" -> "instrumenttools.Cello";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "instrumenttools.Instrument";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.instrumenttools.Cello.Cello.allowable_clefs
      ~abjad.tools.instrumenttools.Cello.Cello.default_tuning
      ~abjad.tools.instrumenttools.Cello.Cello.instrument_name
      ~abjad.tools.instrumenttools.Cello.Cello.instrument_name_markup
      ~abjad.tools.instrumenttools.Cello.Cello.pitch_range
      ~abjad.tools.instrumenttools.Cello.Cello.short_instrument_name
      ~abjad.tools.instrumenttools.Cello.Cello.short_instrument_name_markup
      ~abjad.tools.instrumenttools.Cello.Cello.sounding_pitch_of_written_middle_c
      ~abjad.tools.instrumenttools.Cello.Cello.transpose_from_sounding_pitch_to_written_pitch
      ~abjad.tools.instrumenttools.Cello.Cello.transpose_from_written_pitch_to_sounding_pitch
      ~abjad.tools.instrumenttools.Cello.Cello.__copy__
      ~abjad.tools.instrumenttools.Cello.Cello.__eq__
      ~abjad.tools.instrumenttools.Cello.Cello.__format__
      ~abjad.tools.instrumenttools.Cello.Cello.__hash__
      ~abjad.tools.instrumenttools.Cello.Cello.__ne__
      ~abjad.tools.instrumenttools.Cello.Cello.__repr__

Bases
-----

- :py:class:`instrumenttools.Instrument <abjad.tools.instrumenttools.Instrument.Instrument>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.instrumenttools.Cello.Cello.allowable_clefs
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Cello.Cello.default_tuning
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Cello.Cello.instrument_name
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Cello.Cello.instrument_name_markup
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Cello.Cello.pitch_range
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Cello.Cello.short_instrument_name
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Cello.Cello.short_instrument_name_markup
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Cello.Cello.sounding_pitch_of_written_middle_c
   :noindex:

Methods
-------

.. automethod:: abjad.tools.instrumenttools.Cello.Cello.transpose_from_sounding_pitch_to_written_pitch
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Cello.Cello.transpose_from_written_pitch_to_sounding_pitch
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.instrumenttools.Cello.Cello.__copy__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Cello.Cello.__eq__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Cello.Cello.__format__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Cello.Cello.__hash__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Cello.Cello.__ne__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Cello.Cello.__repr__
   :noindex:
