quantizationtools.QEventProxy
=============================

.. autoclass:: abjad.tools.quantizationtools.QEventProxy.QEventProxy

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
           "quantizationtools.QEventProxy" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>QEventProxy</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.QEventProxy";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.QEventProxy.QEventProxy.index
      ~abjad.tools.quantizationtools.QEventProxy.QEventProxy.offset
      ~abjad.tools.quantizationtools.QEventProxy.QEventProxy.q_event
      ~abjad.tools.quantizationtools.QEventProxy.QEventProxy.__eq__
      ~abjad.tools.quantizationtools.QEventProxy.QEventProxy.__format__
      ~abjad.tools.quantizationtools.QEventProxy.QEventProxy.__hash__
      ~abjad.tools.quantizationtools.QEventProxy.QEventProxy.__ne__
      ~abjad.tools.quantizationtools.QEventProxy.QEventProxy.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.QEventProxy.QEventProxy.index
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QEventProxy.QEventProxy.offset
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QEventProxy.QEventProxy.q_event
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.QEventProxy.QEventProxy.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEventProxy.QEventProxy.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEventProxy.QEventProxy.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEventProxy.QEventProxy.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEventProxy.QEventProxy.__repr__
   :noindex:
