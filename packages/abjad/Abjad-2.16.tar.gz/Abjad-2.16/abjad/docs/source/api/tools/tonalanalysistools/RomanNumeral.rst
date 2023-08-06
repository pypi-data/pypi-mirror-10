tonalanalysistools.RomanNumeral
===============================

.. autoclass:: abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral

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
           "tonalanalysistools.RomanNumeral" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>RomanNumeral</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "tonalanalysistools.RomanNumeral";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.bass_scale_degree
      ~abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.extent
      ~abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.figured_bass_string
      ~abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.inversion
      ~abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.markup
      ~abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.quality
      ~abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.root_scale_degree
      ~abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.scale_degree
      ~abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.suspension
      ~abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.symbolic_string
      ~abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.__eq__
      ~abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.__format__
      ~abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.__hash__
      ~abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.__ne__
      ~abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.bass_scale_degree
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.extent
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.figured_bass_string
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.inversion
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.markup
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.quality
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.root_scale_degree
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.scale_degree
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.suspension
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.symbolic_string
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.__eq__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.__format__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.__hash__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.__ne__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.RomanNumeral.RomanNumeral.__repr__
   :noindex:
