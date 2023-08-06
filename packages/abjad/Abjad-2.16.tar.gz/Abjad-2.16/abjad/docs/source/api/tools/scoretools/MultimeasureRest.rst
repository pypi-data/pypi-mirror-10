scoretools.MultimeasureRest
===========================

.. autoclass:: abjad.tools.scoretools.MultimeasureRest.MultimeasureRest

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
           "scoretools.Component" [color=3,
               group=2,
               label=Component,
               shape=oval,
               style=bold];
           "scoretools.Leaf" [color=3,
               group=2,
               label=Leaf,
               shape=oval,
               style=bold];
           "scoretools.MultimeasureRest" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>MultimeasureRest</B>>,
               shape=box,
               style="filled, rounded"];
           "scoretools.Component" -> "scoretools.Leaf";
           "scoretools.Leaf" -> "scoretools.MultimeasureRest";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "scoretools.Component";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.name
      ~abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.written_duration
      ~abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__copy__
      ~abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__eq__
      ~abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__format__
      ~abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__hash__
      ~abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__illustrate__
      ~abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__mul__
      ~abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__ne__
      ~abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__repr__
      ~abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__rmul__
      ~abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__str__

Bases
-----

- :py:class:`scoretools.Leaf <abjad.tools.scoretools.Leaf.Leaf>`

- :py:class:`scoretools.Component <abjad.tools.scoretools.Component.Component>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read/write properties
---------------------

.. autoattribute:: abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.name
   :noindex:

.. autoattribute:: abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.written_duration
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__copy__
   :noindex:

.. automethod:: abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__eq__
   :noindex:

.. automethod:: abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__format__
   :noindex:

.. automethod:: abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__hash__
   :noindex:

.. automethod:: abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__illustrate__
   :noindex:

.. automethod:: abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__mul__
   :noindex:

.. automethod:: abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__ne__
   :noindex:

.. automethod:: abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__repr__
   :noindex:

.. automethod:: abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__rmul__
   :noindex:

.. automethod:: abjad.tools.scoretools.MultimeasureRest.MultimeasureRest.__str__
   :noindex:
