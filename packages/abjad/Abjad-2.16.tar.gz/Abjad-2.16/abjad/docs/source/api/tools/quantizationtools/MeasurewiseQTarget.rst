quantizationtools.MeasurewiseQTarget
====================================

.. autoclass:: abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget

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
       subgraph cluster_quantizationtools {
           graph [label=quantizationtools];
           "quantizationtools.MeasurewiseQTarget" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>MeasurewiseQTarget</B>>,
               shape=box,
               style="filled, rounded"];
           "quantizationtools.QTarget" [color=3,
               group=2,
               label=QTarget,
               shape=oval,
               style=bold];
           "quantizationtools.QTarget" -> "quantizationtools.MeasurewiseQTarget";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.QTarget";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.beats
      ~abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.duration_in_ms
      ~abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.item_class
      ~abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.items
      ~abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.__call__
      ~abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.__eq__
      ~abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.__format__
      ~abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.__hash__
      ~abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.__ne__
      ~abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.__repr__

Bases
-----

- :py:class:`quantizationtools.QTarget <abjad.tools.quantizationtools.QTarget.QTarget>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.beats
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.duration_in_ms
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.item_class
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.items
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQTarget.MeasurewiseQTarget.__repr__
   :noindex:
