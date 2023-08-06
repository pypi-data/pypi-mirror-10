abjadbooktools.CodeBlock
========================

.. autoclass:: abjad.tools.abjadbooktools.CodeBlock.CodeBlock

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
           "abjadbooktools.CodeBlock" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>CodeBlock</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "abjadbooktools.CodeBlock";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.abjadbooktools.CodeBlock.CodeBlock.hide
      ~abjad.tools.abjadbooktools.CodeBlock.CodeBlock.lines
      ~abjad.tools.abjadbooktools.CodeBlock.CodeBlock.processed_results
      ~abjad.tools.abjadbooktools.CodeBlock.CodeBlock.read
      ~abjad.tools.abjadbooktools.CodeBlock.CodeBlock.scale
      ~abjad.tools.abjadbooktools.CodeBlock.CodeBlock.starting_line_number
      ~abjad.tools.abjadbooktools.CodeBlock.CodeBlock.stopping_line_number
      ~abjad.tools.abjadbooktools.CodeBlock.CodeBlock.strip_prompt
      ~abjad.tools.abjadbooktools.CodeBlock.CodeBlock.wrap_width
      ~abjad.tools.abjadbooktools.CodeBlock.CodeBlock.__call__
      ~abjad.tools.abjadbooktools.CodeBlock.CodeBlock.__eq__
      ~abjad.tools.abjadbooktools.CodeBlock.CodeBlock.__format__
      ~abjad.tools.abjadbooktools.CodeBlock.CodeBlock.__hash__
      ~abjad.tools.abjadbooktools.CodeBlock.CodeBlock.__ne__
      ~abjad.tools.abjadbooktools.CodeBlock.CodeBlock.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.abjadbooktools.CodeBlock.CodeBlock.hide
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.CodeBlock.CodeBlock.lines
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.CodeBlock.CodeBlock.processed_results
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.CodeBlock.CodeBlock.scale
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.CodeBlock.CodeBlock.starting_line_number
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.CodeBlock.CodeBlock.stopping_line_number
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.CodeBlock.CodeBlock.strip_prompt
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.CodeBlock.CodeBlock.wrap_width
   :noindex:

Methods
-------

.. automethod:: abjad.tools.abjadbooktools.CodeBlock.CodeBlock.read
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.abjadbooktools.CodeBlock.CodeBlock.__call__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.CodeBlock.CodeBlock.__eq__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.CodeBlock.CodeBlock.__format__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.CodeBlock.CodeBlock.__hash__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.CodeBlock.CodeBlock.__ne__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.CodeBlock.CodeBlock.__repr__
   :noindex:
