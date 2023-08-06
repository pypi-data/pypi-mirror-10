rhythmmakertools.BooleanPatternInventory
========================================

.. autoclass:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory

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
           "datastructuretools.TypedTuple" [color=3,
               group=2,
               label=TypedTuple,
               shape=box];
           "datastructuretools.TypedCollection" -> "datastructuretools.TypedTuple";
       }
       subgraph cluster_rhythmmakertools {
           graph [label=rhythmmakertools];
           "rhythmmakertools.BooleanPatternInventory" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>BooleanPatternInventory</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedTuple" -> "rhythmmakertools.BooleanPatternInventory";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.count
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.get_matching_pattern
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.get_matching_payload
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.index
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.item_class
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.items
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__add__
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__contains__
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__eq__
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__format__
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__getitem__
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__getslice__
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__hash__
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__iter__
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__len__
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__mul__
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__ne__
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__radd__
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__repr__
      ~abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__rmul__

Bases
-----

- :py:class:`datastructuretools.TypedTuple <abjad.tools.datastructuretools.TypedTuple.TypedTuple>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.item_class
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.items
   :noindex:

Methods
-------

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.count
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.get_matching_pattern
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.get_matching_payload
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.index
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__add__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__contains__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__getitem__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__getslice__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__iter__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__len__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__mul__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__radd__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__repr__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.BooleanPatternInventory.BooleanPatternInventory.__rmul__
   :noindex:
