pitchtools.PitchRangeInventory
==============================

.. autoclass:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory

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
       subgraph cluster_pitchtools {
           graph [label=pitchtools];
           "pitchtools.PitchRangeInventory" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>PitchRangeInventory</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedList" -> "pitchtools.PitchRangeInventory";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.append
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.count
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.extend
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.index
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.insert
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.item_class
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.items
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.keep_sorted
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.pop
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.remove
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.reverse
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.sort
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__contains__
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__delitem__
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__eq__
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__format__
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__getitem__
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__hash__
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__iadd__
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__illustrate__
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__iter__
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__len__
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__ne__
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__repr__
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__reversed__
      ~abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__setitem__

Bases
-----

- :py:class:`datastructuretools.TypedList <abjad.tools.datastructuretools.TypedList.TypedList>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.item_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.items
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.keep_sorted
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.append
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.count
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.extend
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.index
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.insert
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.pop
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.remove
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.reverse
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.sort
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__contains__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__delitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__getitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__iadd__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__illustrate__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__iter__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__len__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__reversed__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchRangeInventory.PitchRangeInventory.__setitem__
   :noindex:
