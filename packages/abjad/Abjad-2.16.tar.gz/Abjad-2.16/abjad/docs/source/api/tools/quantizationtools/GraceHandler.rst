quantizationtools.GraceHandler
==============================

.. autoclass:: abjad.tools.quantizationtools.GraceHandler.GraceHandler

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
           "quantizationtools.CollapsingGraceHandler" [color=3,
               group=2,
               label=CollapsingGraceHandler,
               shape=box];
           "quantizationtools.ConcatenatingGraceHandler" [color=3,
               group=2,
               label=ConcatenatingGraceHandler,
               shape=box];
           "quantizationtools.DiscardingGraceHandler" [color=3,
               group=2,
               label=DiscardingGraceHandler,
               shape=box];
           "quantizationtools.GraceHandler" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>GraceHandler</B>>,
               shape=oval,
               style="filled, rounded"];
           "quantizationtools.GraceHandler" -> "quantizationtools.CollapsingGraceHandler";
           "quantizationtools.GraceHandler" -> "quantizationtools.ConcatenatingGraceHandler";
           "quantizationtools.GraceHandler" -> "quantizationtools.DiscardingGraceHandler";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.GraceHandler";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.GraceHandler.GraceHandler.__call__
      ~abjad.tools.quantizationtools.GraceHandler.GraceHandler.__eq__
      ~abjad.tools.quantizationtools.GraceHandler.GraceHandler.__format__
      ~abjad.tools.quantizationtools.GraceHandler.GraceHandler.__hash__
      ~abjad.tools.quantizationtools.GraceHandler.GraceHandler.__ne__
      ~abjad.tools.quantizationtools.GraceHandler.GraceHandler.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.GraceHandler.GraceHandler.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.GraceHandler.GraceHandler.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.GraceHandler.GraceHandler.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.GraceHandler.GraceHandler.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.GraceHandler.GraceHandler.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.GraceHandler.GraceHandler.__repr__
   :noindex:
