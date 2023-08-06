handlertools.OverrideHandler
============================

.. autoclass:: abjad.tools.handlertools.OverrideHandler.OverrideHandler

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
           "handlertools.Handler" [color=3,
               group=2,
               label=Handler,
               shape=oval,
               style=bold];
           "handlertools.OverrideHandler" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>OverrideHandler</B>>,
               shape=box,
               style="filled, rounded"];
           "handlertools.Handler" -> "handlertools.OverrideHandler";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "handlertools.Handler";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.handlertools.OverrideHandler.OverrideHandler.attribute_name
      ~abjad.tools.handlertools.OverrideHandler.OverrideHandler.attribute_value
      ~abjad.tools.handlertools.OverrideHandler.OverrideHandler.grob_name
      ~abjad.tools.handlertools.OverrideHandler.OverrideHandler.maximum_settings
      ~abjad.tools.handlertools.OverrideHandler.OverrideHandler.maximum_written_duration
      ~abjad.tools.handlertools.OverrideHandler.OverrideHandler.__call__
      ~abjad.tools.handlertools.OverrideHandler.OverrideHandler.__copy__
      ~abjad.tools.handlertools.OverrideHandler.OverrideHandler.__eq__
      ~abjad.tools.handlertools.OverrideHandler.OverrideHandler.__format__
      ~abjad.tools.handlertools.OverrideHandler.OverrideHandler.__hash__
      ~abjad.tools.handlertools.OverrideHandler.OverrideHandler.__ne__
      ~abjad.tools.handlertools.OverrideHandler.OverrideHandler.__repr__

Bases
-----

- :py:class:`handlertools.Handler <abjad.tools.handlertools.Handler.Handler>`

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.handlertools.OverrideHandler.OverrideHandler.attribute_name
   :noindex:

.. autoattribute:: abjad.tools.handlertools.OverrideHandler.OverrideHandler.attribute_value
   :noindex:

.. autoattribute:: abjad.tools.handlertools.OverrideHandler.OverrideHandler.grob_name
   :noindex:

.. autoattribute:: abjad.tools.handlertools.OverrideHandler.OverrideHandler.maximum_settings
   :noindex:

.. autoattribute:: abjad.tools.handlertools.OverrideHandler.OverrideHandler.maximum_written_duration
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.handlertools.OverrideHandler.OverrideHandler.__call__
   :noindex:

.. automethod:: abjad.tools.handlertools.OverrideHandler.OverrideHandler.__copy__
   :noindex:

.. automethod:: abjad.tools.handlertools.OverrideHandler.OverrideHandler.__eq__
   :noindex:

.. automethod:: abjad.tools.handlertools.OverrideHandler.OverrideHandler.__format__
   :noindex:

.. automethod:: abjad.tools.handlertools.OverrideHandler.OverrideHandler.__hash__
   :noindex:

.. automethod:: abjad.tools.handlertools.OverrideHandler.OverrideHandler.__ne__
   :noindex:

.. automethod:: abjad.tools.handlertools.OverrideHandler.OverrideHandler.__repr__
   :noindex:
