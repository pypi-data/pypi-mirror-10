quantizationtools.MeasurewiseQSchemaItem
========================================

.. autoclass:: abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem

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
           "quantizationtools.MeasurewiseQSchemaItem" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>MeasurewiseQSchemaItem</B>>,
               shape=box,
               style="filled, rounded"];
           "quantizationtools.QSchemaItem" [color=3,
               group=2,
               label=QSchemaItem,
               shape=oval,
               style=bold];
           "quantizationtools.QSchemaItem" -> "quantizationtools.MeasurewiseQSchemaItem";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.QSchemaItem";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.beatspan
      ~abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.search_tree
      ~abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.tempo
      ~abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.time_signature
      ~abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.use_full_measure
      ~abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.__eq__
      ~abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.__format__
      ~abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.__hash__
      ~abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.__ne__
      ~abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.__repr__

Bases
-----

- :py:class:`quantizationtools.QSchemaItem <abjad.tools.quantizationtools.QSchemaItem.QSchemaItem>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.beatspan
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.search_tree
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.tempo
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.time_signature
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.use_full_measure
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQSchemaItem.MeasurewiseQSchemaItem.__repr__
   :noindex:
