handlertools.RepeatedMarkupHandler
==================================

.. autoclass:: abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler

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
           "abctools.AbjadValueObject" [color=2,
               group=1,
               label=AbjadValueObject,
               shape=box];
           "abctools.AbjadObject" -> "abctools.AbjadValueObject";
           "abctools.AbjadObject.AbstractBase" -> "abctools.AbjadObject";
       }
       subgraph cluster_handlertools {
           graph [label=handlertools];
           "handlertools.ArticulationHandler" [color=3,
               group=2,
               label=ArticulationHandler,
               shape=oval,
               style=bold];
           "handlertools.Handler" [color=3,
               group=2,
               label=Handler,
               shape=oval,
               style=bold];
           "handlertools.RepeatedMarkupHandler" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>RepeatedMarkupHandler</B>>,
               shape=box,
               style="filled, rounded"];
           "handlertools.ArticulationHandler" -> "handlertools.RepeatedMarkupHandler";
           "handlertools.Handler" -> "handlertools.ArticulationHandler";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "handlertools.Handler";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.markups
      ~abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.maximum_duration
      ~abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.maximum_written_pitch
      ~abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.minimum_duration
      ~abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.minimum_written_pitch
      ~abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.__call__
      ~abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.__copy__
      ~abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.__eq__
      ~abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.__format__
      ~abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.__hash__
      ~abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.__ne__
      ~abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.__repr__

Bases
-----

- :py:class:`handlertools.ArticulationHandler <abjad.tools.handlertools.ArticulationHandler.ArticulationHandler>`

- :py:class:`handlertools.Handler <abjad.tools.handlertools.Handler.Handler>`

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.markups
   :noindex:

.. autoattribute:: abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.maximum_duration
   :noindex:

.. autoattribute:: abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.maximum_written_pitch
   :noindex:

.. autoattribute:: abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.minimum_duration
   :noindex:

.. autoattribute:: abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.minimum_written_pitch
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.__call__
   :noindex:

.. automethod:: abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.__copy__
   :noindex:

.. automethod:: abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.__eq__
   :noindex:

.. automethod:: abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.__format__
   :noindex:

.. automethod:: abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.__hash__
   :noindex:

.. automethod:: abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.__ne__
   :noindex:

.. automethod:: abjad.tools.handlertools.RepeatedMarkupHandler.RepeatedMarkupHandler.__repr__
   :noindex:
