pitchtools.NamedPitch
=====================

.. autoclass:: abjad.tools.pitchtools.NamedPitch.NamedPitch

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
           "pitchtools.NamedPitch" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>NamedPitch</B>>,
               shape=box,
               style="filled, rounded"];
           "pitchtools.Pitch" [color=3,
               group=2,
               label=Pitch,
               shape=oval,
               style=bold];
           "pitchtools.Pitch" -> "pitchtools.NamedPitch";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "pitchtools.Pitch";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.accidental
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.accidental_spelling
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.alteration_in_semitones
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.apply_accidental
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.diatonic_pitch_class_name
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.diatonic_pitch_class_number
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.diatonic_pitch_name
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.diatonic_pitch_number
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.from_hertz
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.from_pitch_carrier
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.from_staff_position
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.hertz
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.invert
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.is_diatonic_pitch_name
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.is_diatonic_pitch_number
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.is_pitch_carrier
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.is_pitch_class_octave_number_string
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.is_pitch_name
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.is_pitch_number
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.multiply
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.named_pitch
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.named_pitch_class
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.numbered_pitch
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.numbered_pitch_class
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.octave
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.octave_number
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.pitch_class_name
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.pitch_class_number
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.pitch_class_octave_label
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.pitch_name
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.pitch_number
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.respell_with_flats
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.respell_with_sharps
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.to_staff_position
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.transpose
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.__add__
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.__copy__
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.__eq__
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.__float__
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.__format__
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.__ge__
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.__gt__
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.__hash__
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.__illustrate__
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.__int__
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.__le__
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.__lt__
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.__ne__
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.__repr__
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.__str__
      ~abjad.tools.pitchtools.NamedPitch.NamedPitch.__sub__

Bases
-----

- :py:class:`pitchtools.Pitch <abjad.tools.pitchtools.Pitch.Pitch>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.accidental
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.accidental_spelling
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.alteration_in_semitones
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.diatonic_pitch_class_name
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.diatonic_pitch_class_number
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.diatonic_pitch_name
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.diatonic_pitch_number
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.hertz
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.named_pitch
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.named_pitch_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.numbered_pitch
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.numbered_pitch_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.octave
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.octave_number
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.pitch_class_name
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.pitch_class_number
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.pitch_class_octave_label
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.pitch_name
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitch.NamedPitch.pitch_number
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.apply_accidental
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.invert
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.multiply
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.respell_with_flats
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.respell_with_sharps
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.to_staff_position
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.transpose
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.from_hertz
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.from_pitch_carrier
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.from_staff_position
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.is_diatonic_pitch_name
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.is_diatonic_pitch_number
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.is_pitch_carrier
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.is_pitch_class_octave_number_string
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.is_pitch_name
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.is_pitch_number
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.__add__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.__copy__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.__float__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.__ge__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.__gt__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.__illustrate__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.__int__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.__le__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.__lt__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.__str__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitch.NamedPitch.__sub__
   :noindex:
