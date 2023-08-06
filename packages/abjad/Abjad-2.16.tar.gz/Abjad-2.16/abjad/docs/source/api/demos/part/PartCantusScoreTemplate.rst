part.PartCantusScoreTemplate
============================

.. autoclass:: abjad.demos.part.PartCantusScoreTemplate.PartCantusScoreTemplate

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
       subgraph cluster_abjad {
           graph [label=abjad];
           "abjad.demos.part.PartCantusScoreTemplate" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>PartCantusScoreTemplate</B>>,
               shape=box,
               style="filled, rounded"];
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
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "abjad.demos.part.PartCantusScoreTemplate";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.demos.part.PartCantusScoreTemplate.PartCantusScoreTemplate.__call__
      ~abjad.demos.part.PartCantusScoreTemplate.PartCantusScoreTemplate.__eq__
      ~abjad.demos.part.PartCantusScoreTemplate.PartCantusScoreTemplate.__format__
      ~abjad.demos.part.PartCantusScoreTemplate.PartCantusScoreTemplate.__hash__
      ~abjad.demos.part.PartCantusScoreTemplate.PartCantusScoreTemplate.__ne__
      ~abjad.demos.part.PartCantusScoreTemplate.PartCantusScoreTemplate.__repr__

Bases
-----

- :py:class:`abjad.tools.abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abjad.tools.abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.demos.part.PartCantusScoreTemplate.PartCantusScoreTemplate.__call__
   :noindex:

.. automethod:: abjad.demos.part.PartCantusScoreTemplate.PartCantusScoreTemplate.__eq__
   :noindex:

.. automethod:: abjad.demos.part.PartCantusScoreTemplate.PartCantusScoreTemplate.__format__
   :noindex:

.. automethod:: abjad.demos.part.PartCantusScoreTemplate.PartCantusScoreTemplate.__hash__
   :noindex:

.. automethod:: abjad.demos.part.PartCantusScoreTemplate.PartCantusScoreTemplate.__ne__
   :noindex:

.. automethod:: abjad.demos.part.PartCantusScoreTemplate.PartCantusScoreTemplate.__repr__
   :noindex:
