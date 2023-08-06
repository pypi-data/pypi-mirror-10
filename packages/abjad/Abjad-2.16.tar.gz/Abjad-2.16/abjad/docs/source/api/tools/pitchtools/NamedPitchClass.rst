pitchtools.NamedPitchClass
==========================

.. autoclass:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass

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
           "pitchtools.NamedPitchClass" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>NamedPitchClass</B>>,
               shape=box,
               style="filled, rounded"];
           "pitchtools.PitchClass" [color=3,
               group=2,
               label=PitchClass,
               shape=oval,
               style=bold];
           "pitchtools.PitchClass" -> "pitchtools.NamedPitchClass";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "pitchtools.PitchClass";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.accidental
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.accidental_spelling
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.alteration_in_semitones
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.apply_accidental
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.diatonic_pitch_class_name
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.diatonic_pitch_class_number
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.invert
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.is_diatonic_pitch_class_name
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.is_diatonic_pitch_class_number
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.is_pitch_class_name
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.is_pitch_class_number
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.multiply
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.named_pitch_class
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.numbered_pitch_class
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.pitch_class_label
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.pitch_class_name
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.pitch_class_number
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.transpose
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__add__
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__copy__
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__eq__
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__float__
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__format__
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__hash__
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__int__
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__ne__
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__repr__
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__str__
      ~abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__sub__

Bases
-----

- :py:class:`pitchtools.PitchClass <abjad.tools.pitchtools.PitchClass.PitchClass>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.accidental
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.accidental_spelling
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.alteration_in_semitones
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.diatonic_pitch_class_name
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.diatonic_pitch_class_number
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.named_pitch_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.numbered_pitch_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.pitch_class_label
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.pitch_class_name
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.pitch_class_number
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.apply_accidental
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.invert
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.multiply
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.transpose
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.is_diatonic_pitch_class_name
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.is_diatonic_pitch_class_number
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.is_pitch_class_name
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.is_pitch_class_number
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__add__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__copy__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__float__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__int__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__str__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedPitchClass.NamedPitchClass.__sub__
   :noindex:
