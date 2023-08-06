pitchtools.IntervalClassVector
==============================

.. autoclass:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector

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
       subgraph cluster_pitchtools {
           graph [label=pitchtools];
           "pitchtools.IntervalClassVector" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>IntervalClassVector</B>>,
               shape=box,
               style="filled, rounded"];
           "pitchtools.Vector" [color=4,
               group=3,
               label=Vector,
               shape=oval,
               style=bold];
           "pitchtools.Vector" -> "pitchtools.IntervalClassVector";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedCounter" -> "pitchtools.Vector";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.clear
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.copy
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.elements
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.from_selection
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.item_class
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.items
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.keys
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.most_common
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.subtract
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.update
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.values
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.viewitems
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.viewkeys
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.viewvalues
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__add__
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__and__
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__contains__
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__delitem__
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__eq__
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__format__
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__getitem__
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__hash__
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__iter__
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__len__
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__missing__
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__ne__
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__or__
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__repr__
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__setitem__
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__str__
      ~abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__sub__

Bases
-----

- :py:class:`pitchtools.Vector <abjad.tools.pitchtools.Vector.Vector>`

- :py:class:`datastructuretools.TypedCounter <abjad.tools.datastructuretools.TypedCounter.TypedCounter>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.item_class
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.clear
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.copy
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.elements
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.items
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.keys
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.most_common
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.subtract
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.update
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.values
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.viewitems
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.viewkeys
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.viewvalues
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.from_selection
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__add__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__and__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__contains__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__delitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__getitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__iter__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__len__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__missing__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__or__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__setitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__str__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalClassVector.IntervalClassVector.__sub__
   :noindex:
