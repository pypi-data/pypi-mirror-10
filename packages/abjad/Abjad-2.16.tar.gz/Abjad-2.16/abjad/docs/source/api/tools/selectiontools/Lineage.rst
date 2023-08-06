selectiontools.Lineage
======================

.. autoclass:: abjad.tools.selectiontools.Lineage.Lineage

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
           "selectiontools.Lineage" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>Lineage</B>>,
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
           "selectiontools.SimultaneousSelection" -> "selectiontools.Lineage";
       }
       "__builtin__.object" -> "selectiontools.Selection";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.selectiontools.Lineage.Lineage.component
      ~abjad.tools.selectiontools.Lineage.Lineage.get_duration
      ~abjad.tools.selectiontools.Lineage.Lineage.get_spanners
      ~abjad.tools.selectiontools.Lineage.Lineage.get_vertical_moment_at
      ~abjad.tools.selectiontools.Lineage.Lineage.__add__
      ~abjad.tools.selectiontools.Lineage.Lineage.__contains__
      ~abjad.tools.selectiontools.Lineage.Lineage.__eq__
      ~abjad.tools.selectiontools.Lineage.Lineage.__format__
      ~abjad.tools.selectiontools.Lineage.Lineage.__getitem__
      ~abjad.tools.selectiontools.Lineage.Lineage.__hash__
      ~abjad.tools.selectiontools.Lineage.Lineage.__illustrate__
      ~abjad.tools.selectiontools.Lineage.Lineage.__len__
      ~abjad.tools.selectiontools.Lineage.Lineage.__ne__
      ~abjad.tools.selectiontools.Lineage.Lineage.__radd__
      ~abjad.tools.selectiontools.Lineage.Lineage.__repr__

Bases
-----

- :py:class:`selectiontools.SimultaneousSelection <abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection>`

- :py:class:`selectiontools.Selection <abjad.tools.selectiontools.Selection.Selection>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.selectiontools.Lineage.Lineage.component
   :noindex:

Methods
-------

.. automethod:: abjad.tools.selectiontools.Lineage.Lineage.get_duration
   :noindex:

.. automethod:: abjad.tools.selectiontools.Lineage.Lineage.get_spanners
   :noindex:

.. automethod:: abjad.tools.selectiontools.Lineage.Lineage.get_vertical_moment_at
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.selectiontools.Lineage.Lineage.__add__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Lineage.Lineage.__contains__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Lineage.Lineage.__eq__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Lineage.Lineage.__format__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Lineage.Lineage.__getitem__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Lineage.Lineage.__hash__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Lineage.Lineage.__illustrate__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Lineage.Lineage.__len__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Lineage.Lineage.__ne__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Lineage.Lineage.__radd__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Lineage.Lineage.__repr__
   :noindex:
