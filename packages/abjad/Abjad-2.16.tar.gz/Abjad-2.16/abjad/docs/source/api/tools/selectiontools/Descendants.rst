selectiontools.Descendants
==========================

.. autoclass:: abjad.tools.selectiontools.Descendants.Descendants

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
           "selectiontools.Descendants" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>Descendants</B>>,
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
           "selectiontools.SimultaneousSelection" -> "selectiontools.Descendants";
       }
       "__builtin__.object" -> "selectiontools.Selection";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.selectiontools.Descendants.Descendants.component
      ~abjad.tools.selectiontools.Descendants.Descendants.get_duration
      ~abjad.tools.selectiontools.Descendants.Descendants.get_spanners
      ~abjad.tools.selectiontools.Descendants.Descendants.get_vertical_moment_at
      ~abjad.tools.selectiontools.Descendants.Descendants.__add__
      ~abjad.tools.selectiontools.Descendants.Descendants.__contains__
      ~abjad.tools.selectiontools.Descendants.Descendants.__eq__
      ~abjad.tools.selectiontools.Descendants.Descendants.__format__
      ~abjad.tools.selectiontools.Descendants.Descendants.__getitem__
      ~abjad.tools.selectiontools.Descendants.Descendants.__hash__
      ~abjad.tools.selectiontools.Descendants.Descendants.__illustrate__
      ~abjad.tools.selectiontools.Descendants.Descendants.__len__
      ~abjad.tools.selectiontools.Descendants.Descendants.__ne__
      ~abjad.tools.selectiontools.Descendants.Descendants.__radd__
      ~abjad.tools.selectiontools.Descendants.Descendants.__repr__

Bases
-----

- :py:class:`selectiontools.SimultaneousSelection <abjad.tools.selectiontools.SimultaneousSelection.SimultaneousSelection>`

- :py:class:`selectiontools.Selection <abjad.tools.selectiontools.Selection.Selection>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.selectiontools.Descendants.Descendants.component
   :noindex:

Methods
-------

.. automethod:: abjad.tools.selectiontools.Descendants.Descendants.get_duration
   :noindex:

.. automethod:: abjad.tools.selectiontools.Descendants.Descendants.get_spanners
   :noindex:

.. automethod:: abjad.tools.selectiontools.Descendants.Descendants.get_vertical_moment_at
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.selectiontools.Descendants.Descendants.__add__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Descendants.Descendants.__contains__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Descendants.Descendants.__eq__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Descendants.Descendants.__format__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Descendants.Descendants.__getitem__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Descendants.Descendants.__hash__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Descendants.Descendants.__illustrate__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Descendants.Descendants.__len__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Descendants.Descendants.__ne__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Descendants.Descendants.__radd__
   :noindex:

.. automethod:: abjad.tools.selectiontools.Descendants.Descendants.__repr__
   :noindex:
