developerscripttools.TestAndRebuildScript
=========================================

.. autoclass:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript

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
       subgraph cluster_developerscripttools {
           graph [label=developerscripttools];
           "developerscripttools.DeveloperScript" [color=3,
               group=2,
               label=DeveloperScript,
               shape=oval,
               style=bold];
           "developerscripttools.TestAndRebuildScript" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>TestAndRebuildScript</B>>,
               shape=box,
               style="filled, rounded"];
           "developerscripttools.DeveloperScript" -> "developerscripttools.TestAndRebuildScript";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "developerscripttools.DeveloperScript";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.alias
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.argument_parser
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.colors
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.formatted_help
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.formatted_usage
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.formatted_version
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.get_terminal_width
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.long_description
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.process_args
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.program_name
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.rebuild_docs
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.run_doctest
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.run_pytest
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.scripting_group
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.setup_argument_parser
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.short_description
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.version
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.__call__
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.__eq__
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.__format__
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.__hash__
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.__ne__
      ~abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.__repr__

Bases
-----

- :py:class:`developerscripttools.DeveloperScript <abjad.tools.developerscripttools.DeveloperScript.DeveloperScript>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.alias
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.argument_parser
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.colors
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.formatted_help
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.formatted_usage
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.formatted_version
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.long_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.program_name
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.scripting_group
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.short_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.version
   :noindex:

Methods
-------

.. automethod:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.get_terminal_width
   :noindex:

.. automethod:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.process_args
   :noindex:

.. automethod:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.rebuild_docs
   :noindex:

.. automethod:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.run_doctest
   :noindex:

.. automethod:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.run_pytest
   :noindex:

.. automethod:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.setup_argument_parser
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.__call__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.__eq__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.__format__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.__hash__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.__ne__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.TestAndRebuildScript.TestAndRebuildScript.__repr__
   :noindex:
