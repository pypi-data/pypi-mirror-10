quantizationtools.TerminalQEvent
================================

.. autoclass:: abjad.tools.quantizationtools.TerminalQEvent.TerminalQEvent

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
           "quantizationtools.QEvent" [color=3,
               group=2,
               label=QEvent,
               shape=oval,
               style=bold];
           "quantizationtools.TerminalQEvent" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>TerminalQEvent</B>>,
               shape=box,
               style="filled, rounded"];
           "quantizationtools.QEvent" -> "quantizationtools.TerminalQEvent";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.QEvent";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.TerminalQEvent.TerminalQEvent.index
      ~abjad.tools.quantizationtools.TerminalQEvent.TerminalQEvent.offset
      ~abjad.tools.quantizationtools.TerminalQEvent.TerminalQEvent.__eq__
      ~abjad.tools.quantizationtools.TerminalQEvent.TerminalQEvent.__format__
      ~abjad.tools.quantizationtools.TerminalQEvent.TerminalQEvent.__hash__
      ~abjad.tools.quantizationtools.TerminalQEvent.TerminalQEvent.__lt__
      ~abjad.tools.quantizationtools.TerminalQEvent.TerminalQEvent.__ne__
      ~abjad.tools.quantizationtools.TerminalQEvent.TerminalQEvent.__repr__

Bases
-----

- :py:class:`quantizationtools.QEvent <abjad.tools.quantizationtools.QEvent.QEvent>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.TerminalQEvent.TerminalQEvent.index
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.TerminalQEvent.TerminalQEvent.offset
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.TerminalQEvent.TerminalQEvent.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.TerminalQEvent.TerminalQEvent.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.TerminalQEvent.TerminalQEvent.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.TerminalQEvent.TerminalQEvent.__lt__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.TerminalQEvent.TerminalQEvent.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.TerminalQEvent.TerminalQEvent.__repr__
   :noindex:
