pitchtools.Octave
=================

.. autoclass:: abjad.tools.pitchtools.Octave.Octave

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
           "pitchtools.Octave" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Octave</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "pitchtools.Octave";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.Octave.Octave.from_pitch_name
      ~abjad.tools.pitchtools.Octave.Octave.from_pitch_number
      ~abjad.tools.pitchtools.Octave.Octave.is_octave_tick_string
      ~abjad.tools.pitchtools.Octave.Octave.octave_number
      ~abjad.tools.pitchtools.Octave.Octave.octave_tick_string
      ~abjad.tools.pitchtools.Octave.Octave.pitch_number
      ~abjad.tools.pitchtools.Octave.Octave.pitch_range
      ~abjad.tools.pitchtools.Octave.Octave.__eq__
      ~abjad.tools.pitchtools.Octave.Octave.__float__
      ~abjad.tools.pitchtools.Octave.Octave.__format__
      ~abjad.tools.pitchtools.Octave.Octave.__hash__
      ~abjad.tools.pitchtools.Octave.Octave.__int__
      ~abjad.tools.pitchtools.Octave.Octave.__ne__
      ~abjad.tools.pitchtools.Octave.Octave.__repr__
      ~abjad.tools.pitchtools.Octave.Octave.__str__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.Octave.Octave.octave_number
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Octave.Octave.octave_tick_string
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Octave.Octave.pitch_number
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Octave.Octave.pitch_range
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.pitchtools.Octave.Octave.from_pitch_name
   :noindex:

.. automethod:: abjad.tools.pitchtools.Octave.Octave.from_pitch_number
   :noindex:

.. automethod:: abjad.tools.pitchtools.Octave.Octave.is_octave_tick_string
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.Octave.Octave.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Octave.Octave.__float__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Octave.Octave.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Octave.Octave.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Octave.Octave.__int__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Octave.Octave.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Octave.Octave.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Octave.Octave.__str__
   :noindex:
