systemtools.Timer
=================

.. autoclass:: abjad.tools.systemtools.Timer.Timer

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
           "abctools.ContextManager" [color=2,
               group=1,
               label=ContextManager,
               shape=oval,
               style=bold];
           "abctools.AbjadObject" -> "abctools.ContextManager";
           "abctools.AbjadObject.AbstractBase" -> "abctools.AbjadObject";
       }
       subgraph cluster_systemtools {
           graph [label=systemtools];
           "systemtools.Timer" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Timer</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.ContextManager" -> "systemtools.Timer";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.systemtools.Timer.Timer.elapsed_time
      ~abjad.tools.systemtools.Timer.Timer.enter_message
      ~abjad.tools.systemtools.Timer.Timer.exit_message
      ~abjad.tools.systemtools.Timer.Timer.start_time
      ~abjad.tools.systemtools.Timer.Timer.stop_time
      ~abjad.tools.systemtools.Timer.Timer.verbose
      ~abjad.tools.systemtools.Timer.Timer.__enter__
      ~abjad.tools.systemtools.Timer.Timer.__eq__
      ~abjad.tools.systemtools.Timer.Timer.__exit__
      ~abjad.tools.systemtools.Timer.Timer.__format__
      ~abjad.tools.systemtools.Timer.Timer.__hash__
      ~abjad.tools.systemtools.Timer.Timer.__ne__
      ~abjad.tools.systemtools.Timer.Timer.__repr__

Bases
-----

- :py:class:`abctools.ContextManager <abjad.tools.abctools.ContextManager.ContextManager>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.systemtools.Timer.Timer.elapsed_time
   :noindex:

.. autoattribute:: abjad.tools.systemtools.Timer.Timer.enter_message
   :noindex:

.. autoattribute:: abjad.tools.systemtools.Timer.Timer.exit_message
   :noindex:

.. autoattribute:: abjad.tools.systemtools.Timer.Timer.start_time
   :noindex:

.. autoattribute:: abjad.tools.systemtools.Timer.Timer.stop_time
   :noindex:

.. autoattribute:: abjad.tools.systemtools.Timer.Timer.verbose
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.systemtools.Timer.Timer.__enter__
   :noindex:

.. automethod:: abjad.tools.systemtools.Timer.Timer.__eq__
   :noindex:

.. automethod:: abjad.tools.systemtools.Timer.Timer.__exit__
   :noindex:

.. automethod:: abjad.tools.systemtools.Timer.Timer.__format__
   :noindex:

.. automethod:: abjad.tools.systemtools.Timer.Timer.__hash__
   :noindex:

.. automethod:: abjad.tools.systemtools.Timer.Timer.__ne__
   :noindex:

.. automethod:: abjad.tools.systemtools.Timer.Timer.__repr__
   :noindex:
