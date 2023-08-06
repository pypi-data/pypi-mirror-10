pitchtools.NamedIntervalClass
=============================

.. autoclass:: abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass

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
           "pitchtools.IntervalClass" [color=3,
               group=2,
               label=IntervalClass,
               shape=oval,
               style=bold];
           "pitchtools.NamedIntervalClass" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>NamedIntervalClass</B>>,
               shape=box,
               style="filled, rounded"];
           "pitchtools.NamedInversionEquivalentIntervalClass" [color=3,
               group=2,
               label=NamedInversionEquivalentIntervalClass,
               shape=box];
           "pitchtools.IntervalClass" -> "pitchtools.NamedIntervalClass";
           "pitchtools.NamedIntervalClass" -> "pitchtools.NamedInversionEquivalentIntervalClass";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "pitchtools.IntervalClass";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.direction_number
      ~abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.direction_string
      ~abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.direction_symbol
      ~abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.from_pitch_carriers
      ~abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.number
      ~abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.quality_string
      ~abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__abs__
      ~abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__eq__
      ~abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__float__
      ~abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__format__
      ~abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__hash__
      ~abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__int__
      ~abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__lt__
      ~abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__ne__
      ~abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__repr__
      ~abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__str__

Bases
-----

- :py:class:`pitchtools.IntervalClass <abjad.tools.pitchtools.IntervalClass.IntervalClass>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.direction_number
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.direction_string
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.direction_symbol
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.number
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.quality_string
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.from_pitch_carriers
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__abs__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__float__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__int__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__lt__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.NamedIntervalClass.NamedIntervalClass.__str__
   :noindex:
