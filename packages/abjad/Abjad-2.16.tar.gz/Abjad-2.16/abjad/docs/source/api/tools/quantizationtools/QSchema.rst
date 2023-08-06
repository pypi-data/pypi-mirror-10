quantizationtools.QSchema
=========================

.. autoclass:: abjad.tools.quantizationtools.QSchema.QSchema

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
           "quantizationtools.BeatwiseQSchema" [color=3,
               group=2,
               label=BeatwiseQSchema,
               shape=box];
           "quantizationtools.MeasurewiseQSchema" [color=3,
               group=2,
               label=MeasurewiseQSchema,
               shape=box];
           "quantizationtools.QSchema" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>QSchema</B>>,
               shape=oval,
               style="filled, rounded"];
           "quantizationtools.QSchema" -> "quantizationtools.BeatwiseQSchema";
           "quantizationtools.QSchema" -> "quantizationtools.MeasurewiseQSchema";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.QSchema";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.QSchema.QSchema.item_class
      ~abjad.tools.quantizationtools.QSchema.QSchema.items
      ~abjad.tools.quantizationtools.QSchema.QSchema.search_tree
      ~abjad.tools.quantizationtools.QSchema.QSchema.target_class
      ~abjad.tools.quantizationtools.QSchema.QSchema.target_item_class
      ~abjad.tools.quantizationtools.QSchema.QSchema.tempo
      ~abjad.tools.quantizationtools.QSchema.QSchema.__call__
      ~abjad.tools.quantizationtools.QSchema.QSchema.__eq__
      ~abjad.tools.quantizationtools.QSchema.QSchema.__format__
      ~abjad.tools.quantizationtools.QSchema.QSchema.__getitem__
      ~abjad.tools.quantizationtools.QSchema.QSchema.__hash__
      ~abjad.tools.quantizationtools.QSchema.QSchema.__ne__
      ~abjad.tools.quantizationtools.QSchema.QSchema.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.QSchema.QSchema.item_class
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QSchema.QSchema.items
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QSchema.QSchema.search_tree
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QSchema.QSchema.target_class
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QSchema.QSchema.target_item_class
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QSchema.QSchema.tempo
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.QSchema.QSchema.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QSchema.QSchema.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QSchema.QSchema.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QSchema.QSchema.__getitem__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QSchema.QSchema.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QSchema.QSchema.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QSchema.QSchema.__repr__
   :noindex:
