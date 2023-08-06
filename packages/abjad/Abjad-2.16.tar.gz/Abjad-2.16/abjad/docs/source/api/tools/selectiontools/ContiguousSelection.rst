selectiontools.ContiguousSelection
==================================

.. autoclass:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection

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
       subgraph cluster_selectiontools {
           graph [label=selectiontools];
           "selectiontools.ContiguousSelection" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>ContiguousSelection</B>>,
               shape=box,
               style="filled, rounded"];
           "selectiontools.LogicalTie" [color=2,
               group=1,
               label=LogicalTie,
               shape=box];
           "selectiontools.Selection" [color=2,
               group=1,
               label=Selection,
               shape=box];
           "selectiontools.SliceSelection" [color=2,
               group=1,
               label=SliceSelection,
               shape=box];
           "selectiontools.ContiguousSelection" -> "selectiontools.LogicalTie";
           "selectiontools.ContiguousSelection" -> "selectiontools.SliceSelection";
           "selectiontools.Selection" -> "selectiontools.ContiguousSelection";
       }
       "__builtin__.object" -> "selectiontools.Selection";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.get_duration
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.get_spanners
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.get_timespan
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.group_by
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.partition_by_durations
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.partition_by_durations_exactly
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.partition_by_durations_not_greater_than
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.partition_by_durations_not_less_than
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__add__
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__contains__
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__eq__
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__format__
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__getitem__
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__hash__
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__illustrate__
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__len__
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__ne__
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__radd__
      ~abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__repr__

Bases
-----

- :py:class:`selectiontools.Selection <abjad.tools.selectiontools.Selection.Selection>`

- :py:class:`__builtin__.object <object>`

Methods
-------

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.get_duration
   :noindex:

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.get_spanners
   :noindex:

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.get_timespan
   :noindex:

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.group_by
   :noindex:

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.partition_by_durations
   :noindex:

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.partition_by_durations_exactly
   :noindex:

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.partition_by_durations_not_greater_than
   :noindex:

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.partition_by_durations_not_less_than
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__add__
   :noindex:

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__contains__
   :noindex:

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__eq__
   :noindex:

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__format__
   :noindex:

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__getitem__
   :noindex:

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__hash__
   :noindex:

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__illustrate__
   :noindex:

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__len__
   :noindex:

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__ne__
   :noindex:

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__radd__
   :noindex:

.. automethod:: abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection.__repr__
   :noindex:
