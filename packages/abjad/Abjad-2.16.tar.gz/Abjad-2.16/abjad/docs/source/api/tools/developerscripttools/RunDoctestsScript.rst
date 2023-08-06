developerscripttools.RunDoctestsScript
======================================

.. autoclass:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript

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
           "developerscripttools.RunDoctestsScript" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>RunDoctestsScript</B>>,
               shape=box,
               style="filled, rounded"];
           "developerscripttools.DeveloperScript" -> "developerscripttools.DirectoryScript";
           "developerscripttools.DirectoryScript" -> "developerscripttools.RunDoctestsScript";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "developerscripttools.DeveloperScript";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.alias
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.argument_parser
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.colors
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.formatted_help
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.formatted_usage
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.formatted_version
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.long_description
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.process_args
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.program_name
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.scripting_group
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.setup_argument_parser
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.short_description
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.version
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.__call__
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.__eq__
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.__format__
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.__hash__
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.__ne__
      ~abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.__repr__

Bases
-----

- :py:class:`developerscripttools.DirectoryScript <abjad.tools.developerscripttools.DirectoryScript.DirectoryScript>`

- :py:class:`developerscripttools.DeveloperScript <abjad.tools.developerscripttools.DeveloperScript.DeveloperScript>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.alias
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.argument_parser
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.colors
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.formatted_help
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.formatted_usage
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.formatted_version
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.long_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.program_name
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.scripting_group
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.short_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.version
   :noindex:

Methods
-------

.. automethod:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.process_args
   :noindex:

.. automethod:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.setup_argument_parser
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.__call__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.__eq__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.__format__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.__hash__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.__ne__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.RunDoctestsScript.RunDoctestsScript.__repr__
   :noindex:
