indicatortools.MetricModulation
===============================

.. autoclass:: abjad.tools.indicatortools.MetricModulation.MetricModulation

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
       subgraph cluster_indicatortools {
           graph [label=indicatortools];
           "indicatortools.MetricModulation" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>MetricModulation</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "indicatortools.MetricModulation";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.indicatortools.MetricModulation.MetricModulation.left_markup
      ~abjad.tools.indicatortools.MetricModulation.MetricModulation.left_rhythm
      ~abjad.tools.indicatortools.MetricModulation.MetricModulation.ratio
      ~abjad.tools.indicatortools.MetricModulation.MetricModulation.right_markup
      ~abjad.tools.indicatortools.MetricModulation.MetricModulation.right_rhythm
      ~abjad.tools.indicatortools.MetricModulation.MetricModulation.__eq__
      ~abjad.tools.indicatortools.MetricModulation.MetricModulation.__format__
      ~abjad.tools.indicatortools.MetricModulation.MetricModulation.__hash__
      ~abjad.tools.indicatortools.MetricModulation.MetricModulation.__illustrate__
      ~abjad.tools.indicatortools.MetricModulation.MetricModulation.__ne__
      ~abjad.tools.indicatortools.MetricModulation.MetricModulation.__repr__
      ~abjad.tools.indicatortools.MetricModulation.MetricModulation.__str__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.indicatortools.MetricModulation.MetricModulation.left_markup
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.MetricModulation.MetricModulation.left_rhythm
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.MetricModulation.MetricModulation.ratio
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.MetricModulation.MetricModulation.right_markup
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.MetricModulation.MetricModulation.right_rhythm
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.indicatortools.MetricModulation.MetricModulation.__eq__
   :noindex:

.. automethod:: abjad.tools.indicatortools.MetricModulation.MetricModulation.__format__
   :noindex:

.. automethod:: abjad.tools.indicatortools.MetricModulation.MetricModulation.__hash__
   :noindex:

.. automethod:: abjad.tools.indicatortools.MetricModulation.MetricModulation.__illustrate__
   :noindex:

.. automethod:: abjad.tools.indicatortools.MetricModulation.MetricModulation.__ne__
   :noindex:

.. automethod:: abjad.tools.indicatortools.MetricModulation.MetricModulation.__repr__
   :noindex:

.. automethod:: abjad.tools.indicatortools.MetricModulation.MetricModulation.__str__
   :noindex:
