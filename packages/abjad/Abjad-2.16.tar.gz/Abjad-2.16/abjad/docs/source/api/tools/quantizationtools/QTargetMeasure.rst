quantizationtools.QTargetMeasure
================================

.. autoclass:: abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure

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
           "quantizationtools.QTargetMeasure" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>QTargetMeasure</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.QTargetMeasure";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.beats
      ~abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.duration_in_ms
      ~abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.offset_in_ms
      ~abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.search_tree
      ~abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.tempo
      ~abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.time_signature
      ~abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.use_full_measure
      ~abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.__eq__
      ~abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.__format__
      ~abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.__hash__
      ~abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.__ne__
      ~abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.beats
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.duration_in_ms
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.offset_in_ms
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.search_tree
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.tempo
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.time_signature
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.use_full_measure
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QTargetMeasure.QTargetMeasure.__repr__
   :noindex:
