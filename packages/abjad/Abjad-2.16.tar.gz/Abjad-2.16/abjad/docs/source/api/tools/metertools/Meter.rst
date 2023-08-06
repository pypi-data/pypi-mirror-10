metertools.Meter
================

.. autoclass:: abjad.tools.metertools.Meter.Meter

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
       subgraph cluster_metertools {
           graph [label=metertools];
           "metertools.Meter" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Meter</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "metertools.Meter";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.metertools.Meter.Meter.decrease_durations_monotonically
      ~abjad.tools.metertools.Meter.Meter.denominator
      ~abjad.tools.metertools.Meter.Meter.depthwise_offset_inventory
      ~abjad.tools.metertools.Meter.Meter.duration
      ~abjad.tools.metertools.Meter.Meter.fit_meters_to_expr
      ~abjad.tools.metertools.Meter.Meter.generate_offset_kernel_to_denominator
      ~abjad.tools.metertools.Meter.Meter.implied_time_signature
      ~abjad.tools.metertools.Meter.Meter.is_compound
      ~abjad.tools.metertools.Meter.Meter.is_simple
      ~abjad.tools.metertools.Meter.Meter.numerator
      ~abjad.tools.metertools.Meter.Meter.preferred_boundary_depth
      ~abjad.tools.metertools.Meter.Meter.pretty_rtm_format
      ~abjad.tools.metertools.Meter.Meter.root_node
      ~abjad.tools.metertools.Meter.Meter.rtm_format
      ~abjad.tools.metertools.Meter.Meter.__eq__
      ~abjad.tools.metertools.Meter.Meter.__format__
      ~abjad.tools.metertools.Meter.Meter.__graph__
      ~abjad.tools.metertools.Meter.Meter.__hash__
      ~abjad.tools.metertools.Meter.Meter.__iter__
      ~abjad.tools.metertools.Meter.Meter.__ne__
      ~abjad.tools.metertools.Meter.Meter.__repr__
      ~abjad.tools.metertools.Meter.Meter.__str__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.metertools.Meter.Meter.decrease_durations_monotonically
   :noindex:

.. autoattribute:: abjad.tools.metertools.Meter.Meter.denominator
   :noindex:

.. autoattribute:: abjad.tools.metertools.Meter.Meter.depthwise_offset_inventory
   :noindex:

.. autoattribute:: abjad.tools.metertools.Meter.Meter.duration
   :noindex:

.. autoattribute:: abjad.tools.metertools.Meter.Meter.implied_time_signature
   :noindex:

.. autoattribute:: abjad.tools.metertools.Meter.Meter.is_compound
   :noindex:

.. autoattribute:: abjad.tools.metertools.Meter.Meter.is_simple
   :noindex:

.. autoattribute:: abjad.tools.metertools.Meter.Meter.numerator
   :noindex:

.. autoattribute:: abjad.tools.metertools.Meter.Meter.preferred_boundary_depth
   :noindex:

.. autoattribute:: abjad.tools.metertools.Meter.Meter.pretty_rtm_format
   :noindex:

.. autoattribute:: abjad.tools.metertools.Meter.Meter.root_node
   :noindex:

.. autoattribute:: abjad.tools.metertools.Meter.Meter.rtm_format
   :noindex:

Methods
-------

.. automethod:: abjad.tools.metertools.Meter.Meter.generate_offset_kernel_to_denominator
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.metertools.Meter.Meter.fit_meters_to_expr
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.metertools.Meter.Meter.__eq__
   :noindex:

.. automethod:: abjad.tools.metertools.Meter.Meter.__format__
   :noindex:

.. automethod:: abjad.tools.metertools.Meter.Meter.__graph__
   :noindex:

.. automethod:: abjad.tools.metertools.Meter.Meter.__hash__
   :noindex:

.. automethod:: abjad.tools.metertools.Meter.Meter.__iter__
   :noindex:

.. automethod:: abjad.tools.metertools.Meter.Meter.__ne__
   :noindex:

.. automethod:: abjad.tools.metertools.Meter.Meter.__repr__
   :noindex:

.. automethod:: abjad.tools.metertools.Meter.Meter.__str__
   :noindex:
