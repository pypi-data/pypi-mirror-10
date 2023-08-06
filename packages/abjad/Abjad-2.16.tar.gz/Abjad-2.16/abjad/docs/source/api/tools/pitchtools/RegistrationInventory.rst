pitchtools.RegistrationInventory
================================

.. autoclass:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory

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
           "pitchtools.RegistrationInventory" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>RegistrationInventory</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedList" -> "pitchtools.RegistrationInventory";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.append
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.count
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.extend
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.index
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.insert
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.item_class
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.items
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.keep_sorted
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.pop
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.remove
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.reverse
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.sort
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__contains__
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__delitem__
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__eq__
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__format__
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__getitem__
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__hash__
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__iadd__
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__iter__
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__len__
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__ne__
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__repr__
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__reversed__
      ~abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__setitem__

Bases
-----

- :py:class:`datastructuretools.TypedList <abjad.tools.datastructuretools.TypedList.TypedList>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.item_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.items
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.keep_sorted
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.append
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.count
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.extend
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.index
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.insert
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.pop
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.remove
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.reverse
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.sort
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__contains__
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__delitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__getitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__iadd__
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__iter__
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__len__
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__reversed__
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationInventory.RegistrationInventory.__setitem__
   :noindex:
