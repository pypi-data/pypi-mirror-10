datastructuretools.TypedCounter
===============================

.. autoclass:: abjad.tools.datastructuretools.TypedCounter.TypedCounter

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
           "datastructuretools.TypedCounter" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>TypedCounter</B>>,
               shape=box,
               style="filled, rounded"];
           "datastructuretools.TypedCollection" -> "datastructuretools.TypedCounter";
       }
       subgraph cluster_metertools {
           graph [label=metertools];
           "metertools.OffsetCounter" [color=4,
               group=3,
               label=OffsetCounter,
               shape=box];
       }
       subgraph cluster_pitchtools {
           graph [label=pitchtools];
           "pitchtools.IntervalClassVector" [color=5,
               group=4,
               label=IntervalClassVector,
               shape=box];
           "pitchtools.IntervalVector" [color=5,
               group=4,
               label=IntervalVector,
               shape=box];
           "pitchtools.PitchClassVector" [color=5,
               group=4,
               label=PitchClassVector,
               shape=box];
           "pitchtools.PitchVector" [color=5,
               group=4,
               label=PitchVector,
               shape=box];
           "pitchtools.Vector" [color=5,
               group=4,
               label=Vector,
               shape=oval,
               style=bold];
           "pitchtools.Vector" -> "pitchtools.IntervalClassVector";
           "pitchtools.Vector" -> "pitchtools.IntervalVector";
           "pitchtools.Vector" -> "pitchtools.PitchClassVector";
           "pitchtools.Vector" -> "pitchtools.PitchVector";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedCounter" -> "metertools.OffsetCounter";
       "datastructuretools.TypedCounter" -> "pitchtools.Vector";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.clear
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.copy
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.elements
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.item_class
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.items
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.keys
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.most_common
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.subtract
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.update
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.values
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.viewitems
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.viewkeys
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.viewvalues
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.__add__
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.__and__
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.__contains__
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.__delitem__
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.__eq__
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.__format__
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.__getitem__
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.__hash__
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.__iter__
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.__len__
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.__missing__
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.__ne__
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.__or__
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.__repr__
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.__setitem__
      ~abjad.tools.datastructuretools.TypedCounter.TypedCounter.__sub__

Bases
-----

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.item_class
   :noindex:

Methods
-------

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.clear
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.copy
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.elements
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.items
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.keys
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.most_common
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.subtract
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.update
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.values
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.viewitems
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.viewkeys
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.viewvalues
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.__add__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.__and__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.__contains__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.__delitem__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.__eq__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.__format__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.__getitem__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.__hash__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.__iter__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.__len__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.__missing__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.__ne__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.__or__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.__repr__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.__setitem__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedCounter.TypedCounter.__sub__
   :noindex:
