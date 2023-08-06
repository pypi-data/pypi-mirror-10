pitchtools.IntervalClass
========================

.. autoclass:: abjad.tools.pitchtools.IntervalClass.IntervalClass

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
           "pitchtools.IntervalClass" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>IntervalClass</B>>,
               shape=oval,
               style="filled, rounded"];
           "pitchtools.NamedIntervalClass" [color=3,
               group=2,
               label=NamedIntervalClass,
               shape=box];
           "pitchtools.NamedInversionEquivalentIntervalClass" [color=3,
               group=2,
               label=NamedInversionEquivalentIntervalClass,
               shape=box];
           "pitchtools.NumberedIntervalClass" [color=3,
               group=2,
               label=NumberedIntervalClass,
               shape=box];
           "pitchtools.NumberedInversionEquivalentIntervalClass" [color=3,
               group=2,
               label=NumberedInversionEquivalentIntervalClass,
               shape=box];
           "pitchtools.IntervalClass" -> "pitchtools.NamedIntervalClass";
           "pitchtools.IntervalClass" -> "pitchtools.NumberedIntervalClass";
           "pitchtools.NamedIntervalClass" -> "pitchtools.NamedInversionEquivalentIntervalClass";
           "pitchtools.NumberedIntervalClass" -> "pitchtools.NumberedInversionEquivalentIntervalClass";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "pitchtools.IntervalClass";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.IntervalClass.IntervalClass.number
      ~abjad.tools.pitchtools.IntervalClass.IntervalClass.__abs__
      ~abjad.tools.pitchtools.IntervalClass.IntervalClass.__eq__
      ~abjad.tools.pitchtools.IntervalClass.IntervalClass.__float__
      ~abjad.tools.pitchtools.IntervalClass.IntervalClass.__format__
      ~abjad.tools.pitchtools.IntervalClass.IntervalClass.__hash__
      ~abjad.tools.pitchtools.IntervalClass.IntervalClass.__int__
      ~abjad.tools.pitchtools.IntervalClass.IntervalClass.__ne__
      ~abjad.tools.pitchtools.IntervalClass.IntervalClass.__repr__
      ~abjad.tools.pitchtools.IntervalClass.IntervalClass.__str__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.IntervalClass.IntervalClass.number
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.IntervalClass.IntervalClass.__abs__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClass.IntervalClass.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClass.IntervalClass.__float__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClass.IntervalClass.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClass.IntervalClass.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClass.IntervalClass.__int__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClass.IntervalClass.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClass.IntervalClass.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClass.IntervalClass.__str__
   :noindex:
