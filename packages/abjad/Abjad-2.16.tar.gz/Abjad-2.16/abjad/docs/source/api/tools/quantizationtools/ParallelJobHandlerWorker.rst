quantizationtools.ParallelJobHandlerWorker
==========================================

.. autoclass:: abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker

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
           "quantizationtools.ParallelJobHandlerWorker" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>ParallelJobHandlerWorker</B>>,
               shape=box,
               style="filled, rounded"];
       }
       subgraph cluster_multiprocessing {
           graph [label=multiprocessing];
           "multiprocessing.process.Process" [color=3,
               group=2,
               label=Process,
               shape=box];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "__builtin__.object" -> "multiprocessing.process.Process";
       "abctools.AbjadObject" -> "quantizationtools.ParallelJobHandlerWorker";
       "multiprocessing.process.Process" -> "quantizationtools.ParallelJobHandlerWorker";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.authkey
      ~abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.daemon
      ~abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.exitcode
      ~abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.ident
      ~abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.is_alive
      ~abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.join
      ~abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.name
      ~abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.pid
      ~abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.run
      ~abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.start
      ~abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.terminate
      ~abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.__eq__
      ~abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.__format__
      ~abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.__hash__
      ~abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.__ne__
      ~abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.__repr__

Bases
-----

- :py:class:`multiprocessing.process.Process <multiprocessing.process.Process>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.exitcode
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.ident
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.pid
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.authkey
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.daemon
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.is_alive
   :noindex:

.. automethod:: abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.join
   :noindex:

.. automethod:: abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.run
   :noindex:

.. automethod:: abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.start
   :noindex:

.. automethod:: abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.terminate
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.ParallelJobHandlerWorker.ParallelJobHandlerWorker.__repr__
   :noindex:
