datastructuretools.CyclicTuple
==============================

.. autoclass:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple

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
           "__builtin__.tuple" [color=1,
               group=0,
               label=tuple,
               shape=box];
           "__builtin__.object" -> "__builtin__.tuple";
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
           "datastructuretools.CyclicTuple" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>CyclicTuple</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "__builtin__.tuple" -> "datastructuretools.CyclicTuple";
       "abctools.AbjadObject" -> "datastructuretools.CyclicTuple";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.count
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.index
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__add__
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__contains__
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__eq__
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__format__
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__ge__
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__getitem__
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__getslice__
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__gt__
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__hash__
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__iter__
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__le__
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__len__
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__lt__
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__mul__
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__ne__
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__repr__
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__rmul__
      ~abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__str__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.tuple <tuple>`

- :py:class:`__builtin__.object <object>`

Methods
-------

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.count
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.index
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__add__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__contains__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__eq__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__format__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__ge__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__getitem__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__getslice__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__gt__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__hash__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__iter__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__le__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__len__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__lt__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__mul__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__ne__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__repr__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__rmul__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.CyclicTuple.CyclicTuple.__str__
   :noindex:
