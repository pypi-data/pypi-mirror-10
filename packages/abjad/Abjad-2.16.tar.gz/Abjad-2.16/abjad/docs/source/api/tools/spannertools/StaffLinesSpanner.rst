spannertools.StaffLinesSpanner
==============================

.. autoclass:: abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner

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
           "spannertools.Spanner" [color=3,
               group=2,
               label=Spanner,
               shape=box];
           "spannertools.StaffLinesSpanner" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>StaffLinesSpanner</B>>,
               shape=box,
               style="filled, rounded"];
           "spannertools.Spanner" -> "spannertools.StaffLinesSpanner";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "spannertools.Spanner";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.components
      ~abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.forbid_restarting
      ~abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.lines
      ~abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.name
      ~abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.overrides
      ~abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__contains__
      ~abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__copy__
      ~abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__eq__
      ~abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__format__
      ~abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__getitem__
      ~abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__hash__
      ~abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__len__
      ~abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__lt__
      ~abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__ne__
      ~abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__repr__

Bases
-----

- :py:class:`spannertools.Spanner <abjad.tools.spannertools.Spanner.Spanner>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.components
   :noindex:

.. autoattribute:: abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.forbid_restarting
   :noindex:

.. autoattribute:: abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.lines
   :noindex:

.. autoattribute:: abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.name
   :noindex:

.. autoattribute:: abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.overrides
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__contains__
   :noindex:

.. automethod:: abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__copy__
   :noindex:

.. automethod:: abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__eq__
   :noindex:

.. automethod:: abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__format__
   :noindex:

.. automethod:: abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__getitem__
   :noindex:

.. automethod:: abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__hash__
   :noindex:

.. automethod:: abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__len__
   :noindex:

.. automethod:: abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__lt__
   :noindex:

.. automethod:: abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__ne__
   :noindex:

.. automethod:: abjad.tools.spannertools.StaffLinesSpanner.StaffLinesSpanner.__repr__
   :noindex:
