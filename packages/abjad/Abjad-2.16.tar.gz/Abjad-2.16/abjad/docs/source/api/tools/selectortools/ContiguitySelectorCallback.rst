selectortools.ContiguitySelectorCallback
========================================

.. autoclass:: abjad.tools.selectortools.ContiguitySelectorCallback.ContiguitySelectorCallback

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
           "selectortools.ContiguitySelectorCallback" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>ContiguitySelectorCallback</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "selectortools.ContiguitySelectorCallback";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.selectortools.ContiguitySelectorCallback.ContiguitySelectorCallback.__call__
      ~abjad.tools.selectortools.ContiguitySelectorCallback.ContiguitySelectorCallback.__copy__
      ~abjad.tools.selectortools.ContiguitySelectorCallback.ContiguitySelectorCallback.__eq__
      ~abjad.tools.selectortools.ContiguitySelectorCallback.ContiguitySelectorCallback.__format__
      ~abjad.tools.selectortools.ContiguitySelectorCallback.ContiguitySelectorCallback.__hash__
      ~abjad.tools.selectortools.ContiguitySelectorCallback.ContiguitySelectorCallback.__ne__
      ~abjad.tools.selectortools.ContiguitySelectorCallback.ContiguitySelectorCallback.__repr__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.selectortools.ContiguitySelectorCallback.ContiguitySelectorCallback.__call__
   :noindex:

.. automethod:: abjad.tools.selectortools.ContiguitySelectorCallback.ContiguitySelectorCallback.__copy__
   :noindex:

.. automethod:: abjad.tools.selectortools.ContiguitySelectorCallback.ContiguitySelectorCallback.__eq__
   :noindex:

.. automethod:: abjad.tools.selectortools.ContiguitySelectorCallback.ContiguitySelectorCallback.__format__
   :noindex:

.. automethod:: abjad.tools.selectortools.ContiguitySelectorCallback.ContiguitySelectorCallback.__hash__
   :noindex:

.. automethod:: abjad.tools.selectortools.ContiguitySelectorCallback.ContiguitySelectorCallback.__ne__
   :noindex:

.. automethod:: abjad.tools.selectortools.ContiguitySelectorCallback.ContiguitySelectorCallback.__repr__
   :noindex:
