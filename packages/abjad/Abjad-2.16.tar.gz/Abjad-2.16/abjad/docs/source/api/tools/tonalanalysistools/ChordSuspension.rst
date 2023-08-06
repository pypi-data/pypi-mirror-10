tonalanalysistools.ChordSuspension
==================================

.. autoclass:: abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension

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
           "tonalanalysistools.ChordSuspension" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>ChordSuspension</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "tonalanalysistools.ChordSuspension";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.chord_name
      ~abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.figured_bass_pair
      ~abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.figured_bass_string
      ~abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.is_empty
      ~abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.start
      ~abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.stop
      ~abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.title_string
      ~abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.__eq__
      ~abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.__format__
      ~abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.__hash__
      ~abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.__ne__
      ~abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.__repr__
      ~abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.__str__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.chord_name
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.figured_bass_pair
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.figured_bass_string
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.is_empty
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.start
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.stop
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.title_string
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.__eq__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.__format__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.__hash__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.__ne__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.__repr__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ChordSuspension.ChordSuspension.__str__
   :noindex:
