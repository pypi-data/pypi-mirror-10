developerscripttools.RenameModulesScript
========================================

.. autoclass:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript

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
           "developerscripttools.RenameModulesScript" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>RenameModulesScript</B>>,
               shape=box,
               style="filled, rounded"];
           "developerscripttools.DeveloperScript" -> "developerscripttools.RenameModulesScript";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "developerscripttools.DeveloperScript";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.alias
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.argument_parser
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.colors
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.formatted_help
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.formatted_usage
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.formatted_version
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.long_description
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.process_args
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.program_name
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.scripting_group
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.setup_argument_parser
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.short_description
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.version
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.__call__
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.__eq__
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.__format__
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.__hash__
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.__ne__
      ~abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.__repr__

Bases
-----

- :py:class:`developerscripttools.DeveloperScript <abjad.tools.developerscripttools.DeveloperScript.DeveloperScript>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.alias
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.argument_parser
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.colors
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.formatted_help
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.formatted_usage
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.formatted_version
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.long_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.program_name
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.scripting_group
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.short_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.version
   :noindex:

Methods
-------

.. automethod:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.process_args
   :noindex:

.. automethod:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.setup_argument_parser
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.__call__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.__eq__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.__format__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.__hash__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.__ne__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.RenameModulesScript.RenameModulesScript.__repr__
   :noindex:
