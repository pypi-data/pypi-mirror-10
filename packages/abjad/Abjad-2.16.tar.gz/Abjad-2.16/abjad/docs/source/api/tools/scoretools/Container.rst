scoretools.Container
====================

.. autoclass:: abjad.tools.scoretools.Container.Container

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
           "scoretools.Cluster" [color=3,
               group=2,
               label=Cluster,
               shape=box];
           "scoretools.Component" [color=3,
               group=2,
               label=Component,
               shape=oval,
               style=bold];
           "scoretools.Container" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Container</B>>,
               shape=box,
               style="filled, rounded"];
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
           "scoretools.Measure" [color=3,
               group=2,
               label=Measure,
               shape=box];
           "scoretools.Score" [color=3,
               group=2,
               label=Score,
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
           "scoretools.Tuplet" -> "scoretools.FixedDurationTuplet";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "scoretools.Component";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.scoretools.Container.Container.append
      ~abjad.tools.scoretools.Container.Container.extend
      ~abjad.tools.scoretools.Container.Container.index
      ~abjad.tools.scoretools.Container.Container.insert
      ~abjad.tools.scoretools.Container.Container.is_simultaneous
      ~abjad.tools.scoretools.Container.Container.name
      ~abjad.tools.scoretools.Container.Container.pop
      ~abjad.tools.scoretools.Container.Container.remove
      ~abjad.tools.scoretools.Container.Container.reverse
      ~abjad.tools.scoretools.Container.Container.select_leaves
      ~abjad.tools.scoretools.Container.Container.__contains__
      ~abjad.tools.scoretools.Container.Container.__copy__
      ~abjad.tools.scoretools.Container.Container.__delitem__
      ~abjad.tools.scoretools.Container.Container.__eq__
      ~abjad.tools.scoretools.Container.Container.__format__
      ~abjad.tools.scoretools.Container.Container.__getitem__
      ~abjad.tools.scoretools.Container.Container.__graph__
      ~abjad.tools.scoretools.Container.Container.__hash__
      ~abjad.tools.scoretools.Container.Container.__illustrate__
      ~abjad.tools.scoretools.Container.Container.__len__
      ~abjad.tools.scoretools.Container.Container.__mul__
      ~abjad.tools.scoretools.Container.Container.__ne__
      ~abjad.tools.scoretools.Container.Container.__repr__
      ~abjad.tools.scoretools.Container.Container.__rmul__
      ~abjad.tools.scoretools.Container.Container.__setitem__

Bases
-----

- :py:class:`scoretools.Component <abjad.tools.scoretools.Component.Component>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read/write properties
---------------------

.. autoattribute:: abjad.tools.scoretools.Container.Container.is_simultaneous
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Container.Container.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.scoretools.Container.Container.append
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.extend
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.index
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.insert
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.pop
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.remove
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.reverse
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.select_leaves
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.scoretools.Container.Container.__contains__
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.__copy__
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.__delitem__
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.__eq__
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.__format__
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.__getitem__
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.__graph__
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.__hash__
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.__illustrate__
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.__len__
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.__mul__
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.__ne__
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.__repr__
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.__rmul__
   :noindex:

.. automethod:: abjad.tools.scoretools.Container.Container.__setitem__
   :noindex:
