scoretools.Chord
================

.. autoclass:: abjad.tools.scoretools.Chord.Chord

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
           "scoretools.Chord" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Chord</B>>,
               shape=box,
               style="filled, rounded"];
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
           "scoretools.Component" -> "scoretools.Leaf";
           "scoretools.Leaf" -> "scoretools.Chord";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "scoretools.Component";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.scoretools.Chord.Chord.name
      ~abjad.tools.scoretools.Chord.Chord.note_heads
      ~abjad.tools.scoretools.Chord.Chord.written_duration
      ~abjad.tools.scoretools.Chord.Chord.written_pitches
      ~abjad.tools.scoretools.Chord.Chord.__copy__
      ~abjad.tools.scoretools.Chord.Chord.__eq__
      ~abjad.tools.scoretools.Chord.Chord.__format__
      ~abjad.tools.scoretools.Chord.Chord.__hash__
      ~abjad.tools.scoretools.Chord.Chord.__illustrate__
      ~abjad.tools.scoretools.Chord.Chord.__mul__
      ~abjad.tools.scoretools.Chord.Chord.__ne__
      ~abjad.tools.scoretools.Chord.Chord.__repr__
      ~abjad.tools.scoretools.Chord.Chord.__rmul__
      ~abjad.tools.scoretools.Chord.Chord.__str__

Bases
-----

- :py:class:`scoretools.Leaf <abjad.tools.scoretools.Leaf.Leaf>`

- :py:class:`scoretools.Component <abjad.tools.scoretools.Component.Component>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read/write properties
---------------------

.. autoattribute:: abjad.tools.scoretools.Chord.Chord.name
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Chord.Chord.note_heads
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Chord.Chord.written_duration
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Chord.Chord.written_pitches
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.scoretools.Chord.Chord.__copy__
   :noindex:

.. automethod:: abjad.tools.scoretools.Chord.Chord.__eq__
   :noindex:

.. automethod:: abjad.tools.scoretools.Chord.Chord.__format__
   :noindex:

.. automethod:: abjad.tools.scoretools.Chord.Chord.__hash__
   :noindex:

.. automethod:: abjad.tools.scoretools.Chord.Chord.__illustrate__
   :noindex:

.. automethod:: abjad.tools.scoretools.Chord.Chord.__mul__
   :noindex:

.. automethod:: abjad.tools.scoretools.Chord.Chord.__ne__
   :noindex:

.. automethod:: abjad.tools.scoretools.Chord.Chord.__repr__
   :noindex:

.. automethod:: abjad.tools.scoretools.Chord.Chord.__rmul__
   :noindex:

.. automethod:: abjad.tools.scoretools.Chord.Chord.__str__
   :noindex:
