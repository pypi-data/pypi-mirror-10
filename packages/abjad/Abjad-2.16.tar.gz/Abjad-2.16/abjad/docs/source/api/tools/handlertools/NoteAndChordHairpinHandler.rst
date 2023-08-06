handlertools.NoteAndChordHairpinHandler
=======================================

.. autoclass:: abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler

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
           "handlertools.DynamicHandler" [color=3,
               group=2,
               label=DynamicHandler,
               shape=oval,
               style=bold];
           "handlertools.Handler" [color=3,
               group=2,
               label=Handler,
               shape=oval,
               style=bold];
           "handlertools.NoteAndChordHairpinHandler" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>NoteAndChordHairpinHandler</B>>,
               shape=box,
               style="filled, rounded"];
           "handlertools.DynamicHandler" -> "handlertools.NoteAndChordHairpinHandler";
           "handlertools.Handler" -> "handlertools.DynamicHandler";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "handlertools.Handler";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.attach_start_dynamic_to_lone_notes
      ~abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.hairpin_token
      ~abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.minimum_duration
      ~abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.patterns
      ~abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.span
      ~abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.__call__
      ~abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.__copy__
      ~abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.__eq__
      ~abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.__format__
      ~abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.__hash__
      ~abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.__ne__
      ~abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.__repr__

Bases
-----

- :py:class:`handlertools.DynamicHandler <abjad.tools.handlertools.DynamicHandler.DynamicHandler>`

- :py:class:`handlertools.Handler <abjad.tools.handlertools.Handler.Handler>`

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.attach_start_dynamic_to_lone_notes
   :noindex:

.. autoattribute:: abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.hairpin_token
   :noindex:

.. autoattribute:: abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.minimum_duration
   :noindex:

.. autoattribute:: abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.patterns
   :noindex:

.. autoattribute:: abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.span
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.__call__
   :noindex:

.. automethod:: abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.__copy__
   :noindex:

.. automethod:: abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.__eq__
   :noindex:

.. automethod:: abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.__format__
   :noindex:

.. automethod:: abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.__hash__
   :noindex:

.. automethod:: abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.__ne__
   :noindex:

.. automethod:: abjad.tools.handlertools.NoteAndChordHairpinHandler.NoteAndChordHairpinHandler.__repr__
   :noindex:
