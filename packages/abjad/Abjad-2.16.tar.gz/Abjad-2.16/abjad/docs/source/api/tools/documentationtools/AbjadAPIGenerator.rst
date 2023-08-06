documentationtools.AbjadAPIGenerator
====================================

.. autoclass:: abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator

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
           "documentationtools.AbjadAPIGenerator" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>AbjadAPIGenerator</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "documentationtools.AbjadAPIGenerator";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.docs_api_index_path
      ~abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.package_prefix
      ~abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.path_definitions
      ~abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.root_package
      ~abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.tools_package_path_index
      ~abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.__call__
      ~abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.__eq__
      ~abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.__format__
      ~abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.__hash__
      ~abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.__ne__
      ~abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.docs_api_index_path
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.package_prefix
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.path_definitions
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.root_package
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.tools_package_path_index
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.__call__
   :noindex:

.. automethod:: abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.AbjadAPIGenerator.AbjadAPIGenerator.__repr__
   :noindex:
