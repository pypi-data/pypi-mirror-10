spannertools.TrillSpanner
=========================

.. autoclass:: abjad.tools.spannertools.TrillSpanner.TrillSpanner

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
           "spannertools.TrillSpanner" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>TrillSpanner</B>>,
               shape=box,
               style="filled, rounded"];
           "spannertools.Spanner" -> "spannertools.TrillSpanner";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "spannertools.Spanner";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.spannertools.TrillSpanner.TrillSpanner.components
      ~abjad.tools.spannertools.TrillSpanner.TrillSpanner.interval
      ~abjad.tools.spannertools.TrillSpanner.TrillSpanner.is_harmonic
      ~abjad.tools.spannertools.TrillSpanner.TrillSpanner.name
      ~abjad.tools.spannertools.TrillSpanner.TrillSpanner.overrides
      ~abjad.tools.spannertools.TrillSpanner.TrillSpanner.pitch
      ~abjad.tools.spannertools.TrillSpanner.TrillSpanner.written_pitch
      ~abjad.tools.spannertools.TrillSpanner.TrillSpanner.__contains__
      ~abjad.tools.spannertools.TrillSpanner.TrillSpanner.__copy__
      ~abjad.tools.spannertools.TrillSpanner.TrillSpanner.__eq__
      ~abjad.tools.spannertools.TrillSpanner.TrillSpanner.__format__
      ~abjad.tools.spannertools.TrillSpanner.TrillSpanner.__getitem__
      ~abjad.tools.spannertools.TrillSpanner.TrillSpanner.__hash__
      ~abjad.tools.spannertools.TrillSpanner.TrillSpanner.__len__
      ~abjad.tools.spannertools.TrillSpanner.TrillSpanner.__lt__
      ~abjad.tools.spannertools.TrillSpanner.TrillSpanner.__ne__
      ~abjad.tools.spannertools.TrillSpanner.TrillSpanner.__repr__

Bases
-----

- :py:class:`spannertools.Spanner <abjad.tools.spannertools.Spanner.Spanner>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.spannertools.TrillSpanner.TrillSpanner.components
   :noindex:

.. autoattribute:: abjad.tools.spannertools.TrillSpanner.TrillSpanner.interval
   :noindex:

.. autoattribute:: abjad.tools.spannertools.TrillSpanner.TrillSpanner.is_harmonic
   :noindex:

.. autoattribute:: abjad.tools.spannertools.TrillSpanner.TrillSpanner.name
   :noindex:

.. autoattribute:: abjad.tools.spannertools.TrillSpanner.TrillSpanner.overrides
   :noindex:

.. autoattribute:: abjad.tools.spannertools.TrillSpanner.TrillSpanner.pitch
   :noindex:

.. autoattribute:: abjad.tools.spannertools.TrillSpanner.TrillSpanner.written_pitch
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.spannertools.TrillSpanner.TrillSpanner.__contains__
   :noindex:

.. automethod:: abjad.tools.spannertools.TrillSpanner.TrillSpanner.__copy__
   :noindex:

.. automethod:: abjad.tools.spannertools.TrillSpanner.TrillSpanner.__eq__
   :noindex:

.. automethod:: abjad.tools.spannertools.TrillSpanner.TrillSpanner.__format__
   :noindex:

.. automethod:: abjad.tools.spannertools.TrillSpanner.TrillSpanner.__getitem__
   :noindex:

.. automethod:: abjad.tools.spannertools.TrillSpanner.TrillSpanner.__hash__
   :noindex:

.. automethod:: abjad.tools.spannertools.TrillSpanner.TrillSpanner.__len__
   :noindex:

.. automethod:: abjad.tools.spannertools.TrillSpanner.TrillSpanner.__lt__
   :noindex:

.. automethod:: abjad.tools.spannertools.TrillSpanner.TrillSpanner.__ne__
   :noindex:

.. automethod:: abjad.tools.spannertools.TrillSpanner.TrillSpanner.__repr__
   :noindex:
