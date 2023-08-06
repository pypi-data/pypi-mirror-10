scoretools.Component
====================

.. autoclass:: abjad.tools.scoretools.Component.Component

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
       subgraph cluster_scoretools {
           graph [label=scoretools];
           "scoretools.Chord" [color=3,
               group=2,
               label=Chord,
               shape=box];
           "scoretools.Cluster" [color=3,
               group=2,
               label=Cluster,
               shape=box];
           "scoretools.Component" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Component</B>>,
               shape=oval,
               style="filled, rounded"];
           "scoretools.Container" [color=3,
               group=2,
               label=Container,
               shape=box];
           "scoretools.Context" [color=3,
               group=2,
               label=Context,
               shape=box];
           "scoretools.FixedDurationContainer" [color=3,
               group=2,
               label=FixedDurationContainer,
               shape=box];
           "scoretools.FixedDurationTuplet" [color=3,
               group=2,
               label=FixedDurationTuplet,
               shape=box];
           "scoretools.GraceContainer" [color=3,
               group=2,
               label=GraceContainer,
               shape=box];
           "scoretools.Leaf" [color=3,
               group=2,
               label=Leaf,
               shape=oval,
               style=bold];
           "scoretools.Measure" [color=3,
               group=2,
               label=Measure,
               shape=box];
           "scoretools.MultimeasureRest" [color=3,
               group=2,
               label=MultimeasureRest,
               shape=box];
           "scoretools.Note" [color=3,
               group=2,
               label=Note,
               shape=box];
           "scoretools.Rest" [color=3,
               group=2,
               label=Rest,
               shape=box];
           "scoretools.Score" [color=3,
               group=2,
               label=Score,
               shape=box];
           "scoretools.Skip" [color=3,
               group=2,
               label=Skip,
               shape=box];
           "scoretools.Staff" [color=3,
               group=2,
               label=Staff,
               shape=box];
           "scoretools.StaffGroup" [color=3,
               group=2,
               label=StaffGroup,
               shape=box];
           "scoretools.Tuplet" [color=3,
               group=2,
               label=Tuplet,
               shape=box];
           "scoretools.Voice" [color=3,
               group=2,
               label=Voice,
               shape=box];
           "scoretools.Component" -> "scoretools.Container";
           "scoretools.Component" -> "scoretools.Leaf";
           "scoretools.Container" -> "scoretools.Cluster";
           "scoretools.Container" -> "scoretools.Context";
           "scoretools.Container" -> "scoretools.FixedDurationContainer";
           "scoretools.Container" -> "scoretools.GraceContainer";
           "scoretools.Container" -> "scoretools.Tuplet";
           "scoretools.Context" -> "scoretools.Score";
           "scoretools.Context" -> "scoretools.Staff";
           "scoretools.Context" -> "scoretools.StaffGroup";
           "scoretools.Context" -> "scoretools.Voice";
           "scoretools.FixedDurationContainer" -> "scoretools.Measure";
           "scoretools.Leaf" -> "scoretools.Chord";
           "scoretools.Leaf" -> "scoretools.MultimeasureRest";
           "scoretools.Leaf" -> "scoretools.Note";
           "scoretools.Leaf" -> "scoretools.Rest";
           "scoretools.Leaf" -> "scoretools.Skip";
           "scoretools.Tuplet" -> "scoretools.FixedDurationTuplet";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "scoretools.Component";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.scoretools.Component.Component.name
      ~abjad.tools.scoretools.Component.Component.__copy__
      ~abjad.tools.scoretools.Component.Component.__eq__
      ~abjad.tools.scoretools.Component.Component.__format__
      ~abjad.tools.scoretools.Component.Component.__hash__
      ~abjad.tools.scoretools.Component.Component.__illustrate__
      ~abjad.tools.scoretools.Component.Component.__mul__
      ~abjad.tools.scoretools.Component.Component.__ne__
      ~abjad.tools.scoretools.Component.Component.__repr__
      ~abjad.tools.scoretools.Component.Component.__rmul__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read/write properties
---------------------

.. autoattribute:: abjad.tools.scoretools.Component.Component.name
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.scoretools.Component.Component.__copy__
   :noindex:

.. automethod:: abjad.tools.scoretools.Component.Component.__eq__
   :noindex:

.. automethod:: abjad.tools.scoretools.Component.Component.__format__
   :noindex:

.. automethod:: abjad.tools.scoretools.Component.Component.__hash__
   :noindex:

.. automethod:: abjad.tools.scoretools.Component.Component.__illustrate__
   :noindex:

.. automethod:: abjad.tools.scoretools.Component.Component.__mul__
   :noindex:

.. automethod:: abjad.tools.scoretools.Component.Component.__ne__
   :noindex:

.. automethod:: abjad.tools.scoretools.Component.Component.__repr__
   :noindex:

.. automethod:: abjad.tools.scoretools.Component.Component.__rmul__
   :noindex:
