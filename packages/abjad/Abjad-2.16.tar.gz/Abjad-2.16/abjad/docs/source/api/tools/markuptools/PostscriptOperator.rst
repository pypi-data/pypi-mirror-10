markuptools.PostscriptOperator
==============================

.. autoclass:: abjad.tools.markuptools.PostscriptOperator.PostscriptOperator

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
           "markuptools.PostscriptOperator" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>PostscriptOperator</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "markuptools.PostscriptOperator";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.arguments
      ~abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.name
      ~abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.__copy__
      ~abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.__eq__
      ~abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.__format__
      ~abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.__hash__
      ~abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.__ne__
      ~abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.__repr__
      ~abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.__str__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.arguments
   :noindex:

.. autoattribute:: abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.name
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.__copy__
   :noindex:

.. automethod:: abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.__eq__
   :noindex:

.. automethod:: abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.__format__
   :noindex:

.. automethod:: abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.__hash__
   :noindex:

.. automethod:: abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.__ne__
   :noindex:

.. automethod:: abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.__repr__
   :noindex:

.. automethod:: abjad.tools.markuptools.PostscriptOperator.PostscriptOperator.__str__
   :noindex:
