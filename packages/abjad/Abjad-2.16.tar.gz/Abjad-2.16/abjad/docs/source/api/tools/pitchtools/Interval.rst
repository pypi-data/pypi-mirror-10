pitchtools.Interval
===================

.. autoclass:: abjad.tools.pitchtools.Interval.Interval

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
           "pitchtools.Interval" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Interval</B>>,
               shape=oval,
               style="filled, rounded"];
           "pitchtools.NamedInterval" [color=3,
               group=2,
               label=NamedInterval,
               shape=box];
           "pitchtools.NumberedInterval" [color=3,
               group=2,
               label=NumberedInterval,
               shape=box];
           "pitchtools.Interval" -> "pitchtools.NamedInterval";
           "pitchtools.Interval" -> "pitchtools.NumberedInterval";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "pitchtools.Interval";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.Interval.Interval.cents
      ~abjad.tools.pitchtools.Interval.Interval.is_named_interval_abbreviation
      ~abjad.tools.pitchtools.Interval.Interval.is_named_interval_quality_abbreviation
      ~abjad.tools.pitchtools.Interval.Interval.__abs__
      ~abjad.tools.pitchtools.Interval.Interval.__eq__
      ~abjad.tools.pitchtools.Interval.Interval.__float__
      ~abjad.tools.pitchtools.Interval.Interval.__format__
      ~abjad.tools.pitchtools.Interval.Interval.__hash__
      ~abjad.tools.pitchtools.Interval.Interval.__int__
      ~abjad.tools.pitchtools.Interval.Interval.__ne__
      ~abjad.tools.pitchtools.Interval.Interval.__neg__
      ~abjad.tools.pitchtools.Interval.Interval.__repr__
      ~abjad.tools.pitchtools.Interval.Interval.__str__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.Interval.Interval.cents
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.pitchtools.Interval.Interval.is_named_interval_abbreviation
   :noindex:

.. automethod:: abjad.tools.pitchtools.Interval.Interval.is_named_interval_quality_abbreviation
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.Interval.Interval.__abs__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Interval.Interval.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Interval.Interval.__float__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Interval.Interval.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Interval.Interval.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Interval.Interval.__int__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Interval.Interval.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Interval.Interval.__neg__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Interval.Interval.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Interval.Interval.__str__
   :noindex:
