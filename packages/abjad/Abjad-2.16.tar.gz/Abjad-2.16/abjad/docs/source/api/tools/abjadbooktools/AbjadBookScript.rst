abjadbooktools.AbjadBookScript
==============================

.. autoclass:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript

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
           "abjadbooktools.AbjadBookScript" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>AbjadBookScript</B>>,
               shape=box,
               style="filled, rounded"];
       }
       subgraph cluster_developerscripttools {
           graph [label=developerscripttools];
           "developerscripttools.DeveloperScript" [color=4,
               group=3,
               label=DeveloperScript,
               shape=oval,
               style=bold];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "developerscripttools.DeveloperScript";
       "developerscripttools.DeveloperScript" -> "abjadbooktools.AbjadBookScript";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.alias
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.argument_parser
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.colors
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.formatted_help
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.formatted_usage
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.formatted_version
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.long_description
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.output_formats
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.process_args
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.program_name
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.scripting_group
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.setup_argument_parser
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.short_description
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.version
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.__call__
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.__eq__
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.__format__
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.__hash__
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.__ne__
      ~abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.__repr__

Bases
-----

- :py:class:`developerscripttools.DeveloperScript <abjad.tools.developerscripttools.DeveloperScript.DeveloperScript>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.alias
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.argument_parser
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.colors
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.formatted_help
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.formatted_usage
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.formatted_version
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.long_description
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.output_formats
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.program_name
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.scripting_group
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.short_description
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.version
   :noindex:

Methods
-------

.. automethod:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.process_args
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.setup_argument_parser
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.__call__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.__eq__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.__format__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.__hash__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.__ne__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.AbjadBookScript.AbjadBookScript.__repr__
   :noindex:
