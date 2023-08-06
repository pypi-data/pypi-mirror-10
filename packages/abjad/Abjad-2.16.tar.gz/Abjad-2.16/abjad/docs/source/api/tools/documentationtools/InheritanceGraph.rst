documentationtools.InheritanceGraph
===================================

.. autoclass:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph

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
           "documentationtools.InheritanceGraph" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>InheritanceGraph</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "documentationtools.InheritanceGraph";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.addresses
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.child_parents_mapping
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.immediate_classes
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.lineage_addresses
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.lineage_classes
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.lineage_distance_mapping
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.lineage_prune_distance
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.parent_children_mapping
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.recurse_into_submodules
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.root_addresses
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.root_classes
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.use_clusters
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.use_groups
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.__eq__
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.__format__
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.__graph__
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.__hash__
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.__ne__
      ~abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.addresses
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.child_parents_mapping
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.immediate_classes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.lineage_addresses
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.lineage_classes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.lineage_distance_mapping
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.lineage_prune_distance
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.parent_children_mapping
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.recurse_into_submodules
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.root_addresses
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.root_classes
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.use_clusters
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.use_groups
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.__graph__
   :noindex:

.. automethod:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.InheritanceGraph.InheritanceGraph.__repr__
   :noindex:
