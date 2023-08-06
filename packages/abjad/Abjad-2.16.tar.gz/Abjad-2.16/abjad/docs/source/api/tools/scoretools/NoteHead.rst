scoretools.NoteHead
===================

.. autoclass:: abjad.tools.scoretools.NoteHead.NoteHead

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
           "scoretools.DrumNoteHead" [color=3,
               group=2,
               label=DrumNoteHead,
               shape=box];
           "scoretools.NoteHead" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>NoteHead</B>>,
               shape=box,
               style="filled, rounded"];
           "scoretools.NoteHead" -> "scoretools.DrumNoteHead";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "scoretools.NoteHead";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.scoretools.NoteHead.NoteHead.client
      ~abjad.tools.scoretools.NoteHead.NoteHead.is_cautionary
      ~abjad.tools.scoretools.NoteHead.NoteHead.is_forced
      ~abjad.tools.scoretools.NoteHead.NoteHead.is_parenthesized
      ~abjad.tools.scoretools.NoteHead.NoteHead.named_pitch
      ~abjad.tools.scoretools.NoteHead.NoteHead.tweak
      ~abjad.tools.scoretools.NoteHead.NoteHead.written_pitch
      ~abjad.tools.scoretools.NoteHead.NoteHead.__copy__
      ~abjad.tools.scoretools.NoteHead.NoteHead.__eq__
      ~abjad.tools.scoretools.NoteHead.NoteHead.__format__
      ~abjad.tools.scoretools.NoteHead.NoteHead.__ge__
      ~abjad.tools.scoretools.NoteHead.NoteHead.__gt__
      ~abjad.tools.scoretools.NoteHead.NoteHead.__hash__
      ~abjad.tools.scoretools.NoteHead.NoteHead.__le__
      ~abjad.tools.scoretools.NoteHead.NoteHead.__lt__
      ~abjad.tools.scoretools.NoteHead.NoteHead.__ne__
      ~abjad.tools.scoretools.NoteHead.NoteHead.__repr__
      ~abjad.tools.scoretools.NoteHead.NoteHead.__str__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.scoretools.NoteHead.NoteHead.client
   :noindex:

.. autoattribute:: abjad.tools.scoretools.NoteHead.NoteHead.named_pitch
   :noindex:

.. autoattribute:: abjad.tools.scoretools.NoteHead.NoteHead.tweak
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.scoretools.NoteHead.NoteHead.is_cautionary
   :noindex:

.. autoattribute:: abjad.tools.scoretools.NoteHead.NoteHead.is_forced
   :noindex:

.. autoattribute:: abjad.tools.scoretools.NoteHead.NoteHead.is_parenthesized
   :noindex:

.. autoattribute:: abjad.tools.scoretools.NoteHead.NoteHead.written_pitch
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.scoretools.NoteHead.NoteHead.__copy__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHead.NoteHead.__eq__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHead.NoteHead.__format__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHead.NoteHead.__ge__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHead.NoteHead.__gt__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHead.NoteHead.__hash__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHead.NoteHead.__le__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHead.NoteHead.__lt__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHead.NoteHead.__ne__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHead.NoteHead.__repr__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHead.NoteHead.__str__
   :noindex:
