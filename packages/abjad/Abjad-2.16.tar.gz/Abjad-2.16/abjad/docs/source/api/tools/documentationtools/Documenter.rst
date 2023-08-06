documentationtools.Documenter
=============================

.. autoclass:: abjad.tools.documentationtools.Documenter.Documenter

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
           "documentationtools.ClassDocumenter" [color=3,
               group=2,
               label=ClassDocumenter,
               shape=box];
           "documentationtools.Documenter" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Documenter</B>>,
               shape=box,
               style="filled, rounded"];
           "documentationtools.FunctionDocumenter" [color=3,
               group=2,
               label=FunctionDocumenter,
               shape=box];
           "documentationtools.ToolsPackageDocumenter" [color=3,
               group=2,
               label=ToolsPackageDocumenter,
               shape=box];
           "documentationtools.Documenter" -> "documentationtools.ClassDocumenter";
           "documentationtools.Documenter" -> "documentationtools.FunctionDocumenter";
           "documentationtools.Documenter" -> "documentationtools.ToolsPackageDocumenter";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "documentationtools.Documenter";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.Documenter.Documenter.module_name
      ~abjad.tools.documentationtools.Documenter.Documenter.prefix
      ~abjad.tools.documentationtools.Documenter.Documenter.subject
      ~abjad.tools.documentationtools.Documenter.Documenter.write
      ~abjad.tools.documentationtools.Documenter.Documenter.__eq__
      ~abjad.tools.documentationtools.Documenter.Documenter.__format__
      ~abjad.tools.documentationtools.Documenter.Documenter.__hash__
      ~abjad.tools.documentationtools.Documenter.Documenter.__ne__
      ~abjad.tools.documentationtools.Documenter.Documenter.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.Documenter.Documenter.module_name
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.Documenter.Documenter.prefix
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.Documenter.Documenter.subject
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.documentationtools.Documenter.Documenter.write
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.Documenter.Documenter.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.Documenter.Documenter.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.Documenter.Documenter.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.Documenter.Documenter.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.Documenter.Documenter.__repr__
   :noindex:
