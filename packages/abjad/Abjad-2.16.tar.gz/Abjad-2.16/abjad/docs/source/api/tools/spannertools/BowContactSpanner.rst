spannertools.BowContactSpanner
==============================

.. autoclass:: abjad.tools.spannertools.BowContactSpanner.BowContactSpanner

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
       subgraph cluster_spannertools {
           graph [label=spannertools];
           "spannertools.BowContactSpanner" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>BowContactSpanner</B>>,
               shape=box,
               style="filled, rounded"];
           "spannertools.Spanner" [color=3,
               group=2,
               label=Spanner,
               shape=box];
           "spannertools.Spanner" -> "spannertools.BowContactSpanner";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "spannertools.Spanner";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.components
      ~abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.name
      ~abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.overrides
      ~abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__contains__
      ~abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__copy__
      ~abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__eq__
      ~abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__format__
      ~abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__getitem__
      ~abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__hash__
      ~abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__len__
      ~abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__lt__
      ~abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__ne__
      ~abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__repr__

Bases
-----

- :py:class:`spannertools.Spanner <abjad.tools.spannertools.Spanner.Spanner>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.components
   :noindex:

.. autoattribute:: abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.name
   :noindex:

.. autoattribute:: abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.overrides
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__contains__
   :noindex:

.. automethod:: abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__copy__
   :noindex:

.. automethod:: abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__eq__
   :noindex:

.. automethod:: abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__format__
   :noindex:

.. automethod:: abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__getitem__
   :noindex:

.. automethod:: abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__hash__
   :noindex:

.. automethod:: abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__len__
   :noindex:

.. automethod:: abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__lt__
   :noindex:

.. automethod:: abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__ne__
   :noindex:

.. automethod:: abjad.tools.spannertools.BowContactSpanner.BowContactSpanner.__repr__
   :noindex:
