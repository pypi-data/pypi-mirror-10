spannertools.Decrescendo
========================

.. autoclass:: abjad.tools.spannertools.Decrescendo.Decrescendo

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
           "spannertools.Decrescendo" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Decrescendo</B>>,
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

      ~abjad.tools.spannertools.Decrescendo.Decrescendo.components
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.descriptor
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.direction
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.include_rests
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.name
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.overrides
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.shape_string
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.start_dynamic
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.stop_dynamic
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.__contains__
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.__copy__
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.__eq__
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.__format__
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.__getitem__
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.__hash__
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.__len__
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.__lt__
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.__ne__
      ~abjad.tools.spannertools.Decrescendo.Decrescendo.__repr__

Bases
-----

- :py:class:`spannertools.Hairpin <abjad.tools.spannertools.Hairpin.Hairpin>`

- :py:class:`spannertools.Spanner <abjad.tools.spannertools.Spanner.Spanner>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.spannertools.Decrescendo.Decrescendo.components
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Decrescendo.Decrescendo.descriptor
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Decrescendo.Decrescendo.direction
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Decrescendo.Decrescendo.include_rests
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Decrescendo.Decrescendo.name
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Decrescendo.Decrescendo.overrides
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Decrescendo.Decrescendo.shape_string
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Decrescendo.Decrescendo.start_dynamic
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Decrescendo.Decrescendo.stop_dynamic
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.spannertools.Decrescendo.Decrescendo.__contains__
   :noindex:

.. automethod:: abjad.tools.spannertools.Decrescendo.Decrescendo.__copy__
   :noindex:

.. automethod:: abjad.tools.spannertools.Decrescendo.Decrescendo.__eq__
   :noindex:

.. automethod:: abjad.tools.spannertools.Decrescendo.Decrescendo.__format__
   :noindex:

.. automethod:: abjad.tools.spannertools.Decrescendo.Decrescendo.__getitem__
   :noindex:

.. automethod:: abjad.tools.spannertools.Decrescendo.Decrescendo.__hash__
   :noindex:

.. automethod:: abjad.tools.spannertools.Decrescendo.Decrescendo.__len__
   :noindex:

.. automethod:: abjad.tools.spannertools.Decrescendo.Decrescendo.__lt__
   :noindex:

.. automethod:: abjad.tools.spannertools.Decrescendo.Decrescendo.__ne__
   :noindex:

.. automethod:: abjad.tools.spannertools.Decrescendo.Decrescendo.__repr__
   :noindex:
