quantizationtools.BeatwiseQSchemaItem
=====================================

.. autoclass:: abjad.tools.quantizationtools.BeatwiseQSchemaItem.BeatwiseQSchemaItem

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
           "quantizationtools.BeatwiseQSchemaItem" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>BeatwiseQSchemaItem</B>>,
               shape=box,
               style="filled, rounded"];
           "quantizationtools.QSchemaItem" [color=3,
               group=2,
               label=QSchemaItem,
               shape=oval,
               style=bold];
           "quantizationtools.QSchemaItem" -> "quantizationtools.BeatwiseQSchemaItem";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.QSchemaItem";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.BeatwiseQSchemaItem.BeatwiseQSchemaItem.beatspan
      ~abjad.tools.quantizationtools.BeatwiseQSchemaItem.BeatwiseQSchemaItem.search_tree
      ~abjad.tools.quantizationtools.BeatwiseQSchemaItem.BeatwiseQSchemaItem.tempo
      ~abjad.tools.quantizationtools.BeatwiseQSchemaItem.BeatwiseQSchemaItem.__eq__
      ~abjad.tools.quantizationtools.BeatwiseQSchemaItem.BeatwiseQSchemaItem.__format__
      ~abjad.tools.quantizationtools.BeatwiseQSchemaItem.BeatwiseQSchemaItem.__hash__
      ~abjad.tools.quantizationtools.BeatwiseQSchemaItem.BeatwiseQSchemaItem.__ne__
      ~abjad.tools.quantizationtools.BeatwiseQSchemaItem.BeatwiseQSchemaItem.__repr__

Bases
-----

- :py:class:`quantizationtools.QSchemaItem <abjad.tools.quantizationtools.QSchemaItem.QSchemaItem>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.BeatwiseQSchemaItem.BeatwiseQSchemaItem.beatspan
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.BeatwiseQSchemaItem.BeatwiseQSchemaItem.search_tree
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.BeatwiseQSchemaItem.BeatwiseQSchemaItem.tempo
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.BeatwiseQSchemaItem.BeatwiseQSchemaItem.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.BeatwiseQSchemaItem.BeatwiseQSchemaItem.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.BeatwiseQSchemaItem.BeatwiseQSchemaItem.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.BeatwiseQSchemaItem.BeatwiseQSchemaItem.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.BeatwiseQSchemaItem.BeatwiseQSchemaItem.__repr__
   :noindex:
