selectiontools.VerticalMoment
=============================

.. autoclass:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment

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
           "selectiontools.Selection" [color=2,
               group=1,
               label=Selection,
               shape=box];
           "selectiontools.SimultaneousSelection" [color=2,
               group=1,
               label=SimultaneousSelection,
               shape=box];
           "selectiontools.VerticalMoment" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>VerticalMoment</B>>,
               shape=box,
               style="filled, rounded"];
           "selectiontools.Selection" -> "selectiontools.SimultaneousSelection";
           "selectiontools.SimultaneousSelection" -> "selectiontools.VerticalMoment";
       }
       "__builtin__.object" -> "selectiontools.Selection";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.attack_count
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.components
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.get_duration
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.get_spanners
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.get_vertical_moment_at
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.governors
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.leaves
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.measures
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.music
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.next_vertical_moment
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.notes
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.notes_and_chords
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.offset
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.overlap_components
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.overlap_leaves
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.overlap_measures
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.overlap_notes
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.previous_vertical_moment
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.start_components
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.start_leaves
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.start_notes
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__add__
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__contains__
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__eq__
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__format__
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__getitem__
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__hash__
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__illustrate__
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__len__
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__ne__
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__radd__
      ~abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__repr__

Bases
-----

- :py:class:`selectiontools.SimultaneousSelection <abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection>`

- :py:class:`selectiontools.Selection <abjad.tools.selectiontools.Selection.Selection>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.attack_count
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.components
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.governors
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.leaves
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.measures
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.music
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.next_vertical_moment
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.notes
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.notes_and_chords
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.offset
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.overlap_components
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.overlap_leaves
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.overlap_measures
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.overlap_notes
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.previous_vertical_moment
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.start_components
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.start_leaves
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.start_notes
   :noindex:

Methods
-------

.. automethod:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.get_duration
   :noindex:

.. automethod:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.get_spanners
   :noindex:

.. automethod:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.get_vertical_moment_at
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__add__
   :noindex:

.. automethod:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__contains__
   :noindex:

.. automethod:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__eq__
   :noindex:

.. automethod:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__format__
   :noindex:

.. automethod:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__getitem__
   :noindex:

.. automethod:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__hash__
   :noindex:

.. automethod:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__illustrate__
   :noindex:

.. automethod:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__len__
   :noindex:

.. automethod:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__ne__
   :noindex:

.. automethod:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__radd__
   :noindex:

.. automethod:: abjad.tools.selectiontools.VerticalMoment.VerticalMoment.__repr__
   :noindex:
