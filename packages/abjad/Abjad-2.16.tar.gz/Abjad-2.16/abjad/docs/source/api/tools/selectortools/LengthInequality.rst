selectortools.LengthInequality
==============================

.. autoclass:: abjad.tools.selectortools.LengthInequality.LengthInequality

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
           "selectortools.Inequality" [color=3,
               group=2,
               label=Inequality,
               shape=oval,
               style=bold];
           "selectortools.LengthInequality" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>LengthInequality</B>>,
               shape=box,
               style="filled, rounded"];
           "selectortools.Inequality" -> "selectortools.LengthInequality";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "selectortools.Inequality";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.selectortools.LengthInequality.LengthInequality.length
      ~abjad.tools.selectortools.LengthInequality.LengthInequality.operator_string
      ~abjad.tools.selectortools.LengthInequality.LengthInequality.__call__
      ~abjad.tools.selectortools.LengthInequality.LengthInequality.__copy__
      ~abjad.tools.selectortools.LengthInequality.LengthInequality.__eq__
      ~abjad.tools.selectortools.LengthInequality.LengthInequality.__format__
      ~abjad.tools.selectortools.LengthInequality.LengthInequality.__hash__
      ~abjad.tools.selectortools.LengthInequality.LengthInequality.__ne__
      ~abjad.tools.selectortools.LengthInequality.LengthInequality.__repr__

Bases
-----

- :py:class:`selectortools.Inequality <abjad.tools.selectortools.Inequality.Inequality>`

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.selectortools.LengthInequality.LengthInequality.length
   :noindex:

.. autoattribute:: abjad.tools.selectortools.LengthInequality.LengthInequality.operator_string
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.selectortools.LengthInequality.LengthInequality.__call__
   :noindex:

.. automethod:: abjad.tools.selectortools.LengthInequality.LengthInequality.__copy__
   :noindex:

.. automethod:: abjad.tools.selectortools.LengthInequality.LengthInequality.__eq__
   :noindex:

.. automethod:: abjad.tools.selectortools.LengthInequality.LengthInequality.__format__
   :noindex:

.. automethod:: abjad.tools.selectortools.LengthInequality.LengthInequality.__hash__
   :noindex:

.. automethod:: abjad.tools.selectortools.LengthInequality.LengthInequality.__ne__
   :noindex:

.. automethod:: abjad.tools.selectortools.LengthInequality.LengthInequality.__repr__
   :noindex:
