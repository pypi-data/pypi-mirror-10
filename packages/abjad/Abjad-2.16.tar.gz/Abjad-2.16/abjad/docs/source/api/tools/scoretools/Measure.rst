scoretools.Measure
==================

.. autoclass:: abjad.tools.scoretools.Measure.Measure

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
       subgraph cluster_scoretools {
           graph [label=scoretools];
           "scoretools.Component" [color=3,
               group=2,
               label=Component,
               shape=oval,
               style=bold];
           "scoretools.Container" [color=3,
               group=2,
               label=Container,
               shape=box];
           "scoretools.FixedDurationContainer" [color=3,
               group=2,
               label=FixedDurationContainer,
               shape=box];
           "scoretools.Measure" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Measure</B>>,
               shape=box,
               style="filled, rounded"];
           "scoretools.Component" -> "scoretools.Container";
           "scoretools.Container" -> "scoretools.FixedDurationContainer";
           "scoretools.FixedDurationContainer" -> "scoretools.Measure";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "scoretools.Component";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.scoretools.Measure.Measure.always_format_time_signature
      ~abjad.tools.scoretools.Measure.Measure.append
      ~abjad.tools.scoretools.Measure.Measure.automatically_adjust_time_signature
      ~abjad.tools.scoretools.Measure.Measure.extend
      ~abjad.tools.scoretools.Measure.Measure.has_non_power_of_two_denominator
      ~abjad.tools.scoretools.Measure.Measure.has_power_of_two_denominator
      ~abjad.tools.scoretools.Measure.Measure.implicit_scaling
      ~abjad.tools.scoretools.Measure.Measure.implied_prolation
      ~abjad.tools.scoretools.Measure.Measure.index
      ~abjad.tools.scoretools.Measure.Measure.insert
      ~abjad.tools.scoretools.Measure.Measure.is_full
      ~abjad.tools.scoretools.Measure.Measure.is_misfilled
      ~abjad.tools.scoretools.Measure.Measure.is_overfull
      ~abjad.tools.scoretools.Measure.Measure.is_simultaneous
      ~abjad.tools.scoretools.Measure.Measure.is_underfull
      ~abjad.tools.scoretools.Measure.Measure.measure_number
      ~abjad.tools.scoretools.Measure.Measure.name
      ~abjad.tools.scoretools.Measure.Measure.pop
      ~abjad.tools.scoretools.Measure.Measure.remove
      ~abjad.tools.scoretools.Measure.Measure.reverse
      ~abjad.tools.scoretools.Measure.Measure.scale_and_adjust_time_signature
      ~abjad.tools.scoretools.Measure.Measure.select_leaves
      ~abjad.tools.scoretools.Measure.Measure.target_duration
      ~abjad.tools.scoretools.Measure.Measure.time_signature
      ~abjad.tools.scoretools.Measure.Measure.__contains__
      ~abjad.tools.scoretools.Measure.Measure.__copy__
      ~abjad.tools.scoretools.Measure.Measure.__delitem__
      ~abjad.tools.scoretools.Measure.Measure.__eq__
      ~abjad.tools.scoretools.Measure.Measure.__format__
      ~abjad.tools.scoretools.Measure.Measure.__getitem__
      ~abjad.tools.scoretools.Measure.Measure.__graph__
      ~abjad.tools.scoretools.Measure.Measure.__hash__
      ~abjad.tools.scoretools.Measure.Measure.__illustrate__
      ~abjad.tools.scoretools.Measure.Measure.__len__
      ~abjad.tools.scoretools.Measure.Measure.__mul__
      ~abjad.tools.scoretools.Measure.Measure.__ne__
      ~abjad.tools.scoretools.Measure.Measure.__repr__
      ~abjad.tools.scoretools.Measure.Measure.__rmul__
      ~abjad.tools.scoretools.Measure.Measure.__setitem__

Bases
-----

- :py:class:`scoretools.FixedDurationContainer <abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer>`

- :py:class:`scoretools.Container <abjad.tools.scoretools.Container.Container>`

- :py:class:`scoretools.Component <abjad.tools.scoretools.Component.Component>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.scoretools.Measure.Measure.has_non_power_of_two_denominator
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Measure.Measure.has_power_of_two_denominator
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Measure.Measure.implied_prolation
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Measure.Measure.is_full
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Measure.Measure.is_misfilled
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Measure.Measure.is_overfull
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Measure.Measure.is_underfull
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Measure.Measure.measure_number
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Measure.Measure.target_duration
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Measure.Measure.time_signature
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.scoretools.Measure.Measure.always_format_time_signature
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Measure.Measure.automatically_adjust_time_signature
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Measure.Measure.implicit_scaling
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Measure.Measure.is_simultaneous
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Measure.Measure.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.scoretools.Measure.Measure.append
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.extend
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.index
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.insert
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.pop
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.remove
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.reverse
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.scale_and_adjust_time_signature
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.select_leaves
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.scoretools.Measure.Measure.__contains__
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.__copy__
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.__delitem__
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.__eq__
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.__format__
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.__getitem__
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.__graph__
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.__hash__
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.__illustrate__
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.__len__
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.__mul__
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.__ne__
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.__repr__
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.__rmul__
   :noindex:

.. automethod:: abjad.tools.scoretools.Measure.Measure.__setitem__
   :noindex:
