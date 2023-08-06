quantizationtools.QGrid
=======================

.. autoclass:: abjad.tools.quantizationtools.QGrid.QGrid

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
           "quantizationtools.QGrid" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>QGrid</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.QGrid";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.QGrid.QGrid.distance
      ~abjad.tools.quantizationtools.QGrid.QGrid.fit_q_events
      ~abjad.tools.quantizationtools.QGrid.QGrid.leaves
      ~abjad.tools.quantizationtools.QGrid.QGrid.next_downbeat
      ~abjad.tools.quantizationtools.QGrid.QGrid.offsets
      ~abjad.tools.quantizationtools.QGrid.QGrid.pretty_rtm_format
      ~abjad.tools.quantizationtools.QGrid.QGrid.root_node
      ~abjad.tools.quantizationtools.QGrid.QGrid.rtm_format
      ~abjad.tools.quantizationtools.QGrid.QGrid.sort_q_events_by_index
      ~abjad.tools.quantizationtools.QGrid.QGrid.subdivide_leaf
      ~abjad.tools.quantizationtools.QGrid.QGrid.subdivide_leaves
      ~abjad.tools.quantizationtools.QGrid.QGrid.__call__
      ~abjad.tools.quantizationtools.QGrid.QGrid.__copy__
      ~abjad.tools.quantizationtools.QGrid.QGrid.__eq__
      ~abjad.tools.quantizationtools.QGrid.QGrid.__format__
      ~abjad.tools.quantizationtools.QGrid.QGrid.__hash__
      ~abjad.tools.quantizationtools.QGrid.QGrid.__ne__
      ~abjad.tools.quantizationtools.QGrid.QGrid.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.QGrid.QGrid.distance
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGrid.QGrid.leaves
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGrid.QGrid.next_downbeat
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGrid.QGrid.offsets
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGrid.QGrid.pretty_rtm_format
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGrid.QGrid.root_node
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QGrid.QGrid.rtm_format
   :noindex:

Methods
-------

.. automethod:: abjad.tools.quantizationtools.QGrid.QGrid.fit_q_events
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QGrid.QGrid.sort_q_events_by_index
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QGrid.QGrid.subdivide_leaf
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QGrid.QGrid.subdivide_leaves
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.QGrid.QGrid.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QGrid.QGrid.__copy__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QGrid.QGrid.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QGrid.QGrid.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QGrid.QGrid.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QGrid.QGrid.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QGrid.QGrid.__repr__
   :noindex:
