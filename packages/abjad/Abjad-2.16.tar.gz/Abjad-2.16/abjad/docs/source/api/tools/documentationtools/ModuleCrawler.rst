documentationtools.ModuleCrawler
================================

.. autoclass:: abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler

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
           "documentationtools.ModuleCrawler" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>ModuleCrawler</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "documentationtools.ModuleCrawler";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.code_root
      ~abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.ignored_directory_names
      ~abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.root_package_name
      ~abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.visit_private_modules
      ~abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.__eq__
      ~abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.__format__
      ~abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.__hash__
      ~abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.__iter__
      ~abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.__ne__
      ~abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.code_root
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.ignored_directory_names
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.root_package_name
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.visit_private_modules
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.__iter__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.ModuleCrawler.ModuleCrawler.__repr__
   :noindex:
