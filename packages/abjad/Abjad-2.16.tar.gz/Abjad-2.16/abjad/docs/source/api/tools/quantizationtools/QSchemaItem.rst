quantizationtools.QSchemaItem
=============================

.. autoclass:: abjad.tools.quantizationtools.QSchemaItem.QSchemaItem

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
           "quantizationtools.BeatwiseQSchemaItem" [color=3,
               group=2,
               label=BeatwiseQSchemaItem,
               shape=box];
           "quantizationtools.MeasurewiseQSchemaItem" [color=3,
               group=2,
               label=MeasurewiseQSchemaItem,
               shape=box];
           "quantizationtools.QSchemaItem" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>QSchemaItem</B>>,
               shape=oval,
               style="filled, rounded"];
           "quantizationtools.QSchemaItem" -> "quantizationtools.BeatwiseQSchemaItem";
           "quantizationtools.QSchemaItem" -> "quantizationtools.MeasurewiseQSchemaItem";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.QSchemaItem";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.QSchemaItem.QSchemaItem.search_tree
      ~abjad.tools.quantizationtools.QSchemaItem.QSchemaItem.tempo
      ~abjad.tools.quantizationtools.QSchemaItem.QSchemaItem.__eq__
      ~abjad.tools.quantizationtools.QSchemaItem.QSchemaItem.__format__
      ~abjad.tools.quantizationtools.QSchemaItem.QSchemaItem.__hash__
      ~abjad.tools.quantizationtools.QSchemaItem.QSchemaItem.__ne__
      ~abjad.tools.quantizationtools.QSchemaItem.QSchemaItem.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.QSchemaItem.QSchemaItem.search_tree
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QSchemaItem.QSchemaItem.tempo
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.QSchemaItem.QSchemaItem.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QSchemaItem.QSchemaItem.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QSchemaItem.QSchemaItem.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QSchemaItem.QSchemaItem.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QSchemaItem.QSchemaItem.__repr__
   :noindex:
