quantizationtools.AttackPointOptimizer
======================================

.. autoclass:: abjad.tools.quantizationtools.AttackPointOptimizer.AttackPointOptimizer

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
           "quantizationtools.AttackPointOptimizer" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>AttackPointOptimizer</B>>,
               shape=oval,
               style="filled, rounded"];
           "quantizationtools.MeasurewiseAttackPointOptimizer" [color=3,
               group=2,
               label=MeasurewiseAttackPointOptimizer,
               shape=box];
           "quantizationtools.NaiveAttackPointOptimizer" [color=3,
               group=2,
               label=NaiveAttackPointOptimizer,
               shape=box];
           "quantizationtools.NullAttackPointOptimizer" [color=3,
               group=2,
               label=NullAttackPointOptimizer,
               shape=box];
           "quantizationtools.AttackPointOptimizer" -> "quantizationtools.MeasurewiseAttackPointOptimizer";
           "quantizationtools.AttackPointOptimizer" -> "quantizationtools.NaiveAttackPointOptimizer";
           "quantizationtools.AttackPointOptimizer" -> "quantizationtools.NullAttackPointOptimizer";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.AttackPointOptimizer";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.AttackPointOptimizer.AttackPointOptimizer.__call__
      ~abjad.tools.quantizationtools.AttackPointOptimizer.AttackPointOptimizer.__eq__
      ~abjad.tools.quantizationtools.AttackPointOptimizer.AttackPointOptimizer.__format__
      ~abjad.tools.quantizationtools.AttackPointOptimizer.AttackPointOptimizer.__hash__
      ~abjad.tools.quantizationtools.AttackPointOptimizer.AttackPointOptimizer.__ne__
      ~abjad.tools.quantizationtools.AttackPointOptimizer.AttackPointOptimizer.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.AttackPointOptimizer.AttackPointOptimizer.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.AttackPointOptimizer.AttackPointOptimizer.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.AttackPointOptimizer.AttackPointOptimizer.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.AttackPointOptimizer.AttackPointOptimizer.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.AttackPointOptimizer.AttackPointOptimizer.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.AttackPointOptimizer.AttackPointOptimizer.__repr__
   :noindex:
