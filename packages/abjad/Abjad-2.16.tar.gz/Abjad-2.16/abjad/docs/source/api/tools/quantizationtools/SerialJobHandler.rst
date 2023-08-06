quantizationtools.SerialJobHandler
==================================

.. autoclass:: abjad.tools.quantizationtools.SerialJobHandler.SerialJobHandler

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
           "quantizationtools.JobHandler" [color=3,
               group=2,
               label=JobHandler,
               shape=oval,
               style=bold];
           "quantizationtools.SerialJobHandler" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>SerialJobHandler</B>>,
               shape=box,
               style="filled, rounded"];
           "quantizationtools.JobHandler" -> "quantizationtools.SerialJobHandler";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.JobHandler";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.SerialJobHandler.SerialJobHandler.__call__
      ~abjad.tools.quantizationtools.SerialJobHandler.SerialJobHandler.__eq__
      ~abjad.tools.quantizationtools.SerialJobHandler.SerialJobHandler.__format__
      ~abjad.tools.quantizationtools.SerialJobHandler.SerialJobHandler.__hash__
      ~abjad.tools.quantizationtools.SerialJobHandler.SerialJobHandler.__ne__
      ~abjad.tools.quantizationtools.SerialJobHandler.SerialJobHandler.__repr__

Bases
-----

- :py:class:`quantizationtools.JobHandler <abjad.tools.quantizationtools.JobHandler.JobHandler>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.SerialJobHandler.SerialJobHandler.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.SerialJobHandler.SerialJobHandler.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.SerialJobHandler.SerialJobHandler.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.SerialJobHandler.SerialJobHandler.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.SerialJobHandler.SerialJobHandler.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.SerialJobHandler.SerialJobHandler.__repr__
   :noindex:
