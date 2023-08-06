systemtools.ImportManager
=========================

.. autoclass:: abjad.tools.systemtools.ImportManager.ImportManager

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
       subgraph cluster_systemtools {
           graph [label=systemtools];
           "systemtools.ImportManager" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>ImportManager</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "systemtools.ImportManager";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.systemtools.ImportManager.ImportManager.import_material_packages
      ~abjad.tools.systemtools.ImportManager.ImportManager.import_nominative_modules
      ~abjad.tools.systemtools.ImportManager.ImportManager.import_public_names_from_path_into_namespace
      ~abjad.tools.systemtools.ImportManager.ImportManager.import_structured_package

Bases
-----

- :py:class:`__builtin__.object <object>`

Static methods
--------------

.. automethod:: abjad.tools.systemtools.ImportManager.ImportManager.import_material_packages
   :noindex:

.. automethod:: abjad.tools.systemtools.ImportManager.ImportManager.import_nominative_modules
   :noindex:

.. automethod:: abjad.tools.systemtools.ImportManager.ImportManager.import_public_names_from_path_into_namespace
   :noindex:

.. automethod:: abjad.tools.systemtools.ImportManager.ImportManager.import_structured_package
   :noindex:
