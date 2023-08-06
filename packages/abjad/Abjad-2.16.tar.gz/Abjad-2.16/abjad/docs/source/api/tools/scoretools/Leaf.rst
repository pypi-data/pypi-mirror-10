scoretools.Leaf
===============

.. autoclass:: abjad.tools.scoretools.Leaf.Leaf

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
           "scoretools.Component" [color=3,
               group=2,
               label=Component,
               shape=oval,
               style=bold];
           "scoretools.Leaf" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Leaf</B>>,
               shape=oval,
               style="filled, rounded"];
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
           "scoretools.Skip" [color=3,
               group=2,
               label=Skip,
               shape=box];
           "scoretools.Component" -> "scoretools.Leaf";
           "scoretools.Leaf" -> "scoretools.Chord";
           "scoretools.Leaf" -> "scoretools.MultimeasureRest";
           "scoretools.Leaf" -> "scoretools.Note";
           "scoretools.Leaf" -> "scoretools.Rest";
           "scoretools.Leaf" -> "scoretools.Skip";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "scoretools.Component";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.scoretools.Leaf.Leaf.name
      ~abjad.tools.scoretools.Leaf.Leaf.written_duration
      ~abjad.tools.scoretools.Leaf.Leaf.__copy__
      ~abjad.tools.scoretools.Leaf.Leaf.__eq__
      ~abjad.tools.scoretools.Leaf.Leaf.__format__
      ~abjad.tools.scoretools.Leaf.Leaf.__hash__
      ~abjad.tools.scoretools.Leaf.Leaf.__illustrate__
      ~abjad.tools.scoretools.Leaf.Leaf.__mul__
      ~abjad.tools.scoretools.Leaf.Leaf.__ne__
      ~abjad.tools.scoretools.Leaf.Leaf.__repr__
      ~abjad.tools.scoretools.Leaf.Leaf.__rmul__
      ~abjad.tools.scoretools.Leaf.Leaf.__str__

Bases
-----

- :py:class:`scoretools.Component <abjad.tools.scoretools.Component.Component>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read/write properties
---------------------

.. autoattribute:: abjad.tools.scoretools.Leaf.Leaf.name
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Leaf.Leaf.written_duration
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.scoretools.Leaf.Leaf.__copy__
   :noindex:

.. automethod:: abjad.tools.scoretools.Leaf.Leaf.__eq__
   :noindex:

.. automethod:: abjad.tools.scoretools.Leaf.Leaf.__format__
   :noindex:

.. automethod:: abjad.tools.scoretools.Leaf.Leaf.__hash__
   :noindex:

.. automethod:: abjad.tools.scoretools.Leaf.Leaf.__illustrate__
   :noindex:

.. automethod:: abjad.tools.scoretools.Leaf.Leaf.__mul__
   :noindex:

.. automethod:: abjad.tools.scoretools.Leaf.Leaf.__ne__
   :noindex:

.. automethod:: abjad.tools.scoretools.Leaf.Leaf.__repr__
   :noindex:

.. automethod:: abjad.tools.scoretools.Leaf.Leaf.__rmul__
   :noindex:

.. automethod:: abjad.tools.scoretools.Leaf.Leaf.__str__
   :noindex:
