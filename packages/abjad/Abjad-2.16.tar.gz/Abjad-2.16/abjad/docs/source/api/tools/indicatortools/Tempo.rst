indicatortools.Tempo
====================

.. autoclass:: abjad.tools.indicatortools.Tempo.Tempo

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
       subgraph cluster_indicatortools {
           graph [label=indicatortools];
           "indicatortools.Tempo" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Tempo</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "indicatortools.Tempo";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.indicatortools.Tempo.Tempo.duration
      ~abjad.tools.indicatortools.Tempo.Tempo.duration_to_milliseconds
      ~abjad.tools.indicatortools.Tempo.Tempo.is_imprecise
      ~abjad.tools.indicatortools.Tempo.Tempo.list_related_tempos
      ~abjad.tools.indicatortools.Tempo.Tempo.markup
      ~abjad.tools.indicatortools.Tempo.Tempo.quarters_per_minute
      ~abjad.tools.indicatortools.Tempo.Tempo.rewrite_duration
      ~abjad.tools.indicatortools.Tempo.Tempo.textual_indication
      ~abjad.tools.indicatortools.Tempo.Tempo.units_per_minute
      ~abjad.tools.indicatortools.Tempo.Tempo.__add__
      ~abjad.tools.indicatortools.Tempo.Tempo.__copy__
      ~abjad.tools.indicatortools.Tempo.Tempo.__div__
      ~abjad.tools.indicatortools.Tempo.Tempo.__eq__
      ~abjad.tools.indicatortools.Tempo.Tempo.__format__
      ~abjad.tools.indicatortools.Tempo.Tempo.__ge__
      ~abjad.tools.indicatortools.Tempo.Tempo.__gt__
      ~abjad.tools.indicatortools.Tempo.Tempo.__hash__
      ~abjad.tools.indicatortools.Tempo.Tempo.__le__
      ~abjad.tools.indicatortools.Tempo.Tempo.__lt__
      ~abjad.tools.indicatortools.Tempo.Tempo.__mul__
      ~abjad.tools.indicatortools.Tempo.Tempo.__ne__
      ~abjad.tools.indicatortools.Tempo.Tempo.__repr__
      ~abjad.tools.indicatortools.Tempo.Tempo.__rmul__
      ~abjad.tools.indicatortools.Tempo.Tempo.__str__
      ~abjad.tools.indicatortools.Tempo.Tempo.__sub__
      ~abjad.tools.indicatortools.Tempo.Tempo.__truediv__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.indicatortools.Tempo.Tempo.duration
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Tempo.Tempo.is_imprecise
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Tempo.Tempo.markup
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Tempo.Tempo.quarters_per_minute
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Tempo.Tempo.textual_indication
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Tempo.Tempo.units_per_minute
   :noindex:

Methods
-------

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.duration_to_milliseconds
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.list_related_tempos
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.rewrite_duration
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.__add__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.__copy__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.__div__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.__eq__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.__format__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.__ge__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.__gt__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.__hash__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.__le__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.__lt__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.__mul__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.__ne__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.__repr__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.__rmul__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.__str__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.__sub__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Tempo.Tempo.__truediv__
   :noindex:
