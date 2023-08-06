quantizationtools.BeatwiseQSchema
=================================

.. autoclass:: abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema

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
           "quantizationtools.BeatwiseQSchema" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>BeatwiseQSchema</B>>,
               shape=box,
               style="filled, rounded"];
           "quantizationtools.QSchema" [color=3,
               group=2,
               label=QSchema,
               shape=oval,
               style=bold];
           "quantizationtools.QSchema" -> "quantizationtools.BeatwiseQSchema";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.QSchema";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.beatspan
      ~abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.item_class
      ~abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.items
      ~abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.search_tree
      ~abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.target_class
      ~abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.target_item_class
      ~abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.tempo
      ~abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.__call__
      ~abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.__eq__
      ~abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.__format__
      ~abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.__getitem__
      ~abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.__hash__
      ~abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.__ne__
      ~abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.__repr__

Bases
-----

- :py:class:`quantizationtools.QSchema <abjad.tools.quantizationtools.QSchema.QSchema>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.beatspan
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.item_class
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.items
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.search_tree
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.target_class
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.target_item_class
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.tempo
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.__getitem__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.BeatwiseQSchema.BeatwiseQSchema.__repr__
   :noindex:
