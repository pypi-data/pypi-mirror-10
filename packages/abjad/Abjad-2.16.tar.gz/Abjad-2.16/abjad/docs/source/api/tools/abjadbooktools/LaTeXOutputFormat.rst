abjadbooktools.LaTeXOutputFormat
================================

.. autoclass:: abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat

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
       subgraph cluster_abjadbooktools {
           graph [label=abjadbooktools];
           "abjadbooktools.LaTeXOutputFormat" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>LaTeXOutputFormat</B>>,
               shape=box,
               style="filled, rounded"];
           "abjadbooktools.OutputFormat" [color=3,
               group=2,
               label=OutputFormat,
               shape=oval,
               style=bold];
           "abjadbooktools.OutputFormat" -> "abjadbooktools.LaTeXOutputFormat";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "abjadbooktools.OutputFormat";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.code_block_closing
      ~abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.code_block_opening
      ~abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.code_indent
      ~abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.image_block
      ~abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.image_format
      ~abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.__call__
      ~abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.__eq__
      ~abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.__format__
      ~abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.__hash__
      ~abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.__ne__
      ~abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.__repr__

Bases
-----

- :py:class:`abjadbooktools.OutputFormat <abjad.tools.abjadbooktools.OutputFormat.OutputFormat>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.code_block_closing
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.code_block_opening
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.code_indent
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.image_block
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.image_format
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.__call__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.__eq__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.__format__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.__hash__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.__ne__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.LaTeXOutputFormat.LaTeXOutputFormat.__repr__
   :noindex:
