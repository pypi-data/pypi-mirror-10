datastructuretools.CyclicPayloadTree
====================================

.. autoclass:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree

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
           "datastructuretools.CyclicPayloadTree" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>CyclicPayloadTree</B>>,
               shape=box,
               style="filled, rounded"];
           "datastructuretools.PayloadTree" [color=3,
               group=2,
               label=PayloadTree,
               shape=box];
           "datastructuretools.PayloadTree" -> "datastructuretools.CyclicPayloadTree";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.PayloadTree";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.children
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.depth
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.expr
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.get_manifest_payload_of_next_n_nodes_at_level
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.get_next_n_complete_nodes_at_level
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.get_next_n_nodes_at_level
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.get_node_at_position
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.get_position_of_descendant
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.improper_parentage
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.index
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.index_in_parent
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.is_at_level
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.item_class
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.iterate_at_level
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.iterate_depth_first
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.iterate_forever_depth_first
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.iterate_payload
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.level
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.manifest_payload
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.negative_level
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.payload
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.position
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.proper_parentage
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.remove_node
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.remove_to_root
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.root
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.to_nested_lists
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.width
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__contains__
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__eq__
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__format__
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__getitem__
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__graph__
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__hash__
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__iter__
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__len__
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__ne__
      ~abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__repr__

Bases
-----

- :py:class:`datastructuretools.PayloadTree <abjad.tools.datastructuretools.PayloadTree.PayloadTree>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.children
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.depth
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.expr
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.index_in_parent
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.item_class
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.level
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.manifest_payload
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.negative_level
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.payload
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.position
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.root
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.width
   :noindex:

Methods
-------

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.get_manifest_payload_of_next_n_nodes_at_level
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.get_next_n_complete_nodes_at_level
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.get_next_n_nodes_at_level
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.get_node_at_position
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.get_position_of_descendant
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.index
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.is_at_level
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.iterate_at_level
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.iterate_depth_first
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.iterate_forever_depth_first
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.iterate_payload
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.remove_node
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.remove_to_root
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.to_nested_lists
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__contains__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__eq__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__format__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__getitem__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__graph__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__hash__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__iter__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__len__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__ne__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicPayloadTree.CyclicPayloadTree.__repr__
   :noindex:
