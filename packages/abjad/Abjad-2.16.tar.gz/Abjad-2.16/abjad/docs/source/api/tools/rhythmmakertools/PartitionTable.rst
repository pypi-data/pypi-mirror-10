rhythmmakertools.PartitionTable
===============================

.. autoclass:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable

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
           "datastructuretools.TypedCollection" [color=3,
               group=2,
               label=TypedCollection,
               shape=oval,
               style=bold];
           "datastructuretools.TypedOrderedDict" [color=3,
               group=2,
               label=TypedOrderedDict,
               shape=box];
           "datastructuretools.TypedCollection" -> "datastructuretools.TypedOrderedDict";
       }
       subgraph cluster_rhythmmakertools {
           graph [label=rhythmmakertools];
           "rhythmmakertools.PartitionTable" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>PartitionTable</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedOrderedDict" -> "rhythmmakertools.PartitionTable";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.clear
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.copy
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.get
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.has_key
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.item_class
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.items
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.keys
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.pop
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.popitem
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.respell_division
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.setdefault
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.update
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.values
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__cmp__
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__contains__
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__delitem__
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__eq__
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__format__
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__ge__
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__getitem__
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__gt__
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__hash__
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__iter__
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__le__
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__len__
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__lt__
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__ne__
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__repr__
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__reversed__
      ~abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__setitem__

Bases
-----

- :py:class:`datastructuretools.TypedOrderedDict <abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.item_class
   :noindex:

Methods
-------

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.clear
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.copy
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.get
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.has_key
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.items
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.keys
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.pop
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.popitem
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.respell_division
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.setdefault
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.update
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.values
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__cmp__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__contains__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__delitem__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__ge__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__getitem__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__gt__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__iter__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__le__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__len__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__lt__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__repr__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__reversed__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.PartitionTable.PartitionTable.__setitem__
   :noindex:
