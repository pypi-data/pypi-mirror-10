documentationtools.ClassDocumenter
==================================

.. autoclass:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter

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
           "documentationtools.ClassDocumenter" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>ClassDocumenter</B>>,
               shape=box,
               style="filled, rounded"];
           "documentationtools.Documenter" [color=3,
               group=2,
               label=Documenter,
               shape=box];
           "documentationtools.Documenter" -> "documentationtools.ClassDocumenter";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "documentationtools.Documenter";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.class_methods
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.data
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.inherited_attributes
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.is_abstract
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.methods
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.module_name
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.prefix
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.readonly_properties
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.readwrite_properties
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.special_methods
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.static_methods
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.subject
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.write
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.__call__
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.__eq__
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.__format__
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.__hash__
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.__ne__
      ~abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.__repr__

Bases
-----

- :py:class:`documentationtools.Documenter <abjad.tools.documentationtools.Documenter.Documenter>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.class_methods
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.data
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.inherited_attributes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.is_abstract
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.methods
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.module_name
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.prefix
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.readonly_properties
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.readwrite_properties
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.special_methods
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.static_methods
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.subject
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.write
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.__call__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ClassDocumenter.ClassDocumenter.__repr__
   :noindex:
