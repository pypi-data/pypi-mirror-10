selectiontools.SelectionInventory
=================================

.. autoclass:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory

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
       subgraph cluster_selectiontools {
           graph [label=selectiontools];
           "selectiontools.SelectionInventory" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>SelectionInventory</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedList" -> "selectiontools.SelectionInventory";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.append
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.count
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.extend
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.index
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.insert
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.item_class
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.items
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.keep_sorted
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.pop
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.remove
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.reverse
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.sort
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__contains__
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__delitem__
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__eq__
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__format__
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__getitem__
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__hash__
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__iadd__
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__iter__
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__len__
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__ne__
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__repr__
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__reversed__
      ~abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__setitem__

Bases
-----

- :py:class:`datastructuretools.TypedList <abjad.tools.datastructuretools.TypedList.TypedList>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.item_class
   :noindex:

.. autoattribute:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.items
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.keep_sorted
   :noindex:

Methods
-------

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.append
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.count
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.extend
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.index
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.insert
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.pop
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.remove
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.reverse
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.sort
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__contains__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__delitem__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__eq__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__format__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__getitem__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__hash__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__iadd__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__iter__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__len__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__ne__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__repr__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__reversed__
   :noindex:

.. automethod:: abjad.tools.selectiontools.SelectionInventory.SelectionInventory.__setitem__
   :noindex:
