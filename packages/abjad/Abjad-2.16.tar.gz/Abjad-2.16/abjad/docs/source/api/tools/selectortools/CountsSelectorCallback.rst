selectortools.CountsSelectorCallback
====================================

.. autoclass:: abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback

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
           "selectortools.CountsSelectorCallback" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>CountsSelectorCallback</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "selectortools.CountsSelectorCallback";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.counts
      ~abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.cyclic
      ~abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.fuse_overhang
      ~abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.nonempty
      ~abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.overhang
      ~abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.rotate
      ~abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.__call__
      ~abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.__copy__
      ~abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.__eq__
      ~abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.__format__
      ~abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.__hash__
      ~abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.__ne__
      ~abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.__repr__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.counts
   :noindex:

.. autoattribute:: abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.cyclic
   :noindex:

.. autoattribute:: abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.fuse_overhang
   :noindex:

.. autoattribute:: abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.nonempty
   :noindex:

.. autoattribute:: abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.overhang
   :noindex:

.. autoattribute:: abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.rotate
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.__call__
   :noindex:

.. automethod:: abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.__copy__
   :noindex:

.. automethod:: abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.__eq__
   :noindex:

.. automethod:: abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.__format__
   :noindex:

.. automethod:: abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.__hash__
   :noindex:

.. automethod:: abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.__ne__
   :noindex:

.. automethod:: abjad.tools.selectortools.CountsSelectorCallback.CountsSelectorCallback.__repr__
   :noindex:
