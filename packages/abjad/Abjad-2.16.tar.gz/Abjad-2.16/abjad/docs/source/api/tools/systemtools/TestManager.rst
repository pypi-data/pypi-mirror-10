systemtools.TestManager
=======================

.. autoclass:: abjad.tools.systemtools.TestManager.TestManager

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
           "systemtools.TestManager" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>TestManager</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "systemtools.TestManager";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.systemtools.TestManager.TestManager.apply_additional_layout
      ~abjad.tools.systemtools.TestManager.TestManager.clean_string
      ~abjad.tools.systemtools.TestManager.TestManager.compare
      ~abjad.tools.systemtools.TestManager.TestManager.compare_files
      ~abjad.tools.systemtools.TestManager.TestManager.get_current_function_name
      ~abjad.tools.systemtools.TestManager.TestManager.read_test_output
      ~abjad.tools.systemtools.TestManager.TestManager.test_function_name_to_title_lines
      ~abjad.tools.systemtools.TestManager.TestManager.write_test_output

Bases
-----

- :py:class:`__builtin__.object <object>`

Static methods
--------------

.. automethod:: abjad.tools.systemtools.TestManager.TestManager.apply_additional_layout
   :noindex:

.. automethod:: abjad.tools.systemtools.TestManager.TestManager.clean_string
   :noindex:

.. automethod:: abjad.tools.systemtools.TestManager.TestManager.compare
   :noindex:

.. automethod:: abjad.tools.systemtools.TestManager.TestManager.compare_files
   :noindex:

.. automethod:: abjad.tools.systemtools.TestManager.TestManager.get_current_function_name
   :noindex:

.. automethod:: abjad.tools.systemtools.TestManager.TestManager.read_test_output
   :noindex:

.. automethod:: abjad.tools.systemtools.TestManager.TestManager.test_function_name_to_title_lines
   :noindex:

.. automethod:: abjad.tools.systemtools.TestManager.TestManager.write_test_output
   :noindex:
