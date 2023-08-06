documentationtools.FunctionCrawler
==================================

.. autoclass:: abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler

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
           "documentationtools.FunctionCrawler" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>FunctionCrawler</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "documentationtools.FunctionCrawler";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.code_root
      ~abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.include_private_objects
      ~abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.module_crawler
      ~abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.root_package_name
      ~abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.__call__
      ~abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.__eq__
      ~abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.__format__
      ~abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.__hash__
      ~abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.__ne__
      ~abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.code_root
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.include_private_objects
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.module_crawler
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.root_package_name
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.__call__
   :noindex:

.. automethod:: abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.FunctionCrawler.FunctionCrawler.__repr__
   :noindex:
