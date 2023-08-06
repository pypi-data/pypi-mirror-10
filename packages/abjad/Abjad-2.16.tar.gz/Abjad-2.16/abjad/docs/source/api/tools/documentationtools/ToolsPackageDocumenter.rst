documentationtools.ToolsPackageDocumenter
=========================================

.. autoclass:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter

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
       subgraph cluster_documentationtools {
           graph [label=documentationtools];
           "documentationtools.Documenter" [color=3,
               group=2,
               label=Documenter,
               shape=box];
           "documentationtools.ToolsPackageDocumenter" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>ToolsPackageDocumenter</B>>,
               shape=box,
               style="filled, rounded"];
           "documentationtools.Documenter" -> "documentationtools.ToolsPackageDocumenter";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "documentationtools.Documenter";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.abstract_class_documenters
      ~abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.all_documenters
      ~abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.concrete_class_documenters
      ~abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.create_api_toc_section
      ~abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.documentation_section
      ~abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.function_documenters
      ~abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.ignored_directory_names
      ~abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.module_name
      ~abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.prefix
      ~abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.subject
      ~abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.write
      ~abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.__call__
      ~abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.__eq__
      ~abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.__format__
      ~abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.__hash__
      ~abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.__ne__
      ~abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.__repr__

Bases
-----

- :py:class:`documentationtools.Documenter <abjad.tools.documentationtools.Documenter.Documenter>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.abstract_class_documenters
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.all_documenters
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.concrete_class_documenters
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.documentation_section
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.function_documenters
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.ignored_directory_names
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.module_name
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.prefix
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.subject
   :noindex:

Methods
-------

.. automethod:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.create_api_toc_section
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.write
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.__call__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ToolsPackageDocumenter.ToolsPackageDocumenter.__repr__
   :noindex:
