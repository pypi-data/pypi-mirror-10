scoretools.GraceContainer
=========================

.. autoclass:: abjad.tools.scoretools.GraceContainer.GraceContainer

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
           "scoretools.GraceContainer" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>GraceContainer</B>>,
               shape=box,
               style="filled, rounded"];
           "scoretools.Component" -> "scoretools.Container";
           "scoretools.Container" -> "scoretools.GraceContainer";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "scoretools.Component";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.scoretools.GraceContainer.GraceContainer.append
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.extend
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.index
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.insert
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.is_simultaneous
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.kind
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.name
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.pop
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.remove
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.reverse
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.select_leaves
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.__contains__
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.__copy__
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.__delitem__
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.__eq__
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.__format__
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.__getitem__
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.__graph__
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.__hash__
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.__illustrate__
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.__len__
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.__mul__
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.__ne__
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.__repr__
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.__rmul__
      ~abjad.tools.scoretools.GraceContainer.GraceContainer.__setitem__

Bases
-----

- :py:class:`scoretools.Container <abjad.tools.scoretools.Container.Container>`

- :py:class:`scoretools.Component <abjad.tools.scoretools.Component.Component>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read/write properties
---------------------

.. autoattribute:: abjad.tools.scoretools.GraceContainer.GraceContainer.is_simultaneous
   :noindex:

.. autoattribute:: abjad.tools.scoretools.GraceContainer.GraceContainer.kind
   :noindex:

.. autoattribute:: abjad.tools.scoretools.GraceContainer.GraceContainer.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.append
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.extend
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.index
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.insert
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.pop
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.remove
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.reverse
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.select_leaves
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.__contains__
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.__copy__
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.__delitem__
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.__eq__
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.__format__
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.__getitem__
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.__graph__
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.__hash__
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.__illustrate__
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.__len__
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.__mul__
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.__ne__
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.__repr__
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.__rmul__
   :noindex:

.. automethod:: abjad.tools.scoretools.GraceContainer.GraceContainer.__setitem__
   :noindex:
