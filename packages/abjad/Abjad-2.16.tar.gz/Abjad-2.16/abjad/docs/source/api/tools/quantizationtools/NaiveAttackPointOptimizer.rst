quantizationtools.NaiveAttackPointOptimizer
===========================================

.. autoclass:: abjad.tools.quantizationtools.NaiveAttackPointOptimizer.NaiveAttackPointOptimizer

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
           "quantizationtools.AttackPointOptimizer" [color=3,
               group=2,
               label=AttackPointOptimizer,
               shape=oval,
               style=bold];
           "quantizationtools.NaiveAttackPointOptimizer" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>NaiveAttackPointOptimizer</B>>,
               shape=box,
               style="filled, rounded"];
           "quantizationtools.AttackPointOptimizer" -> "quantizationtools.NaiveAttackPointOptimizer";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.AttackPointOptimizer";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.NaiveAttackPointOptimizer.NaiveAttackPointOptimizer.__call__
      ~abjad.tools.quantizationtools.NaiveAttackPointOptimizer.NaiveAttackPointOptimizer.__eq__
      ~abjad.tools.quantizationtools.NaiveAttackPointOptimizer.NaiveAttackPointOptimizer.__format__
      ~abjad.tools.quantizationtools.NaiveAttackPointOptimizer.NaiveAttackPointOptimizer.__hash__
      ~abjad.tools.quantizationtools.NaiveAttackPointOptimizer.NaiveAttackPointOptimizer.__ne__
      ~abjad.tools.quantizationtools.NaiveAttackPointOptimizer.NaiveAttackPointOptimizer.__repr__

Bases
-----

- :py:class:`quantizationtools.AttackPointOptimizer <abjad.tools.quantizationtools.AttackPointOptimizer.AttackPointOptimizer>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.NaiveAttackPointOptimizer.NaiveAttackPointOptimizer.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.NaiveAttackPointOptimizer.NaiveAttackPointOptimizer.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.NaiveAttackPointOptimizer.NaiveAttackPointOptimizer.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.NaiveAttackPointOptimizer.NaiveAttackPointOptimizer.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.NaiveAttackPointOptimizer.NaiveAttackPointOptimizer.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.NaiveAttackPointOptimizer.NaiveAttackPointOptimizer.__repr__
   :noindex:
