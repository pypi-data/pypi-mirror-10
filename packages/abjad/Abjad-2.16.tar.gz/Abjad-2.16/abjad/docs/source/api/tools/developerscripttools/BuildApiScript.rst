developerscripttools.BuildApiScript
===================================

.. autoclass:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript

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
           "developerscripttools.BuildApiScript" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>BuildApiScript</B>>,
               shape=box,
               style="filled, rounded"];
           "developerscripttools.DeveloperScript" [color=3,
               group=2,
               label=DeveloperScript,
               shape=oval,
               style=bold];
           "developerscripttools.DeveloperScript" -> "developerscripttools.BuildApiScript";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "developerscripttools.DeveloperScript";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.alias
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.argument_parser
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.colors
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.formatted_help
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.formatted_usage
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.formatted_version
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.long_description
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.process_args
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.program_name
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.scripting_group
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.setup_argument_parser
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.short_description
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.version
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.__call__
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.__eq__
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.__format__
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.__hash__
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.__ne__
      ~abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.__repr__

Bases
-----

- :py:class:`developerscripttools.DeveloperScript <abjad.tools.developerscripttools.DeveloperScript.DeveloperScript>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.alias
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.argument_parser
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.colors
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.formatted_help
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.formatted_usage
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.formatted_version
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.long_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.program_name
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.scripting_group
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.short_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.version
   :noindex:

Methods
-------

.. automethod:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.process_args
   :noindex:

.. automethod:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.setup_argument_parser
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.__call__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.__eq__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.__format__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.__hash__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.__ne__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.BuildApiScript.BuildApiScript.__repr__
   :noindex:
