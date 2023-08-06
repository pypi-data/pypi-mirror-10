ipythontools.Play
=================

.. autoclass:: abjad.tools.ipythontools.Play.Play

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
       subgraph cluster_ipythontools {
           graph [label=ipythontools];
           "ipythontools.Play" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>Play</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "ipythontools.Play";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.ipythontools.Play.Play.load_sound_font
      ~abjad.tools.ipythontools.Play.Play.midi_bank
      ~abjad.tools.ipythontools.Play.Play.sound_font
      ~abjad.tools.ipythontools.Play.Play.__call__

Bases
-----

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.ipythontools.Play.Play.midi_bank
   :noindex:

.. autoattribute:: abjad.tools.ipythontools.Play.Play.sound_font
   :noindex:

Methods
-------

.. automethod:: abjad.tools.ipythontools.Play.Play.load_sound_font
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.ipythontools.Play.Play.__call__
   :noindex:
