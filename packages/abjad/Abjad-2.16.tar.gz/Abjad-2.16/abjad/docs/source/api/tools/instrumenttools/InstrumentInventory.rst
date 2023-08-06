instrumenttools.InstrumentInventory
===================================

.. autoclass:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory

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
           "instrumenttools.InstrumentInventory" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>InstrumentInventory</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedList" -> "instrumenttools.InstrumentInventory";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.append
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.count
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.extend
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.index
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.insert
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.item_class
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.items
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.keep_sorted
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.pop
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.remove
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.reverse
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.sort
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__contains__
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__delitem__
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__eq__
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__format__
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__getitem__
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__hash__
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__iadd__
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__iter__
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__len__
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__ne__
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__repr__
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__reversed__
      ~abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__setitem__

Bases
-----

- :py:class:`datastructuretools.TypedList <abjad.tools.datastructuretools.TypedList.TypedList>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.item_class
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.items
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.keep_sorted
   :noindex:

Methods
-------

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.append
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.count
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.extend
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.index
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.insert
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.pop
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.remove
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.reverse
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.sort
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__contains__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__delitem__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__eq__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__format__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__getitem__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__hash__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__iadd__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__iter__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__len__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__ne__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__repr__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__reversed__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.InstrumentInventory.InstrumentInventory.__setitem__
   :noindex:
