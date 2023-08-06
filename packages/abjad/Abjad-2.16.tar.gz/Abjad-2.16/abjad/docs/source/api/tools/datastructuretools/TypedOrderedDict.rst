datastructuretools.TypedOrderedDict
===================================

.. autoclass:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict

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
           "datastructuretools.TypedOrderedDict" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>TypedOrderedDict</B>>,
               shape=box,
               style="filled, rounded"];
           "datastructuretools.TypedCollection" -> "datastructuretools.TypedOrderedDict";
       }
       subgraph cluster_rhythmmakertools {
           graph [label=rhythmmakertools];
           "rhythmmakertools.PartitionTable" [color=5,
               group=4,
               label=PartitionTable,
               shape=box];
       }
       subgraph cluster_ide {
           graph [label=ide];
           "ide.idetools.ViewInventory" [color=4,
               group=3,
               label=ViewInventory,
               shape=box];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedOrderedDict" -> "rhythmmakertools.PartitionTable";
       "datastructuretools.TypedOrderedDict" -> "ide.idetools.ViewInventory";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.clear
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.copy
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.get
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.has_key
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.item_class
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.items
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.keys
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.pop
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.popitem
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.setdefault
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.update
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.values
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__cmp__
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__contains__
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__delitem__
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__eq__
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__format__
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__ge__
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__getitem__
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__gt__
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__hash__
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__iter__
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__le__
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__len__
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__lt__
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__ne__
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__repr__
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__reversed__
      ~abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__setitem__

Bases
-----

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.item_class
   :noindex:

Methods
-------

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.clear
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.copy
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.get
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.has_key
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.items
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.keys
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.pop
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.popitem
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.setdefault
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.update
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.values
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__cmp__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__contains__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__delitem__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__eq__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__format__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__ge__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__getitem__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__gt__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__hash__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__iter__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__le__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__len__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__lt__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__ne__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__repr__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__reversed__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedOrderedDict.TypedOrderedDict.__setitem__
   :noindex:
