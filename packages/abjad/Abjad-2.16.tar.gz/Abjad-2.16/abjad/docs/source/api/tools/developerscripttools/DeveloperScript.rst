developerscripttools.DeveloperScript
====================================

.. autoclass:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript

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
       subgraph cluster_abjadbooktools {
           graph [label=abjadbooktools];
           "abjadbooktools.AbjadBookScript" [color=3,
               group=2,
               label=AbjadBookScript,
               shape=box];
       }
       subgraph cluster_developerscripttools {
           graph [label=developerscripttools];
           "developerscripttools.AbjDevScript" [color=4,
               group=3,
               label=AbjDevScript,
               shape=box];
           "developerscripttools.AbjGrepScript" [color=4,
               group=3,
               label=AbjGrepScript,
               shape=box];
           "developerscripttools.BuildApiScript" [color=4,
               group=3,
               label=BuildApiScript,
               shape=box];
           "developerscripttools.CleanScript" [color=4,
               group=3,
               label=CleanScript,
               shape=box];
           "developerscripttools.CountLinewidthsScript" [color=4,
               group=3,
               label=CountLinewidthsScript,
               shape=box];
           "developerscripttools.CountToolsScript" [color=4,
               group=3,
               label=CountToolsScript,
               shape=box];
           "developerscripttools.DeveloperScript" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>DeveloperScript</B>>,
               shape=oval,
               style="filled, rounded"];
           "developerscripttools.DirectoryScript" [color=4,
               group=3,
               label=DirectoryScript,
               shape=oval,
               style=bold];
           "developerscripttools.MakeNewClassTemplateScript" [color=4,
               group=3,
               label=MakeNewClassTemplateScript,
               shape=box];
           "developerscripttools.MakeNewFunctionTemplateScript" [color=4,
               group=3,
               label=MakeNewFunctionTemplateScript,
               shape=box];
           "developerscripttools.PyTestScript" [color=4,
               group=3,
               label=PyTestScript,
               shape=box];
           "developerscripttools.RenameModulesScript" [color=4,
               group=3,
               label=RenameModulesScript,
               shape=box];
           "developerscripttools.ReplaceInFilesScript" [color=4,
               group=3,
               label=ReplaceInFilesScript,
               shape=box];
           "developerscripttools.RunDoctestsScript" [color=4,
               group=3,
               label=RunDoctestsScript,
               shape=box];
           "developerscripttools.TestAndRebuildScript" [color=4,
               group=3,
               label=TestAndRebuildScript,
               shape=box];
           "developerscripttools.DeveloperScript" -> "developerscripttools.AbjDevScript";
           "developerscripttools.DeveloperScript" -> "developerscripttools.BuildApiScript";
           "developerscripttools.DeveloperScript" -> "developerscripttools.DirectoryScript";
           "developerscripttools.DeveloperScript" -> "developerscripttools.MakeNewClassTemplateScript";
           "developerscripttools.DeveloperScript" -> "developerscripttools.MakeNewFunctionTemplateScript";
           "developerscripttools.DeveloperScript" -> "developerscripttools.RenameModulesScript";
           "developerscripttools.DeveloperScript" -> "developerscripttools.TestAndRebuildScript";
           "developerscripttools.DirectoryScript" -> "developerscripttools.AbjGrepScript";
           "developerscripttools.DirectoryScript" -> "developerscripttools.CleanScript";
           "developerscripttools.DirectoryScript" -> "developerscripttools.CountLinewidthsScript";
           "developerscripttools.DirectoryScript" -> "developerscripttools.CountToolsScript";
           "developerscripttools.DirectoryScript" -> "developerscripttools.PyTestScript";
           "developerscripttools.DirectoryScript" -> "developerscripttools.ReplaceInFilesScript";
           "developerscripttools.DirectoryScript" -> "developerscripttools.RunDoctestsScript";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "developerscripttools.DeveloperScript";
       "developerscripttools.DeveloperScript" -> "abjadbooktools.AbjadBookScript";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.alias
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.argument_parser
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.colors
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.formatted_help
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.formatted_usage
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.formatted_version
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.long_description
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.process_args
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.program_name
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.scripting_group
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.setup_argument_parser
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.short_description
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.version
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.__call__
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.__eq__
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.__format__
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.__hash__
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.__ne__
      ~abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.alias
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.argument_parser
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.colors
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.formatted_help
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.formatted_usage
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.formatted_version
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.long_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.program_name
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.scripting_group
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.short_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.version
   :noindex:

Methods
-------

.. automethod:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.process_args
   :noindex:

.. automethod:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.setup_argument_parser
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.__call__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.__eq__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.__format__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.__hash__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.__ne__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.DeveloperScript.DeveloperScript.__repr__
   :noindex:
