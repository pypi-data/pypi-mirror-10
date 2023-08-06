developerscripttools.PyTestScript
=================================

.. autoclass:: abjad.tools.developerscripttools.PyTestScript.PyTestScript

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
           "developerscripttools.DirectoryScript" [color=3,
               group=2,
               label=DirectoryScript,
               shape=oval,
               style=bold];
           "developerscripttools.PyTestScript" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>PyTestScript</B>>,
               shape=box,
               style="filled, rounded"];
           "developerscripttools.DeveloperScript" -> "developerscripttools.DirectoryScript";
           "developerscripttools.DirectoryScript" -> "developerscripttools.PyTestScript";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "developerscripttools.DeveloperScript";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.alias
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.argument_parser
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.colors
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.formatted_help
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.formatted_usage
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.formatted_version
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.long_description
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.process_args
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.program_name
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.scripting_group
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.setup_argument_parser
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.short_description
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.version
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.__call__
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.__eq__
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.__format__
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.__hash__
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.__ne__
      ~abjad.tools.developerscripttools.PyTestScript.PyTestScript.__repr__

Bases
-----

- :py:class:`developerscripttools.DirectoryScript <abjad.tools.developerscripttools.DirectoryScript.DirectoryScript>`

- :py:class:`developerscripttools.DeveloperScript <abjad.tools.developerscripttools.DeveloperScript.DeveloperScript>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.alias
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.argument_parser
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.colors
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.formatted_help
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.formatted_usage
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.formatted_version
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.long_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.program_name
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.scripting_group
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.short_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.version
   :noindex:

Methods
-------

.. automethod:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.process_args
   :noindex:

.. automethod:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.setup_argument_parser
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.__call__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.__eq__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.__format__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.__hash__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.__ne__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.PyTestScript.PyTestScript.__repr__
   :noindex:
