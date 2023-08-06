markuptools.MarkupInventory
===========================

.. autoclass:: abjad.tools.markuptools.MarkupInventory.MarkupInventory

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
       subgraph cluster_markuptools {
           graph [label=markuptools];
           "markuptools.MarkupInventory" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>MarkupInventory</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedList" -> "markuptools.MarkupInventory";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.append
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.count
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.extend
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.index
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.insert
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.item_class
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.items
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.keep_sorted
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.pop
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.remove
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.reverse
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.sort
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.__contains__
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.__delitem__
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.__eq__
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.__format__
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.__getitem__
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.__hash__
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.__iadd__
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.__illustrate__
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.__iter__
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.__len__
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.__ne__
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.__repr__
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.__reversed__
      ~abjad.tools.markuptools.MarkupInventory.MarkupInventory.__setitem__

Bases
-----

- :py:class:`datastructuretools.TypedList <abjad.tools.datastructuretools.TypedList.TypedList>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.item_class
   :noindex:

.. autoattribute:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.items
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.keep_sorted
   :noindex:

Methods
-------

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.append
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.count
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.extend
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.index
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.insert
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.pop
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.remove
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.reverse
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.sort
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.__contains__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.__delitem__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.__eq__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.__format__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.__getitem__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.__hash__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.__iadd__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.__illustrate__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.__iter__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.__len__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.__ne__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.__repr__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.__reversed__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupInventory.MarkupInventory.__setitem__
   :noindex:
