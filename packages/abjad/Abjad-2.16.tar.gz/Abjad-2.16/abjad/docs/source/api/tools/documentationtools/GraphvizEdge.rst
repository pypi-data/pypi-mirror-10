documentationtools.GraphvizEdge
===============================

.. autoclass:: abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge

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
           "documentationtools.GraphvizEdge" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>GraphvizEdge</B>>,
               shape=box,
               style="filled, rounded"];
           "documentationtools.GraphvizObject" [color=3,
               group=2,
               label=GraphvizObject,
               shape=oval,
               style=bold];
           "documentationtools.GraphvizObject" -> "documentationtools.GraphvizEdge";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "documentationtools.GraphvizObject";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.attributes
      ~abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.head
      ~abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.head_port_position
      ~abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.is_directed
      ~abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.tail
      ~abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.tail_port_position
      ~abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.__call__
      ~abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.__eq__
      ~abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.__format__
      ~abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.__hash__
      ~abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.__ne__
      ~abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.__repr__

Bases
-----

- :py:class:`documentationtools.GraphvizObject <abjad.tools.documentationtools.GraphvizObject.GraphvizObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.attributes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.head
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.tail
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.head_port_position
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.is_directed
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.tail_port_position
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.__call__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.GraphvizEdge.GraphvizEdge.__repr__
   :noindex:
