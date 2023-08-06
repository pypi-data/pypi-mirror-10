quantizationtools.MeasurewiseQSchema
====================================

.. autoclass:: abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema

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
           "quantizationtools.MeasurewiseQSchema" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>MeasurewiseQSchema</B>>,
               shape=box,
               style="filled, rounded"];
           "quantizationtools.QSchema" [color=3,
               group=2,
               label=QSchema,
               shape=oval,
               style=bold];
           "quantizationtools.QSchema" -> "quantizationtools.MeasurewiseQSchema";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.QSchema";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.item_class
      ~abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.items
      ~abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.search_tree
      ~abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.target_class
      ~abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.target_item_class
      ~abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.tempo
      ~abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.time_signature
      ~abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.use_full_measure
      ~abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.__call__
      ~abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.__eq__
      ~abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.__format__
      ~abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.__getitem__
      ~abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.__hash__
      ~abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.__ne__
      ~abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.__repr__

Bases
-----

- :py:class:`quantizationtools.QSchema <abjad.tools.quantizationtools.QSchema.QSchema>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.item_class
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.items
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.search_tree
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.target_class
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.target_item_class
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.tempo
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.time_signature
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.use_full_measure
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.__getitem__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.MeasurewiseQSchema.MeasurewiseQSchema.__repr__
   :noindex:
