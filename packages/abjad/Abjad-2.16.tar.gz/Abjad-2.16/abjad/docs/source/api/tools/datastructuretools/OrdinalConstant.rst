datastructuretools.OrdinalConstant
==================================

.. autoclass:: abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant

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
           "datastructuretools.OrdinalConstant" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>OrdinalConstant</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.OrdinalConstant";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__eq__
      ~abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__format__
      ~abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__ge__
      ~abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__gt__
      ~abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__hash__
      ~abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__le__
      ~abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__lt__
      ~abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__ne__
      ~abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__new__
      ~abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__eq__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__format__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__ge__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__gt__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__hash__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__le__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__lt__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__ne__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__new__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.OrdinalConstant.OrdinalConstant.__repr__
   :noindex:
