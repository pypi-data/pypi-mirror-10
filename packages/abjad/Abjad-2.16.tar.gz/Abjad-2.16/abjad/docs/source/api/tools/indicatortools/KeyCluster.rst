indicatortools.KeyCluster
=========================

.. autoclass:: abjad.tools.indicatortools.KeyCluster.KeyCluster

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
       subgraph cluster_indicatortools {
           graph [label=indicatortools];
           "indicatortools.KeyCluster" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>KeyCluster</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "indicatortools.KeyCluster";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.indicatortools.KeyCluster.KeyCluster.include_black_keys
      ~abjad.tools.indicatortools.KeyCluster.KeyCluster.include_white_keys
      ~abjad.tools.indicatortools.KeyCluster.KeyCluster.markup_direction
      ~abjad.tools.indicatortools.KeyCluster.KeyCluster.suppress_markup
      ~abjad.tools.indicatortools.KeyCluster.KeyCluster.__copy__
      ~abjad.tools.indicatortools.KeyCluster.KeyCluster.__eq__
      ~abjad.tools.indicatortools.KeyCluster.KeyCluster.__format__
      ~abjad.tools.indicatortools.KeyCluster.KeyCluster.__hash__
      ~abjad.tools.indicatortools.KeyCluster.KeyCluster.__ne__
      ~abjad.tools.indicatortools.KeyCluster.KeyCluster.__repr__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.indicatortools.KeyCluster.KeyCluster.include_black_keys
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.KeyCluster.KeyCluster.include_white_keys
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.KeyCluster.KeyCluster.markup_direction
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.KeyCluster.KeyCluster.suppress_markup
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.indicatortools.KeyCluster.KeyCluster.__copy__
   :noindex:

.. automethod:: abjad.tools.indicatortools.KeyCluster.KeyCluster.__eq__
   :noindex:

.. automethod:: abjad.tools.indicatortools.KeyCluster.KeyCluster.__format__
   :noindex:

.. automethod:: abjad.tools.indicatortools.KeyCluster.KeyCluster.__hash__
   :noindex:

.. automethod:: abjad.tools.indicatortools.KeyCluster.KeyCluster.__ne__
   :noindex:

.. automethod:: abjad.tools.indicatortools.KeyCluster.KeyCluster.__repr__
   :noindex:
