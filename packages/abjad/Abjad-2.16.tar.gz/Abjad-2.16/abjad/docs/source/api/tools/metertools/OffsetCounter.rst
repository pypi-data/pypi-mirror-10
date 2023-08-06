metertools.OffsetCounter
========================

.. autoclass:: abjad.tools.metertools.OffsetCounter.OffsetCounter

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
           "datastructuretools.TypedCounter" [color=3,
               group=2,
               label=TypedCounter,
               shape=box];
           "datastructuretools.TypedCollection" -> "datastructuretools.TypedCounter";
       }
       subgraph cluster_metertools {
           graph [label=metertools];
           "metertools.OffsetCounter" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>OffsetCounter</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedCounter" -> "metertools.OffsetCounter";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.clear
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.copy
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.elements
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.item_class
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.items
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.keys
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.most_common
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.subtract
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.update
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.values
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.viewitems
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.viewkeys
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.viewvalues
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.__add__
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.__and__
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.__contains__
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.__delitem__
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.__eq__
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.__format__
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.__getitem__
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.__hash__
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.__illustrate__
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.__iter__
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.__len__
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.__missing__
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.__ne__
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.__or__
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.__repr__
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.__setitem__
      ~abjad.tools.metertools.OffsetCounter.OffsetCounter.__sub__

Bases
-----

- :py:class:`datastructuretools.TypedCounter <abjad.tools.datastructuretools.TypedCounter.TypedCounter>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.metertools.OffsetCounter.OffsetCounter.item_class
   :noindex:

Methods
-------

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.clear
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.copy
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.elements
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.items
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.keys
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.most_common
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.subtract
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.update
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.values
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.viewitems
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.viewkeys
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.viewvalues
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.__add__
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.__and__
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.__contains__
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.__delitem__
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.__eq__
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.__format__
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.__getitem__
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.__hash__
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.__illustrate__
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.__iter__
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.__len__
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.__missing__
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.__ne__
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.__or__
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.__repr__
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.__setitem__
   :noindex:

.. automethod:: abjad.tools.metertools.OffsetCounter.OffsetCounter.__sub__
   :noindex:
