selectortools.Selector
======================

.. autoclass:: abjad.tools.selectortools.Selector.Selector

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
           "abctools.AbjadValueObject" [color=2,
               group=1,
               label=AbjadValueObject,
               shape=box];
           "abctools.AbjadObject" -> "abctools.AbjadValueObject";
           "abctools.AbjadObject.AbstractBase" -> "abctools.AbjadObject";
       }
       subgraph cluster_selectortools {
           graph [label=selectortools];
           "selectortools.Selector" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Selector</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "selectortools.Selector";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.selectortools.Selector.Selector.append_callback
      ~abjad.tools.selectortools.Selector.Selector.by_class
      ~abjad.tools.selectortools.Selector.Selector.by_contiguity
      ~abjad.tools.selectortools.Selector.Selector.by_counts
      ~abjad.tools.selectortools.Selector.Selector.by_duration
      ~abjad.tools.selectortools.Selector.Selector.by_leaves
      ~abjad.tools.selectortools.Selector.Selector.by_length
      ~abjad.tools.selectortools.Selector.Selector.by_logical_measure
      ~abjad.tools.selectortools.Selector.Selector.by_logical_tie
      ~abjad.tools.selectortools.Selector.Selector.by_pattern
      ~abjad.tools.selectortools.Selector.Selector.by_pitch
      ~abjad.tools.selectortools.Selector.Selector.by_run
      ~abjad.tools.selectortools.Selector.Selector.callbacks
      ~abjad.tools.selectortools.Selector.Selector.first
      ~abjad.tools.selectortools.Selector.Selector.flatten
      ~abjad.tools.selectortools.Selector.Selector.get_item
      ~abjad.tools.selectortools.Selector.Selector.get_slice
      ~abjad.tools.selectortools.Selector.Selector.last
      ~abjad.tools.selectortools.Selector.Selector.middle
      ~abjad.tools.selectortools.Selector.Selector.most
      ~abjad.tools.selectortools.Selector.Selector.rest
      ~abjad.tools.selectortools.Selector.Selector.run_selectors
      ~abjad.tools.selectortools.Selector.Selector.with_next_leaf
      ~abjad.tools.selectortools.Selector.Selector.with_previous_leaf
      ~abjad.tools.selectortools.Selector.Selector.__call__
      ~abjad.tools.selectortools.Selector.Selector.__copy__
      ~abjad.tools.selectortools.Selector.Selector.__eq__
      ~abjad.tools.selectortools.Selector.Selector.__format__
      ~abjad.tools.selectortools.Selector.Selector.__getitem__
      ~abjad.tools.selectortools.Selector.Selector.__hash__
      ~abjad.tools.selectortools.Selector.Selector.__ne__
      ~abjad.tools.selectortools.Selector.Selector.__repr__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.selectortools.Selector.Selector.callbacks
   :noindex:

Methods
-------

.. automethod:: abjad.tools.selectortools.Selector.Selector.append_callback
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.by_class
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.by_contiguity
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.by_counts
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.by_duration
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.by_leaves
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.by_length
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.by_logical_measure
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.by_logical_tie
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.by_pattern
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.by_pitch
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.by_run
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.first
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.flatten
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.get_item
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.get_slice
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.last
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.middle
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.most
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.rest
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.with_next_leaf
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.with_previous_leaf
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.selectortools.Selector.Selector.run_selectors
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.selectortools.Selector.Selector.__call__
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.__copy__
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.__eq__
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.__format__
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.__getitem__
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.__hash__
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.__ne__
   :noindex:

.. automethod:: abjad.tools.selectortools.Selector.Selector.__repr__
   :noindex:
