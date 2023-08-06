tonalanalysistools.ChordQuality
===============================

.. autoclass:: abjad.tools.tonalanalysistools.ChordQuality.ChordQuality

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
           "tonalanalysistools.ChordQuality" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>ChordQuality</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "tonalanalysistools.ChordQuality";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.tonalanalysistools.ChordQuality.ChordQuality.is_uppercase
      ~abjad.tools.tonalanalysistools.ChordQuality.ChordQuality.quality_string
      ~abjad.tools.tonalanalysistools.ChordQuality.ChordQuality.__eq__
      ~abjad.tools.tonalanalysistools.ChordQuality.ChordQuality.__format__
      ~abjad.tools.tonalanalysistools.ChordQuality.ChordQuality.__hash__
      ~abjad.tools.tonalanalysistools.ChordQuality.ChordQuality.__ne__
      ~abjad.tools.tonalanalysistools.ChordQuality.ChordQuality.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.tonalanalysistools.ChordQuality.ChordQuality.is_uppercase
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.ChordQuality.ChordQuality.quality_string
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.tonalanalysistools.ChordQuality.ChordQuality.__eq__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ChordQuality.ChordQuality.__format__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ChordQuality.ChordQuality.__hash__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ChordQuality.ChordQuality.__ne__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ChordQuality.ChordQuality.__repr__
   :noindex:
