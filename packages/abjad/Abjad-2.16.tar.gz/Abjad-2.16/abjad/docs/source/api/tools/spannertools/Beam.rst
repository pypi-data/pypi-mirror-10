spannertools.Beam
=================

.. autoclass:: abjad.tools.spannertools.Beam.Beam

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
           "spannertools.Beam" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Beam</B>>,
               shape=box,
               style="filled, rounded"];
           "spannertools.ComplexBeam" [color=3,
               group=2,
               label=ComplexBeam,
               shape=box];
           "spannertools.DuratedComplexBeam" [color=3,
               group=2,
               label=DuratedComplexBeam,
               shape=box];
           "spannertools.MeasuredComplexBeam" [color=3,
               group=2,
               label=MeasuredComplexBeam,
               shape=box];
           "spannertools.MultipartBeam" [color=3,
               group=2,
               label=MultipartBeam,
               shape=box];
           "spannertools.Spanner" [color=3,
               group=2,
               label=Spanner,
               shape=box];
           "spannertools.Beam" -> "spannertools.ComplexBeam";
           "spannertools.Beam" -> "spannertools.MultipartBeam";
           "spannertools.ComplexBeam" -> "spannertools.DuratedComplexBeam";
           "spannertools.ComplexBeam" -> "spannertools.MeasuredComplexBeam";
           "spannertools.Spanner" -> "spannertools.Beam";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "spannertools.Spanner";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.spannertools.Beam.Beam.components
      ~abjad.tools.spannertools.Beam.Beam.direction
      ~abjad.tools.spannertools.Beam.Beam.name
      ~abjad.tools.spannertools.Beam.Beam.overrides
      ~abjad.tools.spannertools.Beam.Beam.__contains__
      ~abjad.tools.spannertools.Beam.Beam.__copy__
      ~abjad.tools.spannertools.Beam.Beam.__eq__
      ~abjad.tools.spannertools.Beam.Beam.__format__
      ~abjad.tools.spannertools.Beam.Beam.__getitem__
      ~abjad.tools.spannertools.Beam.Beam.__hash__
      ~abjad.tools.spannertools.Beam.Beam.__len__
      ~abjad.tools.spannertools.Beam.Beam.__lt__
      ~abjad.tools.spannertools.Beam.Beam.__ne__
      ~abjad.tools.spannertools.Beam.Beam.__repr__

Bases
-----

- :py:class:`spannertools.Spanner <abjad.tools.spannertools.Spanner.Spanner>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.spannertools.Beam.Beam.components
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Beam.Beam.direction
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Beam.Beam.name
   :noindex:

.. autoattribute:: abjad.tools.spannertools.Beam.Beam.overrides
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.spannertools.Beam.Beam.__contains__
   :noindex:

.. automethod:: abjad.tools.spannertools.Beam.Beam.__copy__
   :noindex:

.. automethod:: abjad.tools.spannertools.Beam.Beam.__eq__
   :noindex:

.. automethod:: abjad.tools.spannertools.Beam.Beam.__format__
   :noindex:

.. automethod:: abjad.tools.spannertools.Beam.Beam.__getitem__
   :noindex:

.. automethod:: abjad.tools.spannertools.Beam.Beam.__hash__
   :noindex:

.. automethod:: abjad.tools.spannertools.Beam.Beam.__len__
   :noindex:

.. automethod:: abjad.tools.spannertools.Beam.Beam.__lt__
   :noindex:

.. automethod:: abjad.tools.spannertools.Beam.Beam.__ne__
   :noindex:

.. automethod:: abjad.tools.spannertools.Beam.Beam.__repr__
   :noindex:
