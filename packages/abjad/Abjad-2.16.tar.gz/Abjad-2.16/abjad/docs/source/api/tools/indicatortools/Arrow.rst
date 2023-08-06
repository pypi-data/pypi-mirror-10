indicatortools.Arrow
====================

.. autoclass:: abjad.tools.indicatortools.Arrow.Arrow

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
           "indicatortools.Arrow" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Arrow</B>>,
               shape=box,
               style="filled, rounded"];
           "indicatortools.LineSegment" [color=3,
               group=2,
               label=LineSegment,
               shape=box];
           "indicatortools.LineSegment" -> "indicatortools.Arrow";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "indicatortools.LineSegment";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.indicatortools.Arrow.Arrow.arrow_width
      ~abjad.tools.indicatortools.Arrow.Arrow.dash_fraction
      ~abjad.tools.indicatortools.Arrow.Arrow.dash_period
      ~abjad.tools.indicatortools.Arrow.Arrow.left_broken_padding
      ~abjad.tools.indicatortools.Arrow.Arrow.left_broken_text
      ~abjad.tools.indicatortools.Arrow.Arrow.left_hspace
      ~abjad.tools.indicatortools.Arrow.Arrow.left_padding
      ~abjad.tools.indicatortools.Arrow.Arrow.left_stencil_align_direction_y
      ~abjad.tools.indicatortools.Arrow.Arrow.right_arrow
      ~abjad.tools.indicatortools.Arrow.Arrow.right_broken_arrow
      ~abjad.tools.indicatortools.Arrow.Arrow.right_broken_padding
      ~abjad.tools.indicatortools.Arrow.Arrow.right_padding
      ~abjad.tools.indicatortools.Arrow.Arrow.right_stencil_align_direction_y
      ~abjad.tools.indicatortools.Arrow.Arrow.style
      ~abjad.tools.indicatortools.Arrow.Arrow.__copy__
      ~abjad.tools.indicatortools.Arrow.Arrow.__eq__
      ~abjad.tools.indicatortools.Arrow.Arrow.__format__
      ~abjad.tools.indicatortools.Arrow.Arrow.__hash__
      ~abjad.tools.indicatortools.Arrow.Arrow.__ne__
      ~abjad.tools.indicatortools.Arrow.Arrow.__repr__

Bases
-----

- :py:class:`indicatortools.LineSegment <abjad.tools.indicatortools.LineSegment.LineSegment>`

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.indicatortools.Arrow.Arrow.arrow_width
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Arrow.Arrow.dash_fraction
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Arrow.Arrow.dash_period
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Arrow.Arrow.left_broken_padding
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Arrow.Arrow.left_broken_text
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Arrow.Arrow.left_hspace
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Arrow.Arrow.left_padding
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Arrow.Arrow.left_stencil_align_direction_y
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Arrow.Arrow.right_arrow
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Arrow.Arrow.right_broken_arrow
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Arrow.Arrow.right_broken_padding
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Arrow.Arrow.right_padding
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Arrow.Arrow.right_stencil_align_direction_y
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.Arrow.Arrow.style
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.indicatortools.Arrow.Arrow.__copy__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Arrow.Arrow.__eq__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Arrow.Arrow.__format__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Arrow.Arrow.__hash__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Arrow.Arrow.__ne__
   :noindex:

.. automethod:: abjad.tools.indicatortools.Arrow.Arrow.__repr__
   :noindex:
