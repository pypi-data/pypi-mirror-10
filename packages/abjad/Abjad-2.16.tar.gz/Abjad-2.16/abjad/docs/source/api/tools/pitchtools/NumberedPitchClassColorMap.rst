pitchtools.NumberedPitchClassColorMap
=====================================

.. autoclass:: abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap

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
           "pitchtools.NumberedPitchClassColorMap" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>NumberedPitchClassColorMap</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "pitchtools.NumberedPitchClassColorMap";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.colors
      ~abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.get
      ~abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.is_twelve_tone_complete
      ~abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.is_twenty_four_tone_complete
      ~abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.pairs
      ~abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.pitch_iterables
      ~abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.__eq__
      ~abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.__format__
      ~abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.__getitem__
      ~abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.__hash__
      ~abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.__ne__
      ~abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.colors
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.is_twelve_tone_complete
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.is_twenty_four_tone_complete
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.pairs
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.pitch_iterables
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.get
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.__getitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NumberedPitchClassColorMap.NumberedPitchClassColorMap.__repr__
   :noindex:
