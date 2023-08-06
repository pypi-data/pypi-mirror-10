developerscripttools.DirectoryScript
====================================

.. autoclass:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript

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
           "developerscripttools.AbjGrepScript" [color=3,
               group=2,
               label=AbjGrepScript,
               shape=box];
           "developerscripttools.CleanScript" [color=3,
               group=2,
               label=CleanScript,
               shape=box];
           "developerscripttools.CountLinewidthsScript" [color=3,
               group=2,
               label=CountLinewidthsScript,
               shape=box];
           "developerscripttools.CountToolsScript" [color=3,
               group=2,
               label=CountToolsScript,
               shape=box];
           "developerscripttools.DeveloperScript" [color=3,
               group=2,
               label=DeveloperScript,
               shape=oval,
               style=bold];
           "developerscripttools.DirectoryScript" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>DirectoryScript</B>>,
               shape=oval,
               style="filled, rounded"];
           "developerscripttools.PyTestScript" [color=3,
               group=2,
               label=PyTestScript,
               shape=box];
           "developerscripttools.ReplaceInFilesScript" [color=3,
               group=2,
               label=ReplaceInFilesScript,
               shape=box];
           "developerscripttools.RunDoctestsScript" [color=3,
               group=2,
               label=RunDoctestsScript,
               shape=box];
           "developerscripttools.DeveloperScript" -> "developerscripttools.DirectoryScript";
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
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.alias
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.argument_parser
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.colors
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.formatted_help
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.formatted_usage
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.formatted_version
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.long_description
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.process_args
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.program_name
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.scripting_group
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.setup_argument_parser
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.short_description
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.version
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.__call__
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.__eq__
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.__format__
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.__hash__
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.__ne__
      ~abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.__repr__

Bases
-----

- :py:class:`developerscripttools.DeveloperScript <abjad.tools.developerscripttools.DeveloperScript.DeveloperScript>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.alias
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.argument_parser
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.colors
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.formatted_help
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.formatted_usage
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.formatted_version
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.long_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.program_name
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.scripting_group
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.short_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.version
   :noindex:

Methods
-------

.. automethod:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.process_args
   :noindex:

.. automethod:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.setup_argument_parser
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.__call__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.__eq__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.__format__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.__hash__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.__ne__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.DirectoryScript.DirectoryScript.__repr__
   :noindex:
