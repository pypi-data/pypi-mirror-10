quantizationtools.BeatwiseQTarget
=================================

.. autoclass:: abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget

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
           "quantizationtools.BeatwiseQTarget" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>BeatwiseQTarget</B>>,
               shape=box,
               style="filled, rounded"];
           "quantizationtools.QTarget" [color=3,
               group=2,
               label=QTarget,
               shape=oval,
               style=bold];
           "quantizationtools.QTarget" -> "quantizationtools.BeatwiseQTarget";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.QTarget";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.beats
      ~abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.duration_in_ms
      ~abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.item_class
      ~abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.items
      ~abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.__call__
      ~abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.__eq__
      ~abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.__format__
      ~abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.__hash__
      ~abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.__ne__
      ~abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.__repr__

Bases
-----

- :py:class:`quantizationtools.QTarget <abjad.tools.quantizationtools.QTarget.QTarget>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.beats
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.duration_in_ms
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.item_class
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.items
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.BeatwiseQTarget.BeatwiseQTarget.__repr__
   :noindex:
