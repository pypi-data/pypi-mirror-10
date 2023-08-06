quantizationtools.QEvent
========================

.. autoclass:: abjad.tools.quantizationtools.QEvent.QEvent

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
       subgraph cluster_quantizationtools {
           graph [label=quantizationtools];
           "quantizationtools.PitchedQEvent" [color=3,
               group=2,
               label=PitchedQEvent,
               shape=box];
           "quantizationtools.QEvent" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>QEvent</B>>,
               shape=oval,
               style="filled, rounded"];
           "quantizationtools.SilentQEvent" [color=3,
               group=2,
               label=SilentQEvent,
               shape=box];
           "quantizationtools.TerminalQEvent" [color=3,
               group=2,
               label=TerminalQEvent,
               shape=box];
           "quantizationtools.QEvent" -> "quantizationtools.PitchedQEvent";
           "quantizationtools.QEvent" -> "quantizationtools.SilentQEvent";
           "quantizationtools.QEvent" -> "quantizationtools.TerminalQEvent";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.QEvent";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.QEvent.QEvent.index
      ~abjad.tools.quantizationtools.QEvent.QEvent.offset
      ~abjad.tools.quantizationtools.QEvent.QEvent.__eq__
      ~abjad.tools.quantizationtools.QEvent.QEvent.__format__
      ~abjad.tools.quantizationtools.QEvent.QEvent.__hash__
      ~abjad.tools.quantizationtools.QEvent.QEvent.__lt__
      ~abjad.tools.quantizationtools.QEvent.QEvent.__ne__
      ~abjad.tools.quantizationtools.QEvent.QEvent.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.QEvent.QEvent.index
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QEvent.QEvent.offset
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.QEvent.QEvent.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEvent.QEvent.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEvent.QEvent.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEvent.QEvent.__lt__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEvent.QEvent.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEvent.QEvent.__repr__
   :noindex:
