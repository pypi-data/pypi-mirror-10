pitchtools.PitchClass
=====================

.. autoclass:: abjad.tools.pitchtools.PitchClass.PitchClass

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
           "pitchtools.NamedPitchClass" [color=3,
               group=2,
               label=NamedPitchClass,
               shape=box];
           "pitchtools.NumberedPitchClass" [color=3,
               group=2,
               label=NumberedPitchClass,
               shape=box];
           "pitchtools.PitchClass" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>PitchClass</B>>,
               shape=oval,
               style="filled, rounded"];
           "pitchtools.PitchClass" -> "pitchtools.NamedPitchClass";
           "pitchtools.PitchClass" -> "pitchtools.NumberedPitchClass";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "pitchtools.PitchClass";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.PitchClass.PitchClass.accidental
      ~abjad.tools.pitchtools.PitchClass.PitchClass.accidental_spelling
      ~abjad.tools.pitchtools.PitchClass.PitchClass.alteration_in_semitones
      ~abjad.tools.pitchtools.PitchClass.PitchClass.apply_accidental
      ~abjad.tools.pitchtools.PitchClass.PitchClass.diatonic_pitch_class_name
      ~abjad.tools.pitchtools.PitchClass.PitchClass.diatonic_pitch_class_number
      ~abjad.tools.pitchtools.PitchClass.PitchClass.invert
      ~abjad.tools.pitchtools.PitchClass.PitchClass.is_diatonic_pitch_class_name
      ~abjad.tools.pitchtools.PitchClass.PitchClass.is_diatonic_pitch_class_number
      ~abjad.tools.pitchtools.PitchClass.PitchClass.is_pitch_class_name
      ~abjad.tools.pitchtools.PitchClass.PitchClass.is_pitch_class_number
      ~abjad.tools.pitchtools.PitchClass.PitchClass.multiply
      ~abjad.tools.pitchtools.PitchClass.PitchClass.named_pitch_class
      ~abjad.tools.pitchtools.PitchClass.PitchClass.numbered_pitch_class
      ~abjad.tools.pitchtools.PitchClass.PitchClass.pitch_class_label
      ~abjad.tools.pitchtools.PitchClass.PitchClass.pitch_class_name
      ~abjad.tools.pitchtools.PitchClass.PitchClass.pitch_class_number
      ~abjad.tools.pitchtools.PitchClass.PitchClass.transpose
      ~abjad.tools.pitchtools.PitchClass.PitchClass.__eq__
      ~abjad.tools.pitchtools.PitchClass.PitchClass.__format__
      ~abjad.tools.pitchtools.PitchClass.PitchClass.__hash__
      ~abjad.tools.pitchtools.PitchClass.PitchClass.__ne__
      ~abjad.tools.pitchtools.PitchClass.PitchClass.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.PitchClass.PitchClass.accidental
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClass.PitchClass.accidental_spelling
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClass.PitchClass.alteration_in_semitones
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClass.PitchClass.diatonic_pitch_class_name
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClass.PitchClass.diatonic_pitch_class_number
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClass.PitchClass.named_pitch_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClass.PitchClass.numbered_pitch_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClass.PitchClass.pitch_class_label
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClass.PitchClass.pitch_class_name
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClass.PitchClass.pitch_class_number
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.PitchClass.PitchClass.apply_accidental
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClass.PitchClass.invert
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClass.PitchClass.multiply
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClass.PitchClass.transpose
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.pitchtools.PitchClass.PitchClass.is_diatonic_pitch_class_name
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClass.PitchClass.is_diatonic_pitch_class_number
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClass.PitchClass.is_pitch_class_name
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClass.PitchClass.is_pitch_class_number
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.PitchClass.PitchClass.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClass.PitchClass.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClass.PitchClass.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClass.PitchClass.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClass.PitchClass.__repr__
   :noindex:
