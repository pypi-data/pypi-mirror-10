selectiontools.Parentage
========================

.. autoclass:: abjad.tools.selectiontools.Parentage.Parentage

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
           "selectiontools.Parentage" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>Parentage</B>>,
               shape=box,
               style="filled, rounded"];
           "selectiontools.Selection" [color=2,
               group=1,
               label=Selection,
               shape=box];
           "selectiontools.SimultaneousSelection" [color=2,
               group=1,
               label=SimultaneousSelection,
               shape=box];
           "selectiontools.Selection" -> "selectiontools.SimultaneousSelection";
           "selectiontools.SimultaneousSelection" -> "selectiontools.Parentage";
       }
       "__builtin__.object" -> "selectiontools.Selection";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.selectiontools.Parentage.Parentage.component
      ~abjad.tools.selectiontools.Parentage.Parentage.depth
      ~abjad.tools.selectiontools.Parentage.Parentage.get_duration
      ~abjad.tools.selectiontools.Parentage.Parentage.get_first
      ~abjad.tools.selectiontools.Parentage.Parentage.get_spanners
      ~abjad.tools.selectiontools.Parentage.Parentage.get_vertical_moment_at
      ~abjad.tools.selectiontools.Parentage.Parentage.is_orphan
      ~abjad.tools.selectiontools.Parentage.Parentage.logical_voice
      ~abjad.tools.selectiontools.Parentage.Parentage.parent
      ~abjad.tools.selectiontools.Parentage.Parentage.prolation
      ~abjad.tools.selectiontools.Parentage.Parentage.root
      ~abjad.tools.selectiontools.Parentage.Parentage.score_index
      ~abjad.tools.selectiontools.Parentage.Parentage.tuplet_depth
      ~abjad.tools.selectiontools.Parentage.Parentage.__add__
      ~abjad.tools.selectiontools.Parentage.Parentage.__contains__
      ~abjad.tools.selectiontools.Parentage.Parentage.__eq__
      ~abjad.tools.selectiontools.Parentage.Parentage.__format__
      ~abjad.tools.selectiontools.Parentage.Parentage.__getitem__
      ~abjad.tools.selectiontools.Parentage.Parentage.__hash__
      ~abjad.tools.selectiontools.Parentage.Parentage.__illustrate__
      ~abjad.tools.selectiontools.Parentage.Parentage.__len__
      ~abjad.tools.selectiontools.Parentage.Parentage.__ne__
      ~abjad.tools.selectiontools.Parentage.Parentage.__radd__
      ~abjad.tools.selectiontools.Parentage.Parentage.__repr__

Bases
-----

- :py:class:`selectiontools.SimultaneousSelection <abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection>`

- :py:class:`selectiontools.Selection <abjad.tools.selectiontools.Selection.Selection>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.selectiontools.Parentage.Parentage.component
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.Parentage.Parentage.depth
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.Parentage.Parentage.is_orphan
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.Parentage.Parentage.logical_voice
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.Parentage.Parentage.parent
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.Parentage.Parentage.prolation
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.Parentage.Parentage.root
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.Parentage.Parentage.score_index
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.Parentage.Parentage.tuplet_depth
   :noindex:

Methods
-------

.. automethod:: abjad.tools.selectiontools.Parentage.Parentage.get_duration
   :noindex:

.. automethod:: abjad.tools.selectiontools.Parentage.Parentage.get_first
   :noindex:

.. automethod:: abjad.tools.selectiontools.Parentage.Parentage.get_spanners
   :noindex:

.. automethod:: abjad.tools.selectiontools.Parentage.Parentage.get_vertical_moment_at
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.selectiontools.Parentage.Parentage.__add__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Parentage.Parentage.__contains__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Parentage.Parentage.__eq__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Parentage.Parentage.__format__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Parentage.Parentage.__getitem__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Parentage.Parentage.__hash__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Parentage.Parentage.__illustrate__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Parentage.Parentage.__len__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Parentage.Parentage.__ne__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Parentage.Parentage.__radd__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Parentage.Parentage.__repr__
   :noindex:
