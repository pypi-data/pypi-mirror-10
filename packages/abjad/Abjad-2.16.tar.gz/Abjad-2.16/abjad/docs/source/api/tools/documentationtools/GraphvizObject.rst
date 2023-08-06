documentationtools.GraphvizObject
=================================

.. autoclass:: abjad.tools.documentationtools.GraphvizObject.GraphvizObject

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
       subgraph cluster_abctools {
           graph [label=abctools];
           "abctools.AbjadObject" [color=2,
               group=1,
               label=AbjadObject,
               shape=box];
           "abctools.AbjadObject.AbstractBase" [color=2,
               group=1,
               label=AbstractBase,
               shape=box];
           "abctools.AbjadObject.AbstractBase" -> "abctools.AbjadObject";
       }
       subgraph cluster_documentationtools {
           graph [label=documentationtools];
           "documentationtools.GraphvizEdge" [color=3,
               group=2,
               label=GraphvizEdge,
               shape=box];
           "documentationtools.GraphvizGraph" [color=3,
               group=2,
               label=GraphvizGraph,
               shape=box];
           "documentationtools.GraphvizNode" [color=3,
               group=2,
               label=GraphvizNode,
               shape=box];
           "documentationtools.GraphvizObject" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>GraphvizObject</B>>,
               shape=oval,
               style="filled, rounded"];
           "documentationtools.GraphvizSubgraph" [color=3,
               group=2,
               label=GraphvizSubgraph,
               shape=box];
           "documentationtools.GraphvizGraph" -> "documentationtools.GraphvizSubgraph";
           "documentationtools.GraphvizObject" -> "documentationtools.GraphvizEdge";
           "documentationtools.GraphvizObject" -> "documentationtools.GraphvizGraph";
           "documentationtools.GraphvizObject" -> "documentationtools.GraphvizNode";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "documentationtools.GraphvizObject";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.GraphvizObject.GraphvizObject.attributes
      ~abjad.tools.documentationtools.GraphvizObject.GraphvizObject.__eq__
      ~abjad.tools.documentationtools.GraphvizObject.GraphvizObject.__format__
      ~abjad.tools.documentationtools.GraphvizObject.GraphvizObject.__hash__
      ~abjad.tools.documentationtools.GraphvizObject.GraphvizObject.__ne__
      ~abjad.tools.documentationtools.GraphvizObject.GraphvizObject.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizObject.GraphvizObject.attributes
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.GraphvizObject.GraphvizObject.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizObject.GraphvizObject.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizObject.GraphvizObject.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizObject.GraphvizObject.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizObject.GraphvizObject.__repr__
   :noindex:
