scoretools.Note
===============

.. autoclass:: abjad.tools.scoretools.Note.Note

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
           "scoretools.Note" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Note</B>>,
               shape=box,
               style="filled, rounded"];
           "scoretools.Component" -> "scoretools.Leaf";
           "scoretools.Leaf" -> "scoretools.Note";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "scoretools.Component";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.scoretools.Note.Note.name
      ~abjad.tools.scoretools.Note.Note.note_head
      ~abjad.tools.scoretools.Note.Note.written_duration
      ~abjad.tools.scoretools.Note.Note.written_pitch
      ~abjad.tools.scoretools.Note.Note.__copy__
      ~abjad.tools.scoretools.Note.Note.__eq__
      ~abjad.tools.scoretools.Note.Note.__format__
      ~abjad.tools.scoretools.Note.Note.__hash__
      ~abjad.tools.scoretools.Note.Note.__illustrate__
      ~abjad.tools.scoretools.Note.Note.__mul__
      ~abjad.tools.scoretools.Note.Note.__ne__
      ~abjad.tools.scoretools.Note.Note.__repr__
      ~abjad.tools.scoretools.Note.Note.__rmul__
      ~abjad.tools.scoretools.Note.Note.__str__

Bases
-----

- :py:class:`scoretools.Leaf <abjad.tools.scoretools.Leaf.Leaf>`

- :py:class:`scoretools.Component <abjad.tools.scoretools.Component.Component>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read/write properties
---------------------

.. autoattribute:: abjad.tools.scoretools.Note.Note.name
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Note.Note.note_head
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Note.Note.written_duration
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Note.Note.written_pitch
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.scoretools.Note.Note.__copy__
   :noindex:

.. automethod:: abjad.tools.scoretools.Note.Note.__eq__
   :noindex:

.. automethod:: abjad.tools.scoretools.Note.Note.__format__
   :noindex:

.. automethod:: abjad.tools.scoretools.Note.Note.__hash__
   :noindex:

.. automethod:: abjad.tools.scoretools.Note.Note.__illustrate__
   :noindex:

.. automethod:: abjad.tools.scoretools.Note.Note.__mul__
   :noindex:

.. automethod:: abjad.tools.scoretools.Note.Note.__ne__
   :noindex:

.. automethod:: abjad.tools.scoretools.Note.Note.__repr__
   :noindex:

.. automethod:: abjad.tools.scoretools.Note.Note.__rmul__
   :noindex:

.. automethod:: abjad.tools.scoretools.Note.Note.__str__
   :noindex:
