metertools.MeterInventory
=========================

.. autoclass:: abjad.tools.metertools.MeterInventory.MeterInventory

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
       subgraph cluster_metertools {
           graph [label=metertools];
           "metertools.MeterInventory" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>MeterInventory</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedList" -> "metertools.MeterInventory";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.metertools.MeterInventory.MeterInventory.append
      ~abjad.tools.metertools.MeterInventory.MeterInventory.count
      ~abjad.tools.metertools.MeterInventory.MeterInventory.extend
      ~abjad.tools.metertools.MeterInventory.MeterInventory.index
      ~abjad.tools.metertools.MeterInventory.MeterInventory.insert
      ~abjad.tools.metertools.MeterInventory.MeterInventory.item_class
      ~abjad.tools.metertools.MeterInventory.MeterInventory.items
      ~abjad.tools.metertools.MeterInventory.MeterInventory.keep_sorted
      ~abjad.tools.metertools.MeterInventory.MeterInventory.pop
      ~abjad.tools.metertools.MeterInventory.MeterInventory.remove
      ~abjad.tools.metertools.MeterInventory.MeterInventory.reverse
      ~abjad.tools.metertools.MeterInventory.MeterInventory.sort
      ~abjad.tools.metertools.MeterInventory.MeterInventory.__contains__
      ~abjad.tools.metertools.MeterInventory.MeterInventory.__delitem__
      ~abjad.tools.metertools.MeterInventory.MeterInventory.__eq__
      ~abjad.tools.metertools.MeterInventory.MeterInventory.__format__
      ~abjad.tools.metertools.MeterInventory.MeterInventory.__getitem__
      ~abjad.tools.metertools.MeterInventory.MeterInventory.__hash__
      ~abjad.tools.metertools.MeterInventory.MeterInventory.__iadd__
      ~abjad.tools.metertools.MeterInventory.MeterInventory.__illustrate__
      ~abjad.tools.metertools.MeterInventory.MeterInventory.__iter__
      ~abjad.tools.metertools.MeterInventory.MeterInventory.__len__
      ~abjad.tools.metertools.MeterInventory.MeterInventory.__ne__
      ~abjad.tools.metertools.MeterInventory.MeterInventory.__repr__
      ~abjad.tools.metertools.MeterInventory.MeterInventory.__reversed__
      ~abjad.tools.metertools.MeterInventory.MeterInventory.__setitem__

Bases
-----

- :py:class:`datastructuretools.TypedList <abjad.tools.datastructuretools.TypedList.TypedList>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.metertools.MeterInventory.MeterInventory.item_class
   :noindex:

.. autoattribute:: abjad.tools.metertools.MeterInventory.MeterInventory.items
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.metertools.MeterInventory.MeterInventory.keep_sorted
   :noindex:

Methods
-------

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.append
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.count
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.extend
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.index
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.insert
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.pop
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.remove
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.reverse
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.sort
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.__contains__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.__delitem__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.__eq__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.__format__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.__getitem__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.__hash__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.__iadd__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.__illustrate__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.__iter__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.__len__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.__ne__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.__repr__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.__reversed__
   :noindex:

.. automethod:: abjad.tools.metertools.MeterInventory.MeterInventory.__setitem__
   :noindex:
