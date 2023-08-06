spannertools.Hairpin
====================

.. autoclass:: abjad.tools.spannertools.Hairpin.Hairpin

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
           "spannertools.Crescendo" [color=3,
               group=2,
               label=Crescendo,
               shape=box];
           "spannertools.Decrescendo" [color=3,
               group=2,
               label=Decrescendo,
               shape=box];
           "spannertools.Hairpin" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Hairpin</B>>,
               shape=box,
               style="filled, rounded"];
           "spannertools.Spanner" [color=3,
               group=2,
               label=Spanner,
               shape=box];
           "spannertools.Hairpin" -> "spannertools.Crescendo";
           "spannertools.Hairpin" -> "spannertools.Decrescendo";
           "spannertools.Spanner" -> "spannertools.Hairpin";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "spannertools.Spanner";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.spannertools.Hairpin.Hairpin.components
      ~abjad.tools.spannertools.Hairpin.Hairpin.descriptor
      ~abjad.tools.spannertools.Hairpin.Hairpin.direction
      ~abjad.tools.spannertools.Hairpin.Hairpin.include_rests
      ~abjad.tools.spannertools.Hairpin.Hairpin.name
      ~abjad.tools.spannertools.Hairpin.Hairpin.overrides
      ~abjad.tools.spannertools.Hairpin.Hairpin.shape_string
      ~abjad.tools.spannertools.Hairpin.Hairpin.start_dynamic
      ~abjad.tools.spannertools.Hairpin.Hairpin.stop_dynamic
      ~abjad.tools.spannertools.Hairpin.Hairpin.__contains__
      ~abjad.tools.spannertools.Hairpin.Hairpin.__copy__
      ~abjad.tools.spannertools.Hairpin.Hairpin.__eq__
      ~abjad.tools.spannertools.Hairpin.Hairpin.__format__
      ~abjad.tools.spannertools.Hairpin.Hairpin.__getitem__
      ~abjad.tools.spannertools.Hairpin.Hairpin.__hash__
      ~abjad.tools.spannertools.Hairpin.Hairpin.__len__
      ~abjad.tools.spannertools.Hairpin.Hairpin.__lt__
      ~abjad.tools.spannertools.Hairpin.Hairpin.__ne__
      ~abjad.tools.spannertools.Hairpin.Hairpin.__repr__

Bases
-----

- :py:class:`spannertools.Spanner <abjad.tools.spannertools.Spanner.Spanner>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.spannertools.Hairpin.Hairpin.components
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Hairpin.Hairpin.descriptor
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Hairpin.Hairpin.direction
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Hairpin.Hairpin.include_rests
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Hairpin.Hairpin.name
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Hairpin.Hairpin.overrides
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Hairpin.Hairpin.shape_string
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Hairpin.Hairpin.start_dynamic
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Hairpin.Hairpin.stop_dynamic
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.spannertools.Hairpin.Hairpin.__contains__
   :noindex:

.. automethod:: abjad.tools.spannertools.Hairpin.Hairpin.__copy__
   :noindex:

.. automethod:: abjad.tools.spannertools.Hairpin.Hairpin.__eq__
   :noindex:

.. automethod:: abjad.tools.spannertools.Hairpin.Hairpin.__format__
   :noindex:

.. automethod:: abjad.tools.spannertools.Hairpin.Hairpin.__getitem__
   :noindex:

.. automethod:: abjad.tools.spannertools.Hairpin.Hairpin.__hash__
   :noindex:

.. automethod:: abjad.tools.spannertools.Hairpin.Hairpin.__len__
   :noindex:

.. automethod:: abjad.tools.spannertools.Hairpin.Hairpin.__lt__
   :noindex:

.. automethod:: abjad.tools.spannertools.Hairpin.Hairpin.__ne__
   :noindex:

.. automethod:: abjad.tools.spannertools.Hairpin.Hairpin.__repr__
   :noindex:
