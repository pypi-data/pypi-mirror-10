datastructuretools.Matrix
=========================

.. autoclass:: abjad.tools.datastructuretools.Matrix.Matrix

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
       subgraph cluster_datastructuretools {
           graph [label=datastructuretools];
           "datastructuretools.CyclicMatrix" [color=3,
               group=2,
               label=CyclicMatrix,
               shape=box];
           "datastructuretools.Matrix" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Matrix</B>>,
               shape=box,
               style="filled, rounded"];
           "datastructuretools.Matrix" -> "datastructuretools.CyclicMatrix";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.Matrix";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.datastructuretools.Matrix.Matrix.columns
      ~abjad.tools.datastructuretools.Matrix.Matrix.rows
      ~abjad.tools.datastructuretools.Matrix.Matrix.__eq__
      ~abjad.tools.datastructuretools.Matrix.Matrix.__format__
      ~abjad.tools.datastructuretools.Matrix.Matrix.__getitem__
      ~abjad.tools.datastructuretools.Matrix.Matrix.__hash__
      ~abjad.tools.datastructuretools.Matrix.Matrix.__ne__
      ~abjad.tools.datastructuretools.Matrix.Matrix.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.datastructuretools.Matrix.Matrix.columns
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.Matrix.Matrix.rows
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.datastructuretools.Matrix.Matrix.__eq__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.Matrix.Matrix.__format__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.Matrix.Matrix.__getitem__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.Matrix.Matrix.__hash__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.Matrix.Matrix.__ne__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.Matrix.Matrix.__repr__
   :noindex:
