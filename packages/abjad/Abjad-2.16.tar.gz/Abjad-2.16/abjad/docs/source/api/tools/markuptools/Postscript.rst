markuptools.Postscript
======================

.. autoclass:: abjad.tools.markuptools.Postscript.Postscript

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
           "markuptools.Postscript" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Postscript</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "markuptools.Postscript";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.markuptools.Postscript.Postscript.as_markup
      ~abjad.tools.markuptools.Postscript.Postscript.charpath
      ~abjad.tools.markuptools.Postscript.Postscript.closepath
      ~abjad.tools.markuptools.Postscript.Postscript.curveto
      ~abjad.tools.markuptools.Postscript.Postscript.fill
      ~abjad.tools.markuptools.Postscript.Postscript.findfont
      ~abjad.tools.markuptools.Postscript.Postscript.grestore
      ~abjad.tools.markuptools.Postscript.Postscript.gsave
      ~abjad.tools.markuptools.Postscript.Postscript.lineto
      ~abjad.tools.markuptools.Postscript.Postscript.moveto
      ~abjad.tools.markuptools.Postscript.Postscript.newpath
      ~abjad.tools.markuptools.Postscript.Postscript.operators
      ~abjad.tools.markuptools.Postscript.Postscript.rcurveto
      ~abjad.tools.markuptools.Postscript.Postscript.rlineto
      ~abjad.tools.markuptools.Postscript.Postscript.rmoveto
      ~abjad.tools.markuptools.Postscript.Postscript.rotate
      ~abjad.tools.markuptools.Postscript.Postscript.scale
      ~abjad.tools.markuptools.Postscript.Postscript.scalefont
      ~abjad.tools.markuptools.Postscript.Postscript.setdash
      ~abjad.tools.markuptools.Postscript.Postscript.setfont
      ~abjad.tools.markuptools.Postscript.Postscript.setgray
      ~abjad.tools.markuptools.Postscript.Postscript.setlinewidth
      ~abjad.tools.markuptools.Postscript.Postscript.setrgbcolor
      ~abjad.tools.markuptools.Postscript.Postscript.show
      ~abjad.tools.markuptools.Postscript.Postscript.stroke
      ~abjad.tools.markuptools.Postscript.Postscript.translate
      ~abjad.tools.markuptools.Postscript.Postscript.__add__
      ~abjad.tools.markuptools.Postscript.Postscript.__copy__
      ~abjad.tools.markuptools.Postscript.Postscript.__eq__
      ~abjad.tools.markuptools.Postscript.Postscript.__format__
      ~abjad.tools.markuptools.Postscript.Postscript.__hash__
      ~abjad.tools.markuptools.Postscript.Postscript.__illustrate__
      ~abjad.tools.markuptools.Postscript.Postscript.__ne__
      ~abjad.tools.markuptools.Postscript.Postscript.__repr__
      ~abjad.tools.markuptools.Postscript.Postscript.__str__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.markuptools.Postscript.Postscript.operators
   :noindex:

Methods
-------

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.as_markup
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.charpath
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.closepath
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.curveto
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.fill
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.findfont
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.grestore
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.gsave
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.lineto
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.moveto
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.newpath
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.rcurveto
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.rlineto
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.rmoveto
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.rotate
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.scale
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.scalefont
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.setdash
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.setfont
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.setgray
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.setlinewidth
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.setrgbcolor
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.show
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.stroke
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.translate
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.__add__
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.__copy__
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.__eq__
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.__format__
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.__hash__
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.__illustrate__
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.__ne__
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.__repr__
   :noindex:

.. automethod:: abjad.tools.markuptools.Postscript.Postscript.__str__
   :noindex:
