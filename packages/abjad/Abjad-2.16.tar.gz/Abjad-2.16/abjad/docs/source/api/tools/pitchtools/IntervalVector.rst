pitchtools.IntervalVector
=========================

.. autoclass:: abjad.tools.pitchtools.IntervalVector.IntervalVector

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
           "pitchtools.IntervalVector" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>IntervalVector</B>>,
               shape=box,
               style="filled, rounded"];
           "pitchtools.Vector" [color=4,
               group=3,
               label=Vector,
               shape=oval,
               style=bold];
           "pitchtools.Vector" -> "pitchtools.IntervalVector";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedCounter" -> "pitchtools.Vector";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.clear
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.copy
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.elements
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.from_selection
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.item_class
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.items
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.keys
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.most_common
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.subtract
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.update
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.values
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.viewitems
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.viewkeys
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.viewvalues
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.__add__
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.__and__
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.__contains__
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.__delitem__
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.__eq__
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.__format__
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.__getitem__
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.__hash__
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.__iter__
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.__len__
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.__missing__
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.__ne__
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.__or__
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.__repr__
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.__setitem__
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.__str__
      ~abjad.tools.pitchtools.IntervalVector.IntervalVector.__sub__

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

.. autoattribute:: abjad.tools.pitchtools.IntervalVector.IntervalVector.item_class
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.clear
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.copy
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.elements
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.items
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.keys
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.most_common
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.subtract
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.update
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.values
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.viewitems
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.viewkeys
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.viewvalues
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.from_selection
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.__add__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.__and__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.__contains__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.__delitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.__getitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.__iter__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.__len__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.__missing__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.__or__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.__setitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.__str__
   :noindex:

.. automethod:: abjad.tools.pitchtools.IntervalVector.IntervalVector.__sub__
   :noindex:
