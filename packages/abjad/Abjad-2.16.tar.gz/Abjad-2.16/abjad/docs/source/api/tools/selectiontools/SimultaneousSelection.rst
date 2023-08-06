selectiontools.SimultaneousSelection
====================================

.. autoclass:: abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection

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
           "selectiontools.Descendants" [color=2,
               group=1,
               label=Descendants,
               shape=box];
           "selectiontools.Lineage" [color=2,
               group=1,
               label=Lineage,
               shape=box];
           "selectiontools.Parentage" [color=2,
               group=1,
               label=Parentage,
               shape=box];
           "selectiontools.Selection" [color=2,
               group=1,
               label=Selection,
               shape=box];
           "selectiontools.SimultaneousSelection" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>SimultaneousSelection</B>>,
               shape=box,
               style="filled, rounded"];
           "selectiontools.VerticalMoment" [color=2,
               group=1,
               label=VerticalMoment,
               shape=box];
           "selectiontools.Selection" -> "selectiontools.SimultaneousSelection";
           "selectiontools.SimultaneousSelection" -> "selectiontools.Descendants";
           "selectiontools.SimultaneousSelection" -> "selectiontools.Lineage";
           "selectiontools.SimultaneousSelection" -> "selectiontools.Parentage";
           "selectiontools.SimultaneousSelection" -> "selectiontools.VerticalMoment";
       }
       "__builtin__.object" -> "selectiontools.Selection";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.get_duration
      ~abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.get_spanners
      ~abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.get_vertical_moment_at
      ~abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__add__
      ~abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__contains__
      ~abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__eq__
      ~abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__format__
      ~abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__getitem__
      ~abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__hash__
      ~abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__illustrate__
      ~abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__len__
      ~abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__ne__
      ~abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__radd__
      ~abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__repr__

Bases
-----

- :py:class:`selectiontools.Selection <abjad.tools.selectiontools.Selection.Selection>`

- :py:class:`__builtin__.object <object>`

Methods
-------

.. automethod:: abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.get_duration
   :noindex:

.. automethod:: abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.get_spanners
   :noindex:

.. automethod:: abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.get_vertical_moment_at
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__add__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__contains__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__eq__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__format__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__getitem__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__hash__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__illustrate__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__len__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__ne__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__radd__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection.__repr__
   :noindex:
