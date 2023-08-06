quantizationtools.ConcatenatingGraceHandler
===========================================

.. autoclass:: abjad.tools.quantizationtools.ConcatenatingGraceHandler.ConcatenatingGraceHandler

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
       subgraph cluster_quantizationtools {
           graph [label=quantizationtools];
           "quantizationtools.ConcatenatingGraceHandler" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>ConcatenatingGraceHandler</B>>,
               shape=box,
               style="filled, rounded"];
           "quantizationtools.GraceHandler" [color=3,
               group=2,
               label=GraceHandler,
               shape=oval,
               style=bold];
           "quantizationtools.GraceHandler" -> "quantizationtools.ConcatenatingGraceHandler";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.GraceHandler";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.ConcatenatingGraceHandler.ConcatenatingGraceHandler.grace_duration
      ~abjad.tools.quantizationtools.ConcatenatingGraceHandler.ConcatenatingGraceHandler.__call__
      ~abjad.tools.quantizationtools.ConcatenatingGraceHandler.ConcatenatingGraceHandler.__eq__
      ~abjad.tools.quantizationtools.ConcatenatingGraceHandler.ConcatenatingGraceHandler.__format__
      ~abjad.tools.quantizationtools.ConcatenatingGraceHandler.ConcatenatingGraceHandler.__hash__
      ~abjad.tools.quantizationtools.ConcatenatingGraceHandler.ConcatenatingGraceHandler.__ne__
      ~abjad.tools.quantizationtools.ConcatenatingGraceHandler.ConcatenatingGraceHandler.__repr__

Bases
-----

- :py:class:`quantizationtools.GraceHandler <abjad.tools.quantizationtools.GraceHandler.GraceHandler>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.ConcatenatingGraceHandler.ConcatenatingGraceHandler.grace_duration
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.ConcatenatingGraceHandler.ConcatenatingGraceHandler.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.ConcatenatingGraceHandler.ConcatenatingGraceHandler.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.ConcatenatingGraceHandler.ConcatenatingGraceHandler.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.ConcatenatingGraceHandler.ConcatenatingGraceHandler.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.ConcatenatingGraceHandler.ConcatenatingGraceHandler.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.ConcatenatingGraceHandler.ConcatenatingGraceHandler.__repr__
   :noindex:
