tonalanalysistools.ChordInversion
=================================

.. autoclass:: abjad.tools.tonalanalysistools.ChordInversion.ChordInversion

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
       subgraph cluster_tonalanalysistools {
           graph [label=tonalanalysistools];
           "tonalanalysistools.ChordInversion" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>ChordInversion</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "tonalanalysistools.ChordInversion";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.extent_to_figured_bass_string
      ~abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.name
      ~abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.number
      ~abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.title
      ~abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.__eq__
      ~abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.__format__
      ~abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.__hash__
      ~abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.__ne__
      ~abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.name
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.number
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.title
   :noindex:

Methods
-------

.. automethod:: abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.extent_to_figured_bass_string
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.__eq__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.__format__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.__hash__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.__ne__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ChordInversion.ChordInversion.__repr__
   :noindex:
