quantizationtools.QTargetBeat
=============================

.. autoclass:: abjad.tools.quantizationtools.QTargetBeat.QTargetBeat

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
       subgraph cluster_quantizationtools {
           graph [label=quantizationtools];
           "quantizationtools.QTargetBeat" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>QTargetBeat</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.QTargetBeat";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.beatspan
      ~abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.distances
      ~abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.duration_in_ms
      ~abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.offset_in_ms
      ~abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.q_events
      ~abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.q_grid
      ~abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.q_grids
      ~abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.search_tree
      ~abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.tempo
      ~abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.__call__
      ~abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.__eq__
      ~abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.__format__
      ~abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.__hash__
      ~abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.__ne__
      ~abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.beatspan
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.distances
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.duration_in_ms
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.offset_in_ms
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.q_events
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.q_grid
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.q_grids
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.search_tree
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.tempo
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QTargetBeat.QTargetBeat.__repr__
   :noindex:
