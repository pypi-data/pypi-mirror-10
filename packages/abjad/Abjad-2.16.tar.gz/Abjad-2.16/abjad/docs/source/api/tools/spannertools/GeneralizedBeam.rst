spannertools.GeneralizedBeam
============================

.. autoclass:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam

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
           "spannertools.GeneralizedBeam" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>GeneralizedBeam</B>>,
               shape=box,
               style="filled, rounded"];
           "spannertools.Spanner" [color=3,
               group=2,
               label=Spanner,
               shape=box];
           "spannertools.Spanner" -> "spannertools.GeneralizedBeam";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "spannertools.Spanner";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.components
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.durations
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.include_long_duration_notes
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.include_long_duration_rests
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.isolated_nib_direction
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.name
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.overrides
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.use_stemlets
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.vertical_direction
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__contains__
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__copy__
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__eq__
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__format__
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__getitem__
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__hash__
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__len__
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__lt__
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__ne__
      ~abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__repr__

Bases
-----

- :py:class:`spannertools.Spanner <abjad.tools.spannertools.Spanner.Spanner>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.components
   :noindex:

.. autoattribute:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.durations
   :noindex:

.. autoattribute:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.include_long_duration_notes
   :noindex:

.. autoattribute:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.include_long_duration_rests
   :noindex:

.. autoattribute:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.isolated_nib_direction
   :noindex:

.. autoattribute:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.name
   :noindex:

.. autoattribute:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.overrides
   :noindex:

.. autoattribute:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.use_stemlets
   :noindex:

.. autoattribute:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.vertical_direction
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__contains__
   :noindex:

.. automethod:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__copy__
   :noindex:

.. automethod:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__eq__
   :noindex:

.. automethod:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__format__
   :noindex:

.. automethod:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__getitem__
   :noindex:

.. automethod:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__hash__
   :noindex:

.. automethod:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__len__
   :noindex:

.. automethod:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__lt__
   :noindex:

.. automethod:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__ne__
   :noindex:

.. automethod:: abjad.tools.spannertools.GeneralizedBeam.GeneralizedBeam.__repr__
   :noindex:
