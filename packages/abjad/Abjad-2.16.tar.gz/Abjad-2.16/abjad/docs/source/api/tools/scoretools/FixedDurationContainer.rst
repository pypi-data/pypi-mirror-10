scoretools.FixedDurationContainer
=================================

.. autoclass:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer

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
           "scoretools.FixedDurationContainer" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>FixedDurationContainer</B>>,
               shape=box,
               style="filled, rounded"];
           "scoretools.Measure" [color=3,
               group=2,
               label=Measure,
               shape=box];
           "scoretools.Component" -> "scoretools.Container";
           "scoretools.Container" -> "scoretools.FixedDurationContainer";
           "scoretools.FixedDurationContainer" -> "scoretools.Measure";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "scoretools.Component";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.append
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.extend
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.index
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.insert
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.is_full
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.is_misfilled
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.is_overfull
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.is_simultaneous
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.is_underfull
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.name
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.pop
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.remove
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.reverse
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.select_leaves
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.target_duration
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__contains__
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__copy__
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__delitem__
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__eq__
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__format__
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__getitem__
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__graph__
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__hash__
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__illustrate__
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__len__
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__mul__
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__ne__
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__repr__
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__rmul__
      ~abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__setitem__

Bases
-----

- :py:class:`scoretools.Container <abjad.tools.scoretools.Container.Container>`

- :py:class:`scoretools.Component <abjad.tools.scoretools.Component.Component>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.is_full
   :noindex:

.. autoattribute:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.is_misfilled
   :noindex:

.. autoattribute:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.is_overfull
   :noindex:

.. autoattribute:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.is_underfull
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.is_simultaneous
   :noindex:

.. autoattribute:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.name
   :noindex:

.. autoattribute:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.target_duration
   :noindex:

Methods
-------

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.append
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.extend
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.index
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.insert
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.pop
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.remove
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.reverse
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.select_leaves
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__contains__
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__copy__
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__delitem__
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__eq__
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__format__
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__getitem__
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__graph__
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__hash__
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__illustrate__
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__len__
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__mul__
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__ne__
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__repr__
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__rmul__
   :noindex:

.. automethod:: abjad.tools.scoretools.FixedDurationContainer.FixedDurationContainer.__setitem__
   :noindex:
