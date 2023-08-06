datastructuretools.PayloadTree
==============================

.. autoclass:: abjad.tools.datastructuretools.PayloadTree.PayloadTree

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
       subgraph cluster_datastructuretools {
           graph [label=datastructuretools];
           "datastructuretools.CyclicPayloadTree" [color=3,
               group=2,
               label=CyclicPayloadTree,
               shape=box];
           "datastructuretools.PayloadTree" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>PayloadTree</B>>,
               shape=box,
               style="filled, rounded"];
           "datastructuretools.PayloadTree" -> "datastructuretools.CyclicPayloadTree";
       }
       subgraph cluster_pitchtools {
           graph [label=pitchtools];
           "pitchtools.PitchClassTree" [color=4,
               group=3,
               label=PitchClassTree,
               shape=box];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.PayloadTree";
       "datastructuretools.PayloadTree" -> "pitchtools.PitchClassTree";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.children
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.depth
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.expr
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.get_manifest_payload_of_next_n_nodes_at_level
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.get_next_n_complete_nodes_at_level
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.get_next_n_nodes_at_level
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.get_node_at_position
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.get_position_of_descendant
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.improper_parentage
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.index
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.index_in_parent
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.is_at_level
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.item_class
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.iterate_at_level
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.iterate_depth_first
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.iterate_payload
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.level
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.manifest_payload
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.negative_level
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.payload
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.position
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.proper_parentage
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.remove_node
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.remove_to_root
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.root
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.to_nested_lists
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.width
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.__contains__
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.__eq__
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.__format__
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.__getitem__
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.__graph__
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.__hash__
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.__len__
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.__ne__
      ~abjad.tools.datastructuretools.PayloadTree.PayloadTree.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.children
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.depth
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.expr
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.index_in_parent
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.item_class
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.level
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.manifest_payload
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.negative_level
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.payload
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.position
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.root
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.width
   :noindex:

Methods
-------

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.get_manifest_payload_of_next_n_nodes_at_level
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.get_next_n_complete_nodes_at_level
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.get_next_n_nodes_at_level
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.get_node_at_position
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.get_position_of_descendant
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.index
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.is_at_level
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.iterate_at_level
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.iterate_depth_first
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.iterate_payload
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.remove_node
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.remove_to_root
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.to_nested_lists
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.__contains__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.__eq__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.__format__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.__getitem__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.__graph__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.__hash__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.__len__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.__ne__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.PayloadTree.PayloadTree.__repr__
   :noindex:
