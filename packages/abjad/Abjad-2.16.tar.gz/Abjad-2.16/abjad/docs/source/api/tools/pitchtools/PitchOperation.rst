pitchtools.PitchOperation
=========================

.. autoclass:: abjad.tools.pitchtools.PitchOperation.PitchOperation

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
           "abctools.AbjadValueObject" [color=2,
               group=1,
               label=AbjadValueObject,
               shape=box];
           "abctools.AbjadObject" -> "abctools.AbjadValueObject";
           "abctools.AbjadObject.AbstractBase" -> "abctools.AbjadObject";
       }
       subgraph cluster_pitchtools {
           graph [label=pitchtools];
           "pitchtools.PitchOperation" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>PitchOperation</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "pitchtools.PitchOperation";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.PitchOperation.PitchOperation.duplicate
      ~abjad.tools.pitchtools.PitchOperation.PitchOperation.invert
      ~abjad.tools.pitchtools.PitchOperation.PitchOperation.multiply
      ~abjad.tools.pitchtools.PitchOperation.PitchOperation.operators
      ~abjad.tools.pitchtools.PitchOperation.PitchOperation.retrograde
      ~abjad.tools.pitchtools.PitchOperation.PitchOperation.rotate
      ~abjad.tools.pitchtools.PitchOperation.PitchOperation.transpose
      ~abjad.tools.pitchtools.PitchOperation.PitchOperation.__call__
      ~abjad.tools.pitchtools.PitchOperation.PitchOperation.__copy__
      ~abjad.tools.pitchtools.PitchOperation.PitchOperation.__eq__
      ~abjad.tools.pitchtools.PitchOperation.PitchOperation.__format__
      ~abjad.tools.pitchtools.PitchOperation.PitchOperation.__hash__
      ~abjad.tools.pitchtools.PitchOperation.PitchOperation.__ne__
      ~abjad.tools.pitchtools.PitchOperation.PitchOperation.__repr__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.PitchOperation.PitchOperation.operators
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.PitchOperation.PitchOperation.duplicate
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchOperation.PitchOperation.invert
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchOperation.PitchOperation.multiply
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchOperation.PitchOperation.retrograde
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchOperation.PitchOperation.rotate
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchOperation.PitchOperation.transpose
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.PitchOperation.PitchOperation.__call__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchOperation.PitchOperation.__copy__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchOperation.PitchOperation.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchOperation.PitchOperation.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchOperation.PitchOperation.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchOperation.PitchOperation.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchOperation.PitchOperation.__repr__
   :noindex:
