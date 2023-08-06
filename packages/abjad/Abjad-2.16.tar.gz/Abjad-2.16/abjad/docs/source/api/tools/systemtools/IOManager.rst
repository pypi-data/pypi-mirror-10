systemtools.IOManager
=====================

.. autoclass:: abjad.tools.systemtools.IOManager.IOManager

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
       subgraph cluster_systemtools {
           graph [label=systemtools];
           "systemtools.IOManager" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>IOManager</B>>,
               shape=box,
               style="filled, rounded"];
       }
       subgraph cluster_ide {
           graph [label=ide];
           "ide.idetools.IOManager" [color=2,
               group=1,
               label=IOManager,
               shape=box];
       }
       "__builtin__.object" -> "systemtools.IOManager";
       "systemtools.IOManager" -> "ide.idetools.IOManager";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.systemtools.IOManager.IOManager.clear_terminal
      ~abjad.tools.systemtools.IOManager.IOManager.count_function_calls
      ~abjad.tools.systemtools.IOManager.IOManager.find_executable
      ~abjad.tools.systemtools.IOManager.IOManager.get_last_output_file_name
      ~abjad.tools.systemtools.IOManager.IOManager.get_next_output_file_name
      ~abjad.tools.systemtools.IOManager.IOManager.make_subprocess
      ~abjad.tools.systemtools.IOManager.IOManager.open_file
      ~abjad.tools.systemtools.IOManager.IOManager.open_last_log
      ~abjad.tools.systemtools.IOManager.IOManager.open_last_ly
      ~abjad.tools.systemtools.IOManager.IOManager.open_last_pdf
      ~abjad.tools.systemtools.IOManager.IOManager.profile_expr
      ~abjad.tools.systemtools.IOManager.IOManager.run_lilypond
      ~abjad.tools.systemtools.IOManager.IOManager.save_last_ly_as
      ~abjad.tools.systemtools.IOManager.IOManager.save_last_pdf_as
      ~abjad.tools.systemtools.IOManager.IOManager.spawn_subprocess

Bases
-----

- :py:class:`__builtin__.object <object>`

Static methods
--------------

.. automethod:: abjad.tools.systemtools.IOManager.IOManager.clear_terminal
   :noindex:

.. automethod:: abjad.tools.systemtools.IOManager.IOManager.count_function_calls
   :noindex:

.. automethod:: abjad.tools.systemtools.IOManager.IOManager.find_executable
   :noindex:

.. automethod:: abjad.tools.systemtools.IOManager.IOManager.get_last_output_file_name
   :noindex:

.. automethod:: abjad.tools.systemtools.IOManager.IOManager.get_next_output_file_name
   :noindex:

.. automethod:: abjad.tools.systemtools.IOManager.IOManager.make_subprocess
   :noindex:

.. automethod:: abjad.tools.systemtools.IOManager.IOManager.open_file
   :noindex:

.. automethod:: abjad.tools.systemtools.IOManager.IOManager.open_last_log
   :noindex:

.. automethod:: abjad.tools.systemtools.IOManager.IOManager.open_last_ly
   :noindex:

.. automethod:: abjad.tools.systemtools.IOManager.IOManager.open_last_pdf
   :noindex:

.. automethod:: abjad.tools.systemtools.IOManager.IOManager.profile_expr
   :noindex:

.. automethod:: abjad.tools.systemtools.IOManager.IOManager.run_lilypond
   :noindex:

.. automethod:: abjad.tools.systemtools.IOManager.IOManager.save_last_ly_as
   :noindex:

.. automethod:: abjad.tools.systemtools.IOManager.IOManager.save_last_pdf_as
   :noindex:

.. automethod:: abjad.tools.systemtools.IOManager.IOManager.spawn_subprocess
   :noindex:
