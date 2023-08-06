spannertools.Tie
================

.. autoclass:: abjad.tools.spannertools.Tie.Tie

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
           "spannertools.Tie" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Tie</B>>,
               shape=box,
               style="filled, rounded"];
           "spannertools.Spanner" -> "spannertools.Tie";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "spannertools.Spanner";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.spannertools.Tie.Tie.components
      ~abjad.tools.spannertools.Tie.Tie.direction
      ~abjad.tools.spannertools.Tie.Tie.name
      ~abjad.tools.spannertools.Tie.Tie.overrides
      ~abjad.tools.spannertools.Tie.Tie.use_messiaen_style_ties
      ~abjad.tools.spannertools.Tie.Tie.__contains__
      ~abjad.tools.spannertools.Tie.Tie.__copy__
      ~abjad.tools.spannertools.Tie.Tie.__eq__
      ~abjad.tools.spannertools.Tie.Tie.__format__
      ~abjad.tools.spannertools.Tie.Tie.__getitem__
      ~abjad.tools.spannertools.Tie.Tie.__hash__
      ~abjad.tools.spannertools.Tie.Tie.__len__
      ~abjad.tools.spannertools.Tie.Tie.__lt__
      ~abjad.tools.spannertools.Tie.Tie.__ne__
      ~abjad.tools.spannertools.Tie.Tie.__repr__

Bases
-----

- :py:class:`spannertools.Spanner <abjad.tools.spannertools.Spanner.Spanner>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.spannertools.Tie.Tie.components
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Tie.Tie.direction
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Tie.Tie.name
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Tie.Tie.overrides
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Tie.Tie.use_messiaen_style_ties
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.spannertools.Tie.Tie.__contains__
   :noindex:

.. automethod:: abjad.tools.spannertools.Tie.Tie.__copy__
   :noindex:

.. automethod:: abjad.tools.spannertools.Tie.Tie.__eq__
   :noindex:

.. automethod:: abjad.tools.spannertools.Tie.Tie.__format__
   :noindex:

.. automethod:: abjad.tools.spannertools.Tie.Tie.__getitem__
   :noindex:

.. automethod:: abjad.tools.spannertools.Tie.Tie.__hash__
   :noindex:

.. automethod:: abjad.tools.spannertools.Tie.Tie.__len__
   :noindex:

.. automethod:: abjad.tools.spannertools.Tie.Tie.__lt__
   :noindex:

.. automethod:: abjad.tools.spannertools.Tie.Tie.__ne__
   :noindex:

.. automethod:: abjad.tools.spannertools.Tie.Tie.__repr__
   :noindex:
