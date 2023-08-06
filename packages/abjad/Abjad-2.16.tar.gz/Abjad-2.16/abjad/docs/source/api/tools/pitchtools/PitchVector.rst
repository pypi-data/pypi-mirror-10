pitchtools.PitchVector
======================

.. autoclass:: abjad.tools.pitchtools.PitchVector.PitchVector

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
           "pitchtools.PitchVector" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>PitchVector</B>>,
               shape=box,
               style="filled, rounded"];
           "pitchtools.Vector" [color=4,
               group=3,
               label=Vector,
               shape=oval,
               style=bold];
           "pitchtools.Vector" -> "pitchtools.PitchVector";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedCounter" -> "pitchtools.Vector";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.PitchVector.PitchVector.clear
      ~abjad.tools.pitchtools.PitchVector.PitchVector.copy
      ~abjad.tools.pitchtools.PitchVector.PitchVector.elements
      ~abjad.tools.pitchtools.PitchVector.PitchVector.from_selection
      ~abjad.tools.pitchtools.PitchVector.PitchVector.item_class
      ~abjad.tools.pitchtools.PitchVector.PitchVector.items
      ~abjad.tools.pitchtools.PitchVector.PitchVector.keys
      ~abjad.tools.pitchtools.PitchVector.PitchVector.most_common
      ~abjad.tools.pitchtools.PitchVector.PitchVector.subtract
      ~abjad.tools.pitchtools.PitchVector.PitchVector.update
      ~abjad.tools.pitchtools.PitchVector.PitchVector.values
      ~abjad.tools.pitchtools.PitchVector.PitchVector.viewitems
      ~abjad.tools.pitchtools.PitchVector.PitchVector.viewkeys
      ~abjad.tools.pitchtools.PitchVector.PitchVector.viewvalues
      ~abjad.tools.pitchtools.PitchVector.PitchVector.__add__
      ~abjad.tools.pitchtools.PitchVector.PitchVector.__and__
      ~abjad.tools.pitchtools.PitchVector.PitchVector.__contains__
      ~abjad.tools.pitchtools.PitchVector.PitchVector.__delitem__
      ~abjad.tools.pitchtools.PitchVector.PitchVector.__eq__
      ~abjad.tools.pitchtools.PitchVector.PitchVector.__format__
      ~abjad.tools.pitchtools.PitchVector.PitchVector.__getitem__
      ~abjad.tools.pitchtools.PitchVector.PitchVector.__hash__
      ~abjad.tools.pitchtools.PitchVector.PitchVector.__iter__
      ~abjad.tools.pitchtools.PitchVector.PitchVector.__len__
      ~abjad.tools.pitchtools.PitchVector.PitchVector.__missing__
      ~abjad.tools.pitchtools.PitchVector.PitchVector.__ne__
      ~abjad.tools.pitchtools.PitchVector.PitchVector.__or__
      ~abjad.tools.pitchtools.PitchVector.PitchVector.__repr__
      ~abjad.tools.pitchtools.PitchVector.PitchVector.__setitem__
      ~abjad.tools.pitchtools.PitchVector.PitchVector.__str__
      ~abjad.tools.pitchtools.PitchVector.PitchVector.__sub__

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

.. autoattribute:: abjad.tools.pitchtools.PitchVector.PitchVector.item_class
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.clear
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.copy
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.elements
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.items
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.keys
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.most_common
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.subtract
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.update
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.values
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.viewitems
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.viewkeys
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.viewvalues
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.from_selection
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.__add__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.__and__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.__contains__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.__delitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.__getitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.__iter__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.__len__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.__missing__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.__or__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.__setitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.__str__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchVector.PitchVector.__sub__
   :noindex:
