pitchtools.Pitch
================

.. autoclass:: abjad.tools.pitchtools.Pitch.Pitch

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
       subgraph cluster_pitchtools {
           graph [label=pitchtools];
           "pitchtools.NamedPitch" [color=3,
               group=2,
               label=NamedPitch,
               shape=box];
           "pitchtools.NumberedPitch" [color=3,
               group=2,
               label=NumberedPitch,
               shape=box];
           "pitchtools.Pitch" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Pitch</B>>,
               shape=oval,
               style="filled, rounded"];
           "pitchtools.Pitch" -> "pitchtools.NamedPitch";
           "pitchtools.Pitch" -> "pitchtools.NumberedPitch";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "pitchtools.Pitch";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.Pitch.Pitch.accidental
      ~abjad.tools.pitchtools.Pitch.Pitch.accidental_spelling
      ~abjad.tools.pitchtools.Pitch.Pitch.alteration_in_semitones
      ~abjad.tools.pitchtools.Pitch.Pitch.apply_accidental
      ~abjad.tools.pitchtools.Pitch.Pitch.diatonic_pitch_class_name
      ~abjad.tools.pitchtools.Pitch.Pitch.diatonic_pitch_class_number
      ~abjad.tools.pitchtools.Pitch.Pitch.diatonic_pitch_name
      ~abjad.tools.pitchtools.Pitch.Pitch.diatonic_pitch_number
      ~abjad.tools.pitchtools.Pitch.Pitch.from_hertz
      ~abjad.tools.pitchtools.Pitch.Pitch.hertz
      ~abjad.tools.pitchtools.Pitch.Pitch.invert
      ~abjad.tools.pitchtools.Pitch.Pitch.is_diatonic_pitch_name
      ~abjad.tools.pitchtools.Pitch.Pitch.is_diatonic_pitch_number
      ~abjad.tools.pitchtools.Pitch.Pitch.is_pitch_carrier
      ~abjad.tools.pitchtools.Pitch.Pitch.is_pitch_class_octave_number_string
      ~abjad.tools.pitchtools.Pitch.Pitch.is_pitch_name
      ~abjad.tools.pitchtools.Pitch.Pitch.is_pitch_number
      ~abjad.tools.pitchtools.Pitch.Pitch.multiply
      ~abjad.tools.pitchtools.Pitch.Pitch.named_pitch
      ~abjad.tools.pitchtools.Pitch.Pitch.named_pitch_class
      ~abjad.tools.pitchtools.Pitch.Pitch.numbered_pitch
      ~abjad.tools.pitchtools.Pitch.Pitch.numbered_pitch_class
      ~abjad.tools.pitchtools.Pitch.Pitch.octave
      ~abjad.tools.pitchtools.Pitch.Pitch.octave_number
      ~abjad.tools.pitchtools.Pitch.Pitch.pitch_class_name
      ~abjad.tools.pitchtools.Pitch.Pitch.pitch_class_number
      ~abjad.tools.pitchtools.Pitch.Pitch.pitch_class_octave_label
      ~abjad.tools.pitchtools.Pitch.Pitch.pitch_name
      ~abjad.tools.pitchtools.Pitch.Pitch.pitch_number
      ~abjad.tools.pitchtools.Pitch.Pitch.transpose
      ~abjad.tools.pitchtools.Pitch.Pitch.__eq__
      ~abjad.tools.pitchtools.Pitch.Pitch.__float__
      ~abjad.tools.pitchtools.Pitch.Pitch.__format__
      ~abjad.tools.pitchtools.Pitch.Pitch.__hash__
      ~abjad.tools.pitchtools.Pitch.Pitch.__illustrate__
      ~abjad.tools.pitchtools.Pitch.Pitch.__int__
      ~abjad.tools.pitchtools.Pitch.Pitch.__ne__
      ~abjad.tools.pitchtools.Pitch.Pitch.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.accidental
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.accidental_spelling
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.alteration_in_semitones
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.diatonic_pitch_class_name
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.diatonic_pitch_class_number
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.diatonic_pitch_name
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.diatonic_pitch_number
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.hertz
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.named_pitch
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.named_pitch_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.numbered_pitch
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.numbered_pitch_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.octave
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.octave_number
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.pitch_class_name
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.pitch_class_number
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.pitch_class_octave_label
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.pitch_name
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Pitch.Pitch.pitch_number
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.apply_accidental
   :noindex:

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.invert
   :noindex:

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.multiply
   :noindex:

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.transpose
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.from_hertz
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.is_diatonic_pitch_name
   :noindex:

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.is_diatonic_pitch_number
   :noindex:

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.is_pitch_carrier
   :noindex:

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.is_pitch_class_octave_number_string
   :noindex:

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.is_pitch_name
   :noindex:

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.is_pitch_number
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.__float__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.__illustrate__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.__int__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Pitch.Pitch.__repr__
   :noindex:
