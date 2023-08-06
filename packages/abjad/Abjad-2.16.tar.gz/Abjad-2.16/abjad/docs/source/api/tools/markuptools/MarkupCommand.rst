markuptools.MarkupCommand
=========================

.. autoclass:: abjad.tools.markuptools.MarkupCommand.MarkupCommand

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
           "markuptools.MarkupCommand" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>MarkupCommand</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "markuptools.MarkupCommand";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.markuptools.MarkupCommand.MarkupCommand.args
      ~abjad.tools.markuptools.MarkupCommand.MarkupCommand.command
      ~abjad.tools.markuptools.MarkupCommand.MarkupCommand.force_quotes
      ~abjad.tools.markuptools.MarkupCommand.MarkupCommand.__copy__
      ~abjad.tools.markuptools.MarkupCommand.MarkupCommand.__eq__
      ~abjad.tools.markuptools.MarkupCommand.MarkupCommand.__format__
      ~abjad.tools.markuptools.MarkupCommand.MarkupCommand.__hash__
      ~abjad.tools.markuptools.MarkupCommand.MarkupCommand.__ne__
      ~abjad.tools.markuptools.MarkupCommand.MarkupCommand.__repr__
      ~abjad.tools.markuptools.MarkupCommand.MarkupCommand.__str__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.markuptools.MarkupCommand.MarkupCommand.args
   :noindex:

.. autoattribute:: abjad.tools.markuptools.MarkupCommand.MarkupCommand.command
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.markuptools.MarkupCommand.MarkupCommand.force_quotes
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.markuptools.MarkupCommand.MarkupCommand.__copy__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupCommand.MarkupCommand.__eq__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupCommand.MarkupCommand.__format__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupCommand.MarkupCommand.__hash__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupCommand.MarkupCommand.__ne__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupCommand.MarkupCommand.__repr__
   :noindex:

.. automethod:: abjad.tools.markuptools.MarkupCommand.MarkupCommand.__str__
   :noindex:
