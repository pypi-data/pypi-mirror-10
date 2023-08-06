quantizationtools.JobHandler
============================

.. autoclass:: abjad.tools.quantizationtools.JobHandler.JobHandler

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
           "quantizationtools.JobHandler" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>JobHandler</B>>,
               shape=oval,
               style="filled, rounded"];
           "quantizationtools.ParallelJobHandler" [color=3,
               group=2,
               label=ParallelJobHandler,
               shape=box];
           "quantizationtools.SerialJobHandler" [color=3,
               group=2,
               label=SerialJobHandler,
               shape=box];
           "quantizationtools.JobHandler" -> "quantizationtools.ParallelJobHandler";
           "quantizationtools.JobHandler" -> "quantizationtools.SerialJobHandler";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.JobHandler";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.JobHandler.JobHandler.__call__
      ~abjad.tools.quantizationtools.JobHandler.JobHandler.__eq__
      ~abjad.tools.quantizationtools.JobHandler.JobHandler.__format__
      ~abjad.tools.quantizationtools.JobHandler.JobHandler.__hash__
      ~abjad.tools.quantizationtools.JobHandler.JobHandler.__ne__
      ~abjad.tools.quantizationtools.JobHandler.JobHandler.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.JobHandler.JobHandler.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.JobHandler.JobHandler.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.JobHandler.JobHandler.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.JobHandler.JobHandler.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.JobHandler.JobHandler.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.JobHandler.JobHandler.__repr__
   :noindex:
