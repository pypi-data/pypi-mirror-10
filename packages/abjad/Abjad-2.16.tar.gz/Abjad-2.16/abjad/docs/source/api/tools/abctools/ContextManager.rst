abctools.ContextManager
=======================

.. autoclass:: abjad.tools.abctools.ContextManager.ContextManager

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
           "abctools.ContextManager" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>ContextManager</B>>,
               shape=oval,
               style="filled, rounded"];
           "abctools.AbjadObject" -> "abctools.ContextManager";
           "abctools.AbjadObject.AbstractBase" -> "abctools.AbjadObject";
       }
       subgraph cluster_systemtools {
           graph [label=systemtools];
           "systemtools.FilesystemState" [color=4,
               group=3,
               label=FilesystemState,
               shape=box];
           "systemtools.ForbidUpdate" [color=4,
               group=3,
               label=ForbidUpdate,
               shape=box];
           "systemtools.NullContextManager" [color=4,
               group=3,
               label=NullContextManager,
               shape=box];
           "systemtools.ProgressIndicator" [color=4,
               group=3,
               label=ProgressIndicator,
               shape=box];
           "systemtools.RedirectedStreams" [color=4,
               group=3,
               label=RedirectedStreams,
               shape=box];
           "systemtools.TemporaryDirectory" [color=4,
               group=3,
               label=TemporaryDirectory,
               shape=box];
           "systemtools.TemporaryDirectoryChange" [color=4,
               group=3,
               label=TemporaryDirectoryChange,
               shape=box];
           "systemtools.Timer" [color=4,
               group=3,
               label=Timer,
               shape=box];
       }
       subgraph cluster_ide {
           graph [label=ide];
           "ide.idetools.ControllerContext" [color=3,
               group=2,
               label=ControllerContext,
               shape=box];
           "ide.idetools.Interaction" [color=3,
               group=2,
               label=Interaction,
               shape=box];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.ContextManager" -> "systemtools.FilesystemState";
       "abctools.ContextManager" -> "systemtools.ForbidUpdate";
       "abctools.ContextManager" -> "systemtools.NullContextManager";
       "abctools.ContextManager" -> "systemtools.ProgressIndicator";
       "abctools.ContextManager" -> "systemtools.RedirectedStreams";
       "abctools.ContextManager" -> "systemtools.TemporaryDirectory";
       "abctools.ContextManager" -> "systemtools.TemporaryDirectoryChange";
       "abctools.ContextManager" -> "systemtools.Timer";
       "abctools.ContextManager" -> "ide.idetools.ControllerContext";
       "abctools.ContextManager" -> "ide.idetools.Interaction";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.abctools.ContextManager.ContextManager.__enter__
      ~abjad.tools.abctools.ContextManager.ContextManager.__eq__
      ~abjad.tools.abctools.ContextManager.ContextManager.__exit__
      ~abjad.tools.abctools.ContextManager.ContextManager.__format__
      ~abjad.tools.abctools.ContextManager.ContextManager.__hash__
      ~abjad.tools.abctools.ContextManager.ContextManager.__ne__
      ~abjad.tools.abctools.ContextManager.ContextManager.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.abctools.ContextManager.ContextManager.__enter__
   :noindex:

.. automethod:: abjad.tools.abctools.ContextManager.ContextManager.__eq__
   :noindex:

.. automethod:: abjad.tools.abctools.ContextManager.ContextManager.__exit__
   :noindex:

.. automethod:: abjad.tools.abctools.ContextManager.ContextManager.__format__
   :noindex:

.. automethod:: abjad.tools.abctools.ContextManager.ContextManager.__hash__
   :noindex:

.. automethod:: abjad.tools.abctools.ContextManager.ContextManager.__ne__
   :noindex:

.. automethod:: abjad.tools.abctools.ContextManager.ContextManager.__repr__
   :noindex:
