quantizationtools.QTarget
=========================

.. autoclass:: abjad.tools.quantizationtools.QTarget.QTarget

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
           "quantizationtools.BeatwiseQTarget" [color=3,
               group=2,
               label=BeatwiseQTarget,
               shape=box];
           "quantizationtools.MeasurewiseQTarget" [color=3,
               group=2,
               label=MeasurewiseQTarget,
               shape=box];
           "quantizationtools.QTarget" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>QTarget</B>>,
               shape=oval,
               style="filled, rounded"];
           "quantizationtools.QTarget" -> "quantizationtools.BeatwiseQTarget";
           "quantizationtools.QTarget" -> "quantizationtools.MeasurewiseQTarget";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.QTarget";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.QTarget.QTarget.beats
      ~abjad.tools.quantizationtools.QTarget.QTarget.duration_in_ms
      ~abjad.tools.quantizationtools.QTarget.QTarget.item_class
      ~abjad.tools.quantizationtools.QTarget.QTarget.items
      ~abjad.tools.quantizationtools.QTarget.QTarget.__call__
      ~abjad.tools.quantizationtools.QTarget.QTarget.__eq__
      ~abjad.tools.quantizationtools.QTarget.QTarget.__format__
      ~abjad.tools.quantizationtools.QTarget.QTarget.__hash__
      ~abjad.tools.quantizationtools.QTarget.QTarget.__ne__
      ~abjad.tools.quantizationtools.QTarget.QTarget.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.QTarget.QTarget.beats
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QTarget.QTarget.duration_in_ms
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QTarget.QTarget.item_class
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QTarget.QTarget.items
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.QTarget.QTarget.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QTarget.QTarget.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QTarget.QTarget.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QTarget.QTarget.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QTarget.QTarget.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QTarget.QTarget.__repr__
   :noindex:
