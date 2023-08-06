developerscripttools.AbjDevScript
=================================

.. autoclass:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript

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
           "developerscripttools.AbjDevScript" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>AbjDevScript</B>>,
               shape=box,
               style="filled, rounded"];
           "developerscripttools.DeveloperScript" [color=3,
               group=2,
               label=DeveloperScript,
               shape=oval,
               style=bold];
           "developerscripttools.DeveloperScript" -> "developerscripttools.AbjDevScript";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "developerscripttools.DeveloperScript";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.alias
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.argument_parser
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.colors
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.developer_script_aliases
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.developer_script_classes
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.developer_script_program_names
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.formatted_help
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.formatted_usage
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.formatted_version
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.long_description
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.process_args
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.program_name
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.scripting_group
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.setup_argument_parser
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.short_description
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.version
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.__call__
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.__eq__
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.__format__
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.__hash__
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.__ne__
      ~abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.__repr__

Bases
-----

- :py:class:`developerscripttools.DeveloperScript <abjad.tools.developerscripttools.DeveloperScript.DeveloperScript>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.alias
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.argument_parser
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.colors
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.developer_script_aliases
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.developer_script_classes
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.developer_script_program_names
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.formatted_help
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.formatted_usage
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.formatted_version
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.long_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.program_name
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.scripting_group
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.short_description
   :noindex:

.. autoattribute:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.version
   :noindex:

Methods
-------

.. automethod:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.process_args
   :noindex:

.. automethod:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.setup_argument_parser
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.__call__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.__eq__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.__format__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.__hash__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.__ne__
   :noindex:

.. automethod:: abjad.tools.developerscripttools.AbjDevScript.AbjDevScript.__repr__
   :noindex:
