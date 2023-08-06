tonalanalysistools.ScaleDegree
==============================

.. autoclass:: abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree

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
           "tonalanalysistools.ScaleDegree" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>ScaleDegree</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "tonalanalysistools.ScaleDegree";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.accidental
      ~abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.apply_accidental
      ~abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.name
      ~abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.number
      ~abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.roman_numeral_string
      ~abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.symbolic_string
      ~abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.title_string
      ~abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.__eq__
      ~abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.__format__
      ~abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.__hash__
      ~abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.__ne__
      ~abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.__repr__
      ~abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.__str__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.accidental
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.name
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.number
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.roman_numeral_string
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.symbolic_string
   :noindex:

.. autoattribute:: abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.title_string
   :noindex:

Methods
-------

.. automethod:: abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.apply_accidental
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.__eq__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.__format__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.__hash__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.__ne__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.__repr__
   :noindex:

.. automethod:: abjad.tools.tonalanalysistools.ScaleDegree.ScaleDegree.__str__
   :noindex:
