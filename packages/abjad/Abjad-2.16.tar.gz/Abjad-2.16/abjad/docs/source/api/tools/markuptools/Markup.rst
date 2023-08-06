markuptools.Markup
==================

.. autoclass:: abjad.tools.markuptools.Markup.Markup

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
       subgraph cluster_markuptools {
           graph [label=markuptools];
           "markuptools.Markup" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Markup</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "markuptools.Markup";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.markuptools.Markup.Markup.bold
      ~abjad.tools.markuptools.Markup.Markup.box
      ~abjad.tools.markuptools.Markup.Markup.caps
      ~abjad.tools.markuptools.Markup.Markup.center_align
      ~abjad.tools.markuptools.Markup.Markup.center_column
      ~abjad.tools.markuptools.Markup.Markup.circle
      ~abjad.tools.markuptools.Markup.Markup.column
      ~abjad.tools.markuptools.Markup.Markup.combine
      ~abjad.tools.markuptools.Markup.Markup.concat
      ~abjad.tools.markuptools.Markup.Markup.contents
      ~abjad.tools.markuptools.Markup.Markup.direction
      ~abjad.tools.markuptools.Markup.Markup.draw_line
      ~abjad.tools.markuptools.Markup.Markup.dynamic
      ~abjad.tools.markuptools.Markup.Markup.finger
      ~abjad.tools.markuptools.Markup.Markup.flat
      ~abjad.tools.markuptools.Markup.Markup.fontsize
      ~abjad.tools.markuptools.Markup.Markup.fraction
      ~abjad.tools.markuptools.Markup.Markup.general_align
      ~abjad.tools.markuptools.Markup.Markup.halign
      ~abjad.tools.markuptools.Markup.Markup.hcenter_in
      ~abjad.tools.markuptools.Markup.Markup.hspace
      ~abjad.tools.markuptools.Markup.Markup.huge
      ~abjad.tools.markuptools.Markup.Markup.italic
      ~abjad.tools.markuptools.Markup.Markup.larger
      ~abjad.tools.markuptools.Markup.Markup.left_column
      ~abjad.tools.markuptools.Markup.Markup.line
      ~abjad.tools.markuptools.Markup.Markup.musicglyph
      ~abjad.tools.markuptools.Markup.Markup.natural
      ~abjad.tools.markuptools.Markup.Markup.note_by_number
      ~abjad.tools.markuptools.Markup.Markup.null
      ~abjad.tools.markuptools.Markup.Markup.override
      ~abjad.tools.markuptools.Markup.Markup.pad_around
      ~abjad.tools.markuptools.Markup.Markup.pad_to_box
      ~abjad.tools.markuptools.Markup.Markup.parenthesize
      ~abjad.tools.markuptools.Markup.Markup.postscript
      ~abjad.tools.markuptools.Markup.Markup.raise_
      ~abjad.tools.markuptools.Markup.Markup.right_column
      ~abjad.tools.markuptools.Markup.Markup.rotate
      ~abjad.tools.markuptools.Markup.Markup.sans
      ~abjad.tools.markuptools.Markup.Markup.scale
      ~abjad.tools.markuptools.Markup.Markup.sharp
      ~abjad.tools.markuptools.Markup.Markup.smaller
      ~abjad.tools.markuptools.Markup.Markup.stack_priority
      ~abjad.tools.markuptools.Markup.Markup.tiny
      ~abjad.tools.markuptools.Markup.Markup.translate
      ~abjad.tools.markuptools.Markup.Markup.triangle
      ~abjad.tools.markuptools.Markup.Markup.upright
      ~abjad.tools.markuptools.Markup.Markup.vcenter
      ~abjad.tools.markuptools.Markup.Markup.vspace
      ~abjad.tools.markuptools.Markup.Markup.whiteout
      ~abjad.tools.markuptools.Markup.Markup.with_color
      ~abjad.tools.markuptools.Markup.Markup.with_dimensions
      ~abjad.tools.markuptools.Markup.Markup.__add__
      ~abjad.tools.markuptools.Markup.Markup.__copy__
      ~abjad.tools.markuptools.Markup.Markup.__eq__
      ~abjad.tools.markuptools.Markup.Markup.__format__
      ~abjad.tools.markuptools.Markup.Markup.__hash__
      ~abjad.tools.markuptools.Markup.Markup.__illustrate__
      ~abjad.tools.markuptools.Markup.Markup.__ne__
      ~abjad.tools.markuptools.Markup.Markup.__repr__
      ~abjad.tools.markuptools.Markup.Markup.__str__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.markuptools.Markup.Markup.contents
   :noindex:

.. autoattribute:: abjad.tools.markuptools.Markup.Markup.direction
   :noindex:

.. autoattribute:: abjad.tools.markuptools.Markup.Markup.stack_priority
   :noindex:

Methods
-------

.. automethod:: abjad.tools.markuptools.Markup.Markup.bold
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.box
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.caps
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.center_align
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.circle
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.dynamic
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.finger
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.fontsize
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.general_align
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.halign
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.hcenter_in
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.huge
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.italic
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.larger
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.line
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.override
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.pad_around
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.pad_to_box
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.parenthesize
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.raise_
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.rotate
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.sans
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.scale
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.smaller
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.tiny
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.translate
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.upright
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.vcenter
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.whiteout
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.with_color
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.with_dimensions
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.markuptools.Markup.Markup.center_column
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.column
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.combine
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.concat
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.draw_line
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.flat
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.fraction
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.hspace
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.left_column
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.musicglyph
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.natural
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.note_by_number
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.null
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.postscript
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.right_column
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.sharp
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.triangle
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.vspace
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.markuptools.Markup.Markup.__add__
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.__copy__
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.__eq__
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.__format__
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.__hash__
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.__illustrate__
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.__ne__
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.__repr__
   :noindex:

.. automethod:: abjad.tools.markuptools.Markup.Markup.__str__
   :noindex:
