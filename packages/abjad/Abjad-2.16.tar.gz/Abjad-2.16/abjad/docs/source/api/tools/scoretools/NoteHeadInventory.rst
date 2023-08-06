scoretools.NoteHeadInventory
============================

.. autoclass:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory

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
           "datastructuretools.TypedList" [color=3,
               group=2,
               label=TypedList,
               shape=box];
           "datastructuretools.TypedCollection" -> "datastructuretools.TypedList";
       }
       subgraph cluster_scoretools {
           graph [label=scoretools];
           "scoretools.NoteHeadInventory" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>NoteHeadInventory</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedList" -> "scoretools.NoteHeadInventory";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.append
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.client
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.count
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.extend
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.get
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.index
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.insert
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.item_class
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.items
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.keep_sorted
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.pop
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.remove
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.reverse
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.sort
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__contains__
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__delitem__
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__eq__
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__format__
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__getitem__
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__hash__
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__iadd__
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__iter__
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__len__
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__ne__
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__repr__
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__reversed__
      ~abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__setitem__

Bases
-----

- :py:class:`datastructuretools.TypedList <abjad.tools.datastructuretools.TypedList.TypedList>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.client
   :noindex:

.. autoattribute:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.item_class
   :noindex:

.. autoattribute:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.items
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.keep_sorted
   :noindex:

Methods
-------

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.append
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.count
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.extend
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.get
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.index
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.insert
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.pop
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.remove
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.reverse
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.sort
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__contains__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__delitem__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__eq__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__format__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__getitem__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__hash__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__iadd__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__iter__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__len__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__ne__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__repr__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__reversed__
   :noindex:

.. automethod:: abjad.tools.scoretools.NoteHeadInventory.NoteHeadInventory.__setitem__
   :noindex:
