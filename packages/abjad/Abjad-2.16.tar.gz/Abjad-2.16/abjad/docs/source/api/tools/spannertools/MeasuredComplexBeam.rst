spannertools.MeasuredComplexBeam
================================

.. autoclass:: abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam

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
           "spannertools.Beam" [color=3,
               group=2,
               label=Beam,
               shape=box];
           "spannertools.ComplexBeam" [color=3,
               group=2,
               label=ComplexBeam,
               shape=box];
           "spannertools.MeasuredComplexBeam" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>MeasuredComplexBeam</B>>,
               shape=box,
               style="filled, rounded"];
           "spannertools.Spanner" [color=3,
               group=2,
               label=Spanner,
               shape=box];
           "spannertools.Beam" -> "spannertools.ComplexBeam";
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

      ~abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.components
      ~abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.direction
      ~abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.isolated_nib_direction
      ~abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.name
      ~abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.overrides
      ~abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.span_beam_count
      ~abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__contains__
      ~abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__copy__
      ~abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__eq__
      ~abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__format__
      ~abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__getitem__
      ~abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__hash__
      ~abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__len__
      ~abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__lt__
      ~abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__ne__
      ~abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__repr__

Bases
-----

- :py:class:`spannertools.ComplexBeam <abjad.tools.spannertools.ComplexBeam.ComplexBeam>`

- :py:class:`spannertools.Beam <abjad.tools.spannertools.Beam.Beam>`

- :py:class:`spannertools.Spanner <abjad.tools.spannertools.Spanner.Spanner>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.components
   :noindex:

.. autoattribute:: abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.direction
   :noindex:

.. autoattribute:: abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.isolated_nib_direction
   :noindex:

.. autoattribute:: abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.name
   :noindex:

.. autoattribute:: abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.overrides
   :noindex:

.. autoattribute:: abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.span_beam_count
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__contains__
   :noindex:

.. automethod:: abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__copy__
   :noindex:

.. automethod:: abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__eq__
   :noindex:

.. automethod:: abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__format__
   :noindex:

.. automethod:: abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__getitem__
   :noindex:

.. automethod:: abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__hash__
   :noindex:

.. automethod:: abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__len__
   :noindex:

.. automethod:: abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__lt__
   :noindex:

.. automethod:: abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__ne__
   :noindex:

.. automethod:: abjad.tools.spannertools.MeasuredComplexBeam.MeasuredComplexBeam.__repr__
   :noindex:
