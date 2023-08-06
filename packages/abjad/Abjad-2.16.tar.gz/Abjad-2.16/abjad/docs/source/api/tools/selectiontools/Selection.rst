selectiontools.Selection
========================

.. autoclass:: abjad.tools.selectiontools.Selection.Selection

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
           "selectiontools.Descendants" [color=2,
               group=1,
               label=Descendants,
               shape=box];
           "selectiontools.Lineage" [color=2,
               group=1,
               label=Lineage,
               shape=box];
           "selectiontools.LogicalTie" [color=2,
               group=1,
               label=LogicalTie,
               shape=box];
           "selectiontools.Parentage" [color=2,
               group=1,
               label=Parentage,
               shape=box];
           "selectiontools.Selection" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>Selection</B>>,
               shape=box,
               style="filled, rounded"];
           "selectiontools.SimultaneousSelection" [color=2,
               group=1,
               label=SimultaneousSelection,
               shape=box];
           "selectiontools.SliceSelection" [color=2,
               group=1,
               label=SliceSelection,
               shape=box];
           "selectiontools.VerticalMoment" [color=2,
               group=1,
               label=VerticalMoment,
               shape=box];
           "selectiontools.ContiguousSelection" -> "selectiontools.LogicalTie";
           "selectiontools.ContiguousSelection" -> "selectiontools.SliceSelection";
           "selectiontools.Selection" -> "selectiontools.ContiguousSelection";
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

      ~abjad.tools.selectiontools.Selection.Selection.get_duration
      ~abjad.tools.selectiontools.Selection.Selection.get_spanners
      ~abjad.tools.selectiontools.Selection.Selection.__add__
      ~abjad.tools.selectiontools.Selection.Selection.__contains__
      ~abjad.tools.selectiontools.Selection.Selection.__eq__
      ~abjad.tools.selectiontools.Selection.Selection.__format__
      ~abjad.tools.selectiontools.Selection.Selection.__getitem__
      ~abjad.tools.selectiontools.Selection.Selection.__hash__
      ~abjad.tools.selectiontools.Selection.Selection.__illustrate__
      ~abjad.tools.selectiontools.Selection.Selection.__len__
      ~abjad.tools.selectiontools.Selection.Selection.__ne__
      ~abjad.tools.selectiontools.Selection.Selection.__radd__
      ~abjad.tools.selectiontools.Selection.Selection.__repr__

Bases
-----

- :py:class:`__builtin__.object <object>`

Methods
-------

.. automethod:: abjad.tools.selectiontools.Selection.Selection.get_duration
   :noindex:

.. automethod:: abjad.tools.selectiontools.Selection.Selection.get_spanners
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.selectiontools.Selection.Selection.__add__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Selection.Selection.__contains__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Selection.Selection.__eq__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Selection.Selection.__format__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Selection.Selection.__getitem__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Selection.Selection.__hash__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Selection.Selection.__illustrate__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Selection.Selection.__len__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Selection.Selection.__ne__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Selection.Selection.__radd__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Selection.Selection.__repr__
   :noindex:
