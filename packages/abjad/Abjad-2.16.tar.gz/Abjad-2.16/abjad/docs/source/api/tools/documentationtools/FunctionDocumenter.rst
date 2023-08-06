documentationtools.FunctionDocumenter
=====================================

.. autoclass:: abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter

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
           "documentationtools.FunctionDocumenter" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>FunctionDocumenter</B>>,
               shape=box,
               style="filled, rounded"];
           "documentationtools.Documenter" -> "documentationtools.FunctionDocumenter";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "documentationtools.Documenter";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.module_name
      ~abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.prefix
      ~abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.subject
      ~abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.write
      ~abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.__call__
      ~abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.__eq__
      ~abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.__format__
      ~abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.__hash__
      ~abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.__ne__
      ~abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.__repr__

Bases
-----

- :py:class:`documentationtools.Documenter <abjad.tools.documentationtools.Documenter.Documenter>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.module_name
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.prefix
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.subject
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.write
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.__call__
   :noindex:

.. automethod:: abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.FunctionDocumenter.FunctionDocumenter.__repr__
   :noindex:
