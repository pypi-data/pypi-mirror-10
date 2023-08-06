instrumenttools.PerformerInventory
==================================

.. autoclass:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory

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
       subgraph cluster_instrumenttools {
           graph [label=instrumenttools];
           "instrumenttools.PerformerInventory" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>PerformerInventory</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedList" -> "instrumenttools.PerformerInventory";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.append
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.count
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.extend
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.get_instrument
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.index
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.insert
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.item_class
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.items
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.keep_sorted
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.pop
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.remove
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.reverse
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.sort
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__contains__
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__delitem__
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__eq__
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__format__
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__getitem__
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__hash__
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__iadd__
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__iter__
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__len__
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__ne__
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__repr__
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__reversed__
      ~abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__setitem__

Bases
-----

- :py:class:`datastructuretools.TypedList <abjad.tools.datastructuretools.TypedList.TypedList>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.item_class
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.items
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.keep_sorted
   :noindex:

Methods
-------

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.append
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.count
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.extend
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.get_instrument
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.index
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.insert
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.pop
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.remove
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.reverse
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.sort
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__contains__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__delitem__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__eq__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__format__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__getitem__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__hash__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__iadd__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__iter__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__len__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__ne__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__repr__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__reversed__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.PerformerInventory.PerformerInventory.__setitem__
   :noindex:
