datastructuretools.TypedList
============================

.. autoclass:: abjad.tools.datastructuretools.TypedList.TypedList

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
           "datastructuretools.TypedList" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>TypedList</B>>,
               shape=box,
               style="filled, rounded"];
           "datastructuretools.TypedCollection" -> "datastructuretools.TypedList";
       }
       subgraph cluster_indicatortools {
           graph [label=indicatortools];
           "indicatortools.ClefInventory" [color=5,
               group=4,
               label=ClefInventory,
               shape=box];
           "indicatortools.TempoInventory" [color=5,
               group=4,
               label=TempoInventory,
               shape=box];
           "indicatortools.TimeSignatureInventory" [color=5,
               group=4,
               label=TimeSignatureInventory,
               shape=box];
       }
       subgraph cluster_instrumenttools {
           graph [label=instrumenttools];
           "instrumenttools.InstrumentInventory" [color=6,
               group=5,
               label=InstrumentInventory,
               shape=box];
           "instrumenttools.PerformerInventory" [color=6,
               group=5,
               label=PerformerInventory,
               shape=box];
       }
       subgraph cluster_markuptools {
           graph [label=markuptools];
           "markuptools.MarkupInventory" [color=7,
               group=6,
               label=MarkupInventory,
               shape=box];
       }
       subgraph cluster_metertools {
           graph [label=metertools];
           "metertools.MeterInventory" [color=8,
               group=7,
               label=MeterInventory,
               shape=box];
       }
       subgraph cluster_pitchtools {
           graph [label=pitchtools];
           "pitchtools.PitchArrayInventory" [color=9,
               group=8,
               label=PitchArrayInventory,
               shape=box];
           "pitchtools.PitchRangeInventory" [color=9,
               group=8,
               label=PitchRangeInventory,
               shape=box];
           "pitchtools.Registration" [color=9,
               group=8,
               label=Registration,
               shape=box];
           "pitchtools.RegistrationInventory" [color=9,
               group=8,
               label=RegistrationInventory,
               shape=box];
       }
       subgraph cluster_scoretools {
           graph [label=scoretools];
           "scoretools.NoteHeadInventory" [color=1,
               group=9,
               label=NoteHeadInventory,
               shape=box];
       }
       subgraph cluster_selectiontools {
           graph [label=selectiontools];
           "selectiontools.SelectionInventory" [color=2,
               group=10,
               label=SelectionInventory,
               shape=box];
       }
       subgraph cluster_timespantools {
           graph [label=timespantools];
           "timespantools.CompoundInequality" [color=3,
               group=11,
               label=CompoundInequality,
               shape=box];
           "timespantools.TimespanInventory" [color=3,
               group=11,
               label=TimespanInventory,
               shape=box];
       }
       subgraph cluster_ide {
           graph [label=ide];
           "ide.idetools.View" [color=4,
               group=3,
               label=View,
               shape=box];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedList" -> "indicatortools.ClefInventory";
       "datastructuretools.TypedList" -> "indicatortools.TempoInventory";
       "datastructuretools.TypedList" -> "indicatortools.TimeSignatureInventory";
       "datastructuretools.TypedList" -> "instrumenttools.InstrumentInventory";
       "datastructuretools.TypedList" -> "instrumenttools.PerformerInventory";
       "datastructuretools.TypedList" -> "markuptools.MarkupInventory";
       "datastructuretools.TypedList" -> "metertools.MeterInventory";
       "datastructuretools.TypedList" -> "pitchtools.PitchArrayInventory";
       "datastructuretools.TypedList" -> "pitchtools.PitchRangeInventory";
       "datastructuretools.TypedList" -> "pitchtools.Registration";
       "datastructuretools.TypedList" -> "pitchtools.RegistrationInventory";
       "datastructuretools.TypedList" -> "scoretools.NoteHeadInventory";
       "datastructuretools.TypedList" -> "selectiontools.SelectionInventory";
       "datastructuretools.TypedList" -> "timespantools.CompoundInequality";
       "datastructuretools.TypedList" -> "timespantools.TimespanInventory";
       "datastructuretools.TypedList" -> "ide.idetools.View";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.datastructuretools.TypedList.TypedList.append
      ~abjad.tools.datastructuretools.TypedList.TypedList.count
      ~abjad.tools.datastructuretools.TypedList.TypedList.extend
      ~abjad.tools.datastructuretools.TypedList.TypedList.index
      ~abjad.tools.datastructuretools.TypedList.TypedList.insert
      ~abjad.tools.datastructuretools.TypedList.TypedList.item_class
      ~abjad.tools.datastructuretools.TypedList.TypedList.items
      ~abjad.tools.datastructuretools.TypedList.TypedList.keep_sorted
      ~abjad.tools.datastructuretools.TypedList.TypedList.pop
      ~abjad.tools.datastructuretools.TypedList.TypedList.remove
      ~abjad.tools.datastructuretools.TypedList.TypedList.reverse
      ~abjad.tools.datastructuretools.TypedList.TypedList.sort
      ~abjad.tools.datastructuretools.TypedList.TypedList.__contains__
      ~abjad.tools.datastructuretools.TypedList.TypedList.__delitem__
      ~abjad.tools.datastructuretools.TypedList.TypedList.__eq__
      ~abjad.tools.datastructuretools.TypedList.TypedList.__format__
      ~abjad.tools.datastructuretools.TypedList.TypedList.__getitem__
      ~abjad.tools.datastructuretools.TypedList.TypedList.__hash__
      ~abjad.tools.datastructuretools.TypedList.TypedList.__iadd__
      ~abjad.tools.datastructuretools.TypedList.TypedList.__iter__
      ~abjad.tools.datastructuretools.TypedList.TypedList.__len__
      ~abjad.tools.datastructuretools.TypedList.TypedList.__ne__
      ~abjad.tools.datastructuretools.TypedList.TypedList.__repr__
      ~abjad.tools.datastructuretools.TypedList.TypedList.__reversed__
      ~abjad.tools.datastructuretools.TypedList.TypedList.__setitem__

Bases
-----

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.datastructuretools.TypedList.TypedList.item_class
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.TypedList.TypedList.items
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.datastructuretools.TypedList.TypedList.keep_sorted
   :noindex:

Methods
-------

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.append
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.count
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.extend
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.index
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.insert
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.pop
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.remove
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.reverse
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.sort
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.__contains__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.__delitem__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.__eq__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.__format__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.__getitem__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.__hash__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.__iadd__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.__iter__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.__len__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.__ne__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.__repr__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.__reversed__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.TypedList.TypedList.__setitem__
   :noindex:
