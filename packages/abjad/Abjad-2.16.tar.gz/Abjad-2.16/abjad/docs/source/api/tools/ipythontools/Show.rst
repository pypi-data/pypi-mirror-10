ipythontools.Show
=================

.. autoclass:: abjad.tools.ipythontools.Show.Show

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
       subgraph cluster_ipythontools {
           graph [label=ipythontools];
           "ipythontools.Show" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>Show</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "ipythontools.Show";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.ipythontools.Show.Show.__call__

Bases
-----

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.ipythontools.Show.Show.__call__
   :noindex:
