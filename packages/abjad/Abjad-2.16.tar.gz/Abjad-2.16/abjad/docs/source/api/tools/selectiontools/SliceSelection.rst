selectiontools.SliceSelection
=============================

.. autoclass:: abjad.tools.selectiontools.SliceSelection.SliceSelection

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
           "selectiontools.ContiguousSelection" [color=2,
               group=1,
               label=ContiguousSelection,
               shape=box];
           "selectiontools.Selection" [color=2,
               group=1,
               label=Selection,
               shape=box];
           "selectiontools.SliceSelection" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>SliceSelection</B>>,
               shape=box,
               style="filled, rounded"];
           "selectiontools.ContiguousSelection" -> "selectiontools.SliceSelection";
           "selectiontools.Selection" -> "selectiontools.ContiguousSelection";
       }
       "__builtin__.object" -> "selectiontools.Selection";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.get_duration
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.get_spanners
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.get_timespan
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.group_by
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.partition_by_durations
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.partition_by_durations_exactly
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.partition_by_durations_not_greater_than
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.partition_by_durations_not_less_than
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.__add__
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.__contains__
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.__eq__
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.__format__
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.__getitem__
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.__hash__
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.__illustrate__
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.__len__
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.__ne__
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.__radd__
      ~abjad.tools.selectiontools.SliceSelection.SliceSelection.__repr__

Bases
-----

- :py:class:`selectiontools.ContiguousSelection <abjad.tools.selectiontools.ContiguousSelection.ContiguousSelection>`

- :py:class:`selectiontools.Selection <abjad.tools.selectiontools.Selection.Selection>`

- :py:class:`__builtin__.object <object>`

Methods
-------

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.get_duration
   :noindex:

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.get_spanners
   :noindex:

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.get_timespan
   :noindex:

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.group_by
   :noindex:

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.partition_by_durations
   :noindex:

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.partition_by_durations_exactly
   :noindex:

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.partition_by_durations_not_greater_than
   :noindex:

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.partition_by_durations_not_less_than
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.__add__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.__contains__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.__eq__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.__format__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.__getitem__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.__hash__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.__illustrate__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.__len__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.__ne__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.__radd__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SliceSelection.SliceSelection.__repr__
   :noindex:
