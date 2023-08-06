datastructuretools.Enumeration
==============================

.. autoclass:: abjad.tools.datastructuretools.Enumeration.Enumeration

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
           "__builtin__.int" [color=1,
               group=0,
               label=int,
               shape=box];
           "__builtin__.object" [color=1,
               group=0,
               label=object,
               shape=box];
           "__builtin__.object" -> "__builtin__.int";
       }
       subgraph cluster_datastructuretools {
           graph [label=datastructuretools];
           "datastructuretools.Enumeration" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>Enumeration</B>>,
               shape=box,
               style="filled, rounded"];
       }
       subgraph cluster_enum {
           graph [label=enum];
           "enum.Enum" [color=3,
               group=2,
               label=Enum,
               shape=box];
           "enum.IntEnum" [color=3,
               group=2,
               label=IntEnum,
               shape=box];
           "enum.Enum" -> "enum.IntEnum";
       }
       "__builtin__.int" -> "enum.IntEnum";
       "__builtin__.object" -> "enum.Enum";
       "enum.IntEnum" -> "datastructuretools.Enumeration";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::


Bases
-----

- :py:class:`enum.IntEnum <enum.IntEnum>`

- :py:class:`__builtin__.int <int>`

- :py:class:`enum.Enum <enum.Enum>`

- :py:class:`__builtin__.object <object>`
