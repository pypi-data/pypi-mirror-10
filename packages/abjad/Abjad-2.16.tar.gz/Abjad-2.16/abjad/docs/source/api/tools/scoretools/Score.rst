scoretools.Score
================

.. autoclass:: abjad.tools.scoretools.Score.Score

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
       subgraph cluster_scoretools {
           graph [label=scoretools];
           "scoretools.Component" [color=3,
               group=2,
               label=Component,
               shape=oval,
               style=bold];
           "scoretools.Container" [color=3,
               group=2,
               label=Container,
               shape=box];
           "scoretools.Context" [color=3,
               group=2,
               label=Context,
               shape=box];
           "scoretools.Score" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Score</B>>,
               shape=box,
               style="filled, rounded"];
           "scoretools.Component" -> "scoretools.Container";
           "scoretools.Container" -> "scoretools.Context";
           "scoretools.Context" -> "scoretools.Score";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "scoretools.Component";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.scoretools.Score.Score.add_final_bar_line
      ~abjad.tools.scoretools.Score.Score.add_final_markup
      ~abjad.tools.scoretools.Score.Score.append
      ~abjad.tools.scoretools.Score.Score.consists_commands
      ~abjad.tools.scoretools.Score.Score.context_name
      ~abjad.tools.scoretools.Score.Score.extend
      ~abjad.tools.scoretools.Score.Score.index
      ~abjad.tools.scoretools.Score.Score.insert
      ~abjad.tools.scoretools.Score.Score.is_nonsemantic
      ~abjad.tools.scoretools.Score.Score.is_semantic
      ~abjad.tools.scoretools.Score.Score.is_simultaneous
      ~abjad.tools.scoretools.Score.Score.name
      ~abjad.tools.scoretools.Score.Score.pop
      ~abjad.tools.scoretools.Score.Score.remove
      ~abjad.tools.scoretools.Score.Score.remove_commands
      ~abjad.tools.scoretools.Score.Score.reverse
      ~abjad.tools.scoretools.Score.Score.select_leaves
      ~abjad.tools.scoretools.Score.Score.__contains__
      ~abjad.tools.scoretools.Score.Score.__copy__
      ~abjad.tools.scoretools.Score.Score.__delitem__
      ~abjad.tools.scoretools.Score.Score.__eq__
      ~abjad.tools.scoretools.Score.Score.__format__
      ~abjad.tools.scoretools.Score.Score.__getitem__
      ~abjad.tools.scoretools.Score.Score.__graph__
      ~abjad.tools.scoretools.Score.Score.__hash__
      ~abjad.tools.scoretools.Score.Score.__illustrate__
      ~abjad.tools.scoretools.Score.Score.__len__
      ~abjad.tools.scoretools.Score.Score.__mul__
      ~abjad.tools.scoretools.Score.Score.__ne__
      ~abjad.tools.scoretools.Score.Score.__repr__
      ~abjad.tools.scoretools.Score.Score.__rmul__
      ~abjad.tools.scoretools.Score.Score.__setitem__

Bases
-----

- :py:class:`scoretools.Context <abjad.tools.scoretools.Context.Context>`

- :py:class:`scoretools.Container <abjad.tools.scoretools.Container.Container>`

- :py:class:`scoretools.Component <abjad.tools.scoretools.Component.Component>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.scoretools.Score.Score.consists_commands
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Score.Score.is_semantic
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Score.Score.remove_commands
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.scoretools.Score.Score.context_name
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Score.Score.is_nonsemantic
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Score.Score.is_simultaneous
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Score.Score.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.scoretools.Score.Score.add_final_bar_line
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.add_final_markup
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.append
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.extend
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.index
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.insert
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.pop
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.remove
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.reverse
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.select_leaves
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.scoretools.Score.Score.__contains__
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.__copy__
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.__delitem__
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.__eq__
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.__format__
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.__getitem__
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.__graph__
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.__hash__
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.__illustrate__
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.__len__
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.__mul__
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.__ne__
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.__repr__
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.__rmul__
   :noindex:

.. automethod:: abjad.tools.scoretools.Score.Score.__setitem__
   :noindex:
