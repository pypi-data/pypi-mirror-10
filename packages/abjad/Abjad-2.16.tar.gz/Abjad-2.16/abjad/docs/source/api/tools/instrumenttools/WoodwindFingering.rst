instrumenttools.WoodwindFingering
=================================

.. autoclass:: abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering

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
       subgraph cluster_instrumenttools {
           graph [label=instrumenttools];
           "instrumenttools.WoodwindFingering" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>WoodwindFingering</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "instrumenttools.WoodwindFingering";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.center_column
      ~abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.instrument_name
      ~abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.left_hand
      ~abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.print_guide
      ~abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.right_hand
      ~abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.__call__
      ~abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.__eq__
      ~abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.__format__
      ~abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.__hash__
      ~abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.__ne__
      ~abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.center_column
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.instrument_name
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.left_hand
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.right_hand
   :noindex:

Methods
-------

.. automethod:: abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.print_guide
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.__call__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.__eq__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.__format__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.__hash__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.__ne__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.WoodwindFingering.WoodwindFingering.__repr__
   :noindex:
