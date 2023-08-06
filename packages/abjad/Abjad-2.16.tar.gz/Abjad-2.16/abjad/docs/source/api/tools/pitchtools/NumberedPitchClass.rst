pitchtools.NumberedPitchClass
=============================

.. autoclass:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass

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
           "pitchtools.NumberedPitchClass" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>NumberedPitchClass</B>>,
               shape=box,
               style="filled, rounded"];
           "pitchtools.PitchClass" [color=3,
               group=2,
               label=PitchClass,
               shape=oval,
               style=bold];
           "pitchtools.PitchClass" -> "pitchtools.NumberedPitchClass";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "pitchtools.PitchClass";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.accidental
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.accidental_spelling
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.alteration_in_semitones
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.apply_accidental
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.diatonic_pitch_class_name
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.diatonic_pitch_class_number
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.invert
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.is_diatonic_pitch_class_name
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.is_diatonic_pitch_class_number
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.is_pitch_class_name
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.is_pitch_class_number
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.multiply
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.named_pitch_class
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.numbered_pitch_class
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.pitch_class_label
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.pitch_class_name
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.pitch_class_number
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.transpose
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__add__
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__copy__
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__eq__
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__float__
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__format__
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__ge__
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__gt__
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__hash__
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__int__
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__le__
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__lt__
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__ne__
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__neg__
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__repr__
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__str__
      ~abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__sub__

Bases
-----

- :py:class:`pitchtools.PitchClass <abjad.tools.pitchtools.PitchClass.PitchClass>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.accidental
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.accidental_spelling
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.alteration_in_semitones
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.diatonic_pitch_class_name
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.diatonic_pitch_class_number
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.named_pitch_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.numbered_pitch_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.pitch_class_label
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.pitch_class_name
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.pitch_class_number
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.apply_accidental
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.invert
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.multiply
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.transpose
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.is_diatonic_pitch_class_name
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.is_diatonic_pitch_class_number
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.is_pitch_class_name
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.is_pitch_class_number
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__add__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__copy__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__float__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__ge__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__gt__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__int__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__le__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__lt__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__neg__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__str__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClass.NumberedPitchClass.__sub__
   :noindex:
