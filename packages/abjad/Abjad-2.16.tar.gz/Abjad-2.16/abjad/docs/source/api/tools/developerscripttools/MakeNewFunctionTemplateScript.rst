developerscripttools.MakeNewFunctionTemplateScript
==================================================

.. autoclass:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript

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
           "developerscripttools.MakeNewFunctionTemplateScript" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>MakeNewFunctionTemplateScript</B>>,
               shape=box,
               style="filled, rounded"];
           "developerscripttools.DeveloperScript" -> "developerscripttools.MakeNewFunctionTemplateScript";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "developerscripttools.DeveloperScript";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.alias
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.argument_parser
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.colors
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.formatted_help
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.formatted_usage
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.formatted_version
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.long_description
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.process_args
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.program_name
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.scripting_group
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.setup_argument_parser
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.short_description
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.version
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.__call__
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.__eq__
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.__format__
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.__hash__
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.__ne__
      ~abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.__repr__

Bases
-----

- :py:class:`developerscripttools.DeveloperScript <abjad.tools.developerscripttools.DeveloperScript.DeveloperScript>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.alias
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.argument_parser
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.colors
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.formatted_help
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.formatted_usage
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.formatted_version
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.long_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.program_name
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.scripting_group
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.short_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.version
   :noindex:

Methods
-------

.. automethod:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.process_args
   :noindex:

.. automethod:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.setup_argument_parser
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.__call__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.__eq__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.__format__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.__hash__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.__ne__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.MakeNewFunctionTemplateScript.MakeNewFunctionTemplateScript.__repr__
   :noindex:
