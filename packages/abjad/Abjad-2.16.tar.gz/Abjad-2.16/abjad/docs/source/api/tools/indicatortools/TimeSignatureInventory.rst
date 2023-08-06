indicatortools.TimeSignatureInventory
=====================================

.. autoclass:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory

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
       subgraph cluster_indicatortools {
           graph [label=indicatortools];
           "indicatortools.TimeSignatureInventory" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>TimeSignatureInventory</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedList" -> "indicatortools.TimeSignatureInventory";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.append
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.count
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.extend
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.index
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.insert
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.item_class
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.items
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.keep_sorted
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.pop
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.remove
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.reverse
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.sort
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__contains__
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__delitem__
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__eq__
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__format__
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__getitem__
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__hash__
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__iadd__
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__illustrate__
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__iter__
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__len__
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__ne__
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__repr__
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__reversed__
      ~abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__setitem__

Bases
-----

- :py:class:`datastructuretools.TypedList <abjad.tools.datastructuretools.TypedList.TypedList>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.item_class
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.items
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.keep_sorted
   :noindex:

Methods
-------

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.append
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.count
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.extend
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.index
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.insert
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.pop
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.remove
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.reverse
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.sort
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__contains__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__delitem__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__eq__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__format__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__getitem__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__hash__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__iadd__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__illustrate__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__iter__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__len__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__ne__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__repr__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__reversed__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignatureInventory.TimeSignatureInventory.__setitem__
   :noindex:
