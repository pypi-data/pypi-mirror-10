pitchtools.PitchRange
=====================

.. autoclass:: abjad.tools.pitchtools.PitchRange.PitchRange

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
           "pitchtools.PitchRange" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>PitchRange</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "pitchtools.PitchRange";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.PitchRange.PitchRange.from_pitches
      ~abjad.tools.pitchtools.PitchRange.PitchRange.is_range_string
      ~abjad.tools.pitchtools.PitchRange.PitchRange.list_octave_transpositions
      ~abjad.tools.pitchtools.PitchRange.PitchRange.one_line_named_pitch_repr
      ~abjad.tools.pitchtools.PitchRange.PitchRange.one_line_numbered_pitch_repr
      ~abjad.tools.pitchtools.PitchRange.PitchRange.range_string
      ~abjad.tools.pitchtools.PitchRange.PitchRange.start_pitch
      ~abjad.tools.pitchtools.PitchRange.PitchRange.start_pitch_is_included_in_range
      ~abjad.tools.pitchtools.PitchRange.PitchRange.stop_pitch
      ~abjad.tools.pitchtools.PitchRange.PitchRange.stop_pitch_is_included_in_range
      ~abjad.tools.pitchtools.PitchRange.PitchRange.voice_pitch_class
      ~abjad.tools.pitchtools.PitchRange.PitchRange.__contains__
      ~abjad.tools.pitchtools.PitchRange.PitchRange.__eq__
      ~abjad.tools.pitchtools.PitchRange.PitchRange.__format__
      ~abjad.tools.pitchtools.PitchRange.PitchRange.__ge__
      ~abjad.tools.pitchtools.PitchRange.PitchRange.__gt__
      ~abjad.tools.pitchtools.PitchRange.PitchRange.__hash__
      ~abjad.tools.pitchtools.PitchRange.PitchRange.__illustrate__
      ~abjad.tools.pitchtools.PitchRange.PitchRange.__le__
      ~abjad.tools.pitchtools.PitchRange.PitchRange.__lt__
      ~abjad.tools.pitchtools.PitchRange.PitchRange.__ne__
      ~abjad.tools.pitchtools.PitchRange.PitchRange.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.PitchRange.PitchRange.one_line_named_pitch_repr
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchRange.PitchRange.one_line_numbered_pitch_repr
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchRange.PitchRange.range_string
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchRange.PitchRange.start_pitch
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchRange.PitchRange.start_pitch_is_included_in_range
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchRange.PitchRange.stop_pitch
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchRange.PitchRange.stop_pitch_is_included_in_range
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.PitchRange.PitchRange.list_octave_transpositions
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRange.PitchRange.voice_pitch_class
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.pitchtools.PitchRange.PitchRange.is_range_string
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.pitchtools.PitchRange.PitchRange.from_pitches
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.PitchRange.PitchRange.__contains__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRange.PitchRange.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRange.PitchRange.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRange.PitchRange.__ge__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRange.PitchRange.__gt__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRange.PitchRange.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRange.PitchRange.__illustrate__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRange.PitchRange.__le__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRange.PitchRange.__lt__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRange.PitchRange.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRange.PitchRange.__repr__
   :noindex:
