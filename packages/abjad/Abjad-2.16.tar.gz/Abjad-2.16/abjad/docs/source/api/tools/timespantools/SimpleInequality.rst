timespantools.SimpleInequality
==============================

.. autoclass:: abjad.tools.timespantools.SimpleInequality.SimpleInequality

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
       subgraph cluster_timespantools {
           graph [label=timespantools];
           "timespantools.SimpleInequality" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>SimpleInequality</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "timespantools.SimpleInequality";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.timespantools.SimpleInequality.SimpleInequality.evaluate
      ~abjad.tools.timespantools.SimpleInequality.SimpleInequality.evaluate_offset_inequality
      ~abjad.tools.timespantools.SimpleInequality.SimpleInequality.get_offset_indices
      ~abjad.tools.timespantools.SimpleInequality.SimpleInequality.template
      ~abjad.tools.timespantools.SimpleInequality.SimpleInequality.__eq__
      ~abjad.tools.timespantools.SimpleInequality.SimpleInequality.__format__
      ~abjad.tools.timespantools.SimpleInequality.SimpleInequality.__hash__
      ~abjad.tools.timespantools.SimpleInequality.SimpleInequality.__ne__
      ~abjad.tools.timespantools.SimpleInequality.SimpleInequality.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.timespantools.SimpleInequality.SimpleInequality.template
   :noindex:

Methods
-------

.. automethod:: abjad.tools.timespantools.SimpleInequality.SimpleInequality.evaluate
   :noindex:

.. automethod:: abjad.tools.timespantools.SimpleInequality.SimpleInequality.evaluate_offset_inequality
   :noindex:

.. automethod:: abjad.tools.timespantools.SimpleInequality.SimpleInequality.get_offset_indices
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.timespantools.SimpleInequality.SimpleInequality.__eq__
   :noindex:

.. automethod:: abjad.tools.timespantools.SimpleInequality.SimpleInequality.__format__
   :noindex:

.. automethod:: abjad.tools.timespantools.SimpleInequality.SimpleInequality.__hash__
   :noindex:

.. automethod:: abjad.tools.timespantools.SimpleInequality.SimpleInequality.__ne__
   :noindex:

.. automethod:: abjad.tools.timespantools.SimpleInequality.SimpleInequality.__repr__
   :noindex:
