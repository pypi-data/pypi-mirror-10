exceptiontools.MissingMeasureError
==================================

.. autoclass:: abjad.tools.exceptiontools.MissingMeasureError.MissingMeasureError

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
       subgraph cluster_exceptiontools {
           graph [label=exceptiontools];
           "exceptiontools.MissingMeasureError" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>MissingMeasureError</B>>,
               shape=box,
               style="filled, rounded"];
       }
       subgraph cluster_exceptions {
           graph [label=exceptions];
           "exceptions.BaseException" [color=2,
               group=1,
               label=BaseException,
               shape=box];
           "exceptions.Exception" [color=2,
               group=1,
               label=Exception,
               shape=box];
           "exceptions.BaseException" -> "exceptions.Exception";
       }
       "__builtin__.object" -> "exceptions.BaseException";
       "exceptions.Exception" -> "exceptiontools.MissingMeasureError";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.exceptiontools.MissingMeasureError.MissingMeasureError.__delattr__
      ~abjad.tools.exceptiontools.MissingMeasureError.MissingMeasureError.__getitem__
      ~abjad.tools.exceptiontools.MissingMeasureError.MissingMeasureError.__getslice__
      ~abjad.tools.exceptiontools.MissingMeasureError.MissingMeasureError.__repr__
      ~abjad.tools.exceptiontools.MissingMeasureError.MissingMeasureError.__setattr__
      ~abjad.tools.exceptiontools.MissingMeasureError.MissingMeasureError.__str__
      ~abjad.tools.exceptiontools.MissingMeasureError.MissingMeasureError.__unicode__

Bases
-----

- :py:class:`exceptions.Exception <exceptions.Exception>`

- :py:class:`exceptions.BaseException <exceptions.BaseException>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.exceptiontools.MissingMeasureError.MissingMeasureError.__delattr__
   :noindex:

.. automethod:: abjad.tools.exceptiontools.MissingMeasureError.MissingMeasureError.__getitem__
   :noindex:

.. automethod:: abjad.tools.exceptiontools.MissingMeasureError.MissingMeasureError.__getslice__
   :noindex:

.. automethod:: abjad.tools.exceptiontools.MissingMeasureError.MissingMeasureError.__repr__
   :noindex:

.. automethod:: abjad.tools.exceptiontools.MissingMeasureError.MissingMeasureError.__setattr__
   :noindex:

.. automethod:: abjad.tools.exceptiontools.MissingMeasureError.MissingMeasureError.__str__
   :noindex:

.. automethod:: abjad.tools.exceptiontools.MissingMeasureError.MissingMeasureError.__unicode__
   :noindex:
