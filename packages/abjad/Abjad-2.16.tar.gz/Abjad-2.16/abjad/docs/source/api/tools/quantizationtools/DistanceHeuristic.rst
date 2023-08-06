quantizationtools.DistanceHeuristic
===================================

.. autoclass:: abjad.tools.quantizationtools.DistanceHeuristic.DistanceHeuristic

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
           "quantizationtools.DistanceHeuristic" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>DistanceHeuristic</B>>,
               shape=box,
               style="filled, rounded"];
           "quantizationtools.Heuristic" [color=3,
               group=2,
               label=Heuristic,
               shape=oval,
               style=bold];
           "quantizationtools.Heuristic" -> "quantizationtools.DistanceHeuristic";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.Heuristic";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.DistanceHeuristic.DistanceHeuristic.__call__
      ~abjad.tools.quantizationtools.DistanceHeuristic.DistanceHeuristic.__eq__
      ~abjad.tools.quantizationtools.DistanceHeuristic.DistanceHeuristic.__format__
      ~abjad.tools.quantizationtools.DistanceHeuristic.DistanceHeuristic.__hash__
      ~abjad.tools.quantizationtools.DistanceHeuristic.DistanceHeuristic.__ne__
      ~abjad.tools.quantizationtools.DistanceHeuristic.DistanceHeuristic.__repr__

Bases
-----

- :py:class:`quantizationtools.Heuristic <abjad.tools.quantizationtools.Heuristic.Heuristic>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.DistanceHeuristic.DistanceHeuristic.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.DistanceHeuristic.DistanceHeuristic.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.DistanceHeuristic.DistanceHeuristic.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.DistanceHeuristic.DistanceHeuristic.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.DistanceHeuristic.DistanceHeuristic.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.DistanceHeuristic.DistanceHeuristic.__repr__
   :noindex:
