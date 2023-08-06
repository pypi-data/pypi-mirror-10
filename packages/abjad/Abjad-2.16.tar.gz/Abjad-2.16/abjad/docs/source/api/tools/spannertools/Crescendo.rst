spannertools.Crescendo
======================

.. autoclass:: abjad.tools.spannertools.Crescendo.Crescendo

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
           "spannertools.Crescendo" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Crescendo</B>>,
               shape=box,
               style="filled, rounded"];
           "spannertools.Hairpin" [color=3,
               group=2,
               label=Hairpin,
               shape=box];
           "spannertools.Spanner" [color=3,
               group=2,
               label=Spanner,
               shape=box];
           "spannertools.Hairpin" -> "spannertools.Crescendo";
           "spannertools.Spanner" -> "spannertools.Hairpin";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "spannertools.Spanner";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.spannertools.Crescendo.Crescendo.components
      ~abjad.tools.spannertools.Crescendo.Crescendo.descriptor
      ~abjad.tools.spannertools.Crescendo.Crescendo.direction
      ~abjad.tools.spannertools.Crescendo.Crescendo.include_rests
      ~abjad.tools.spannertools.Crescendo.Crescendo.name
      ~abjad.tools.spannertools.Crescendo.Crescendo.overrides
      ~abjad.tools.spannertools.Crescendo.Crescendo.shape_string
      ~abjad.tools.spannertools.Crescendo.Crescendo.start_dynamic
      ~abjad.tools.spannertools.Crescendo.Crescendo.stop_dynamic
      ~abjad.tools.spannertools.Crescendo.Crescendo.__contains__
      ~abjad.tools.spannertools.Crescendo.Crescendo.__copy__
      ~abjad.tools.spannertools.Crescendo.Crescendo.__eq__
      ~abjad.tools.spannertools.Crescendo.Crescendo.__format__
      ~abjad.tools.spannertools.Crescendo.Crescendo.__getitem__
      ~abjad.tools.spannertools.Crescendo.Crescendo.__hash__
      ~abjad.tools.spannertools.Crescendo.Crescendo.__len__
      ~abjad.tools.spannertools.Crescendo.Crescendo.__lt__
      ~abjad.tools.spannertools.Crescendo.Crescendo.__ne__
      ~abjad.tools.spannertools.Crescendo.Crescendo.__repr__

Bases
-----

- :py:class:`spannertools.Hairpin <abjad.tools.spannertools.Hairpin.Hairpin>`

- :py:class:`spannertools.Spanner <abjad.tools.spannertools.Spanner.Spanner>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.spannertools.Crescendo.Crescendo.components
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Crescendo.Crescendo.descriptor
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Crescendo.Crescendo.direction
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Crescendo.Crescendo.include_rests
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Crescendo.Crescendo.name
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Crescendo.Crescendo.overrides
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Crescendo.Crescendo.shape_string
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Crescendo.Crescendo.start_dynamic
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Crescendo.Crescendo.stop_dynamic
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.spannertools.Crescendo.Crescendo.__contains__
   :noindex:

.. automethod:: abjad.tools.spannertools.Crescendo.Crescendo.__copy__
   :noindex:

.. automethod:: abjad.tools.spannertools.Crescendo.Crescendo.__eq__
   :noindex:

.. automethod:: abjad.tools.spannertools.Crescendo.Crescendo.__format__
   :noindex:

.. automethod:: abjad.tools.spannertools.Crescendo.Crescendo.__getitem__
   :noindex:

.. automethod:: abjad.tools.spannertools.Crescendo.Crescendo.__hash__
   :noindex:

.. automethod:: abjad.tools.spannertools.Crescendo.Crescendo.__len__
   :noindex:

.. automethod:: abjad.tools.spannertools.Crescendo.Crescendo.__lt__
   :noindex:

.. automethod:: abjad.tools.spannertools.Crescendo.Crescendo.__ne__
   :noindex:

.. automethod:: abjad.tools.spannertools.Crescendo.Crescendo.__repr__
   :noindex:
