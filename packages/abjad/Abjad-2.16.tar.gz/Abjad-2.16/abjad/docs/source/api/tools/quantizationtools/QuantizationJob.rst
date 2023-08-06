quantizationtools.QuantizationJob
=================================

.. autoclass:: abjad.tools.quantizationtools.QuantizationJob.QuantizationJob

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
           "quantizationtools.QuantizationJob" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>QuantizationJob</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.QuantizationJob";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.job_id
      ~abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.q_event_proxies
      ~abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.q_grids
      ~abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.search_tree
      ~abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.__call__
      ~abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.__eq__
      ~abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.__format__
      ~abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.__hash__
      ~abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.__ne__
      ~abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.job_id
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.q_event_proxies
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.q_grids
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.search_tree
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QuantizationJob.QuantizationJob.__repr__
   :noindex:
