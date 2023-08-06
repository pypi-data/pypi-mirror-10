selectortools.Inequality
========================

.. autoclass:: abjad.tools.selectortools.Inequality.Inequality

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
           "abctools.AbjadValueObject" [color=2,
               group=1,
               label=AbjadValueObject,
               shape=box];
           "abctools.AbjadObject" -> "abctools.AbjadValueObject";
           "abctools.AbjadObject.AbstractBase" -> "abctools.AbjadObject";
       }
       subgraph cluster_selectortools {
           graph [label=selectortools];
           "selectortools.DurationInequality" [color=3,
               group=2,
               label=DurationInequality,
               shape=box];
           "selectortools.Inequality" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Inequality</B>>,
               shape=oval,
               style="filled, rounded"];
           "selectortools.LengthInequality" [color=3,
               group=2,
               label=LengthInequality,
               shape=box];
           "selectortools.Inequality" -> "selectortools.DurationInequality";
           "selectortools.Inequality" -> "selectortools.LengthInequality";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "selectortools.Inequality";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.selectortools.Inequality.Inequality.operator_string
      ~abjad.tools.selectortools.Inequality.Inequality.__call__
      ~abjad.tools.selectortools.Inequality.Inequality.__copy__
      ~abjad.tools.selectortools.Inequality.Inequality.__eq__
      ~abjad.tools.selectortools.Inequality.Inequality.__format__
      ~abjad.tools.selectortools.Inequality.Inequality.__hash__
      ~abjad.tools.selectortools.Inequality.Inequality.__ne__
      ~abjad.tools.selectortools.Inequality.Inequality.__repr__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.selectortools.Inequality.Inequality.operator_string
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.selectortools.Inequality.Inequality.__call__
   :noindex:

.. automethod:: abjad.tools.selectortools.Inequality.Inequality.__copy__
   :noindex:

.. automethod:: abjad.tools.selectortools.Inequality.Inequality.__eq__
   :noindex:

.. automethod:: abjad.tools.selectortools.Inequality.Inequality.__format__
   :noindex:

.. automethod:: abjad.tools.selectortools.Inequality.Inequality.__hash__
   :noindex:

.. automethod:: abjad.tools.selectortools.Inequality.Inequality.__ne__
   :noindex:

.. automethod:: abjad.tools.selectortools.Inequality.Inequality.__repr__
   :noindex:
