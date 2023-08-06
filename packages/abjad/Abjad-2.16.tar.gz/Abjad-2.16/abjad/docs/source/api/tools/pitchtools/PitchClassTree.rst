pitchtools.PitchClassTree
=========================

.. autoclass:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree

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
           "datastructuretools.PayloadTree" [color=3,
               group=2,
               label=PayloadTree,
               shape=box];
       }
       subgraph cluster_pitchtools {
           graph [label=pitchtools];
           "pitchtools.PitchClassTree" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>PitchClassTree</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.PayloadTree";
       "datastructuretools.PayloadTree" -> "pitchtools.PitchClassTree";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.children
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.depth
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.expr
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.get_manifest_payload_of_next_n_nodes_at_level
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.get_next_n_complete_nodes_at_level
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.get_next_n_nodes_at_level
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.get_node_at_position
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.get_position_of_descendant
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.improper_parentage
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.index
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.index_in_parent
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.is_at_level
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.item_class
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.iterate_at_level
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.iterate_depth_first
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.iterate_payload
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.level
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.manifest_payload
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.negative_level
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.payload
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.position
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.proper_parentage
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.remove_node
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.remove_to_root
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.root
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.to_nested_lists
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.width
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__contains__
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__eq__
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__format__
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__getitem__
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__graph__
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__hash__
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__illustrate__
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__len__
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__ne__
      ~abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__repr__

Bases
-----

- :py:class:`datastructuretools.PayloadTree <abjad.tools.datastructuretools.PayloadTree.PayloadTree>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.children
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.depth
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.expr
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.improper_parentage
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.index_in_parent
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.item_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.level
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.manifest_payload
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.negative_level
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.payload
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.position
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.proper_parentage
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.root
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.width
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.get_manifest_payload_of_next_n_nodes_at_level
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.get_next_n_complete_nodes_at_level
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.get_next_n_nodes_at_level
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.get_node_at_position
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.get_position_of_descendant
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.index
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.is_at_level
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.iterate_at_level
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.iterate_depth_first
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.iterate_payload
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.remove_node
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.remove_to_root
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.to_nested_lists
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__contains__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__getitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__graph__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__illustrate__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__len__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchClassTree.PitchClassTree.__repr__
   :noindex:
