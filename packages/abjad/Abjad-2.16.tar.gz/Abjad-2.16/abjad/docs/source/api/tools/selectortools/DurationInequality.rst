selectortools.DurationInequality
================================

.. autoclass:: abjad.tools.selectortools.DurationInequality.DurationInequality

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
           "selectortools.DurationInequality" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>DurationInequality</B>>,
               shape=box,
               style="filled, rounded"];
           "selectortools.Inequality" [color=3,
               group=2,
               label=Inequality,
               shape=oval,
               style=bold];
           "selectortools.Inequality" -> "selectortools.DurationInequality";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "selectortools.Inequality";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.selectortools.DurationInequality.DurationInequality.duration
      ~abjad.tools.selectortools.DurationInequality.DurationInequality.operator_string
      ~abjad.tools.selectortools.DurationInequality.DurationInequality.__call__
      ~abjad.tools.selectortools.DurationInequality.DurationInequality.__copy__
      ~abjad.tools.selectortools.DurationInequality.DurationInequality.__eq__
      ~abjad.tools.selectortools.DurationInequality.DurationInequality.__format__
      ~abjad.tools.selectortools.DurationInequality.DurationInequality.__hash__
      ~abjad.tools.selectortools.DurationInequality.DurationInequality.__ne__
      ~abjad.tools.selectortools.DurationInequality.DurationInequality.__repr__

Bases
-----

- :py:class:`selectortools.Inequality <abjad.tools.selectortools.Inequality.Inequality>`

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.selectortools.DurationInequality.DurationInequality.duration
   :noindex:

.. autoattribute:: abjad.tools.selectortools.DurationInequality.DurationInequality.operator_string
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.selectortools.DurationInequality.DurationInequality.__call__
   :noindex:

.. automethod:: abjad.tools.selectortools.DurationInequality.DurationInequality.__copy__
   :noindex:

.. automethod:: abjad.tools.selectortools.DurationInequality.DurationInequality.__eq__
   :noindex:

.. automethod:: abjad.tools.selectortools.DurationInequality.DurationInequality.__format__
   :noindex:

.. automethod:: abjad.tools.selectortools.DurationInequality.DurationInequality.__hash__
   :noindex:

.. automethod:: abjad.tools.selectortools.DurationInequality.DurationInequality.__ne__
   :noindex:

.. automethod:: abjad.tools.selectortools.DurationInequality.DurationInequality.__repr__
   :noindex:
