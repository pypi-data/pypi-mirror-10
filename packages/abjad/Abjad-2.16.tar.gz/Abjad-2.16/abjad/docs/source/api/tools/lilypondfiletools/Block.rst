lilypondfiletools.Block
=======================

.. autoclass:: abjad.tools.lilypondfiletools.Block.Block

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
       subgraph cluster_lilypondfiletools {
           graph [label=lilypondfiletools];
           "lilypondfiletools.Block" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Block</B>>,
               shape=box,
               style="filled, rounded"];
           "lilypondfiletools.ContextBlock" [color=3,
               group=2,
               label=ContextBlock,
               shape=box];
           "lilypondfiletools.Block" -> "lilypondfiletools.ContextBlock";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "lilypondfiletools.Block";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.lilypondfiletools.Block.Block.items
      ~abjad.tools.lilypondfiletools.Block.Block.name
      ~abjad.tools.lilypondfiletools.Block.Block.__eq__
      ~abjad.tools.lilypondfiletools.Block.Block.__format__
      ~abjad.tools.lilypondfiletools.Block.Block.__getitem__
      ~abjad.tools.lilypondfiletools.Block.Block.__hash__
      ~abjad.tools.lilypondfiletools.Block.Block.__ne__
      ~abjad.tools.lilypondfiletools.Block.Block.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.lilypondfiletools.Block.Block.items
   :noindex:

.. autoattribute:: abjad.tools.lilypondfiletools.Block.Block.name
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.lilypondfiletools.Block.Block.__eq__
   :noindex:

.. automethod:: abjad.tools.lilypondfiletools.Block.Block.__format__
   :noindex:

.. automethod:: abjad.tools.lilypondfiletools.Block.Block.__getitem__
   :noindex:

.. automethod:: abjad.tools.lilypondfiletools.Block.Block.__hash__
   :noindex:

.. automethod:: abjad.tools.lilypondfiletools.Block.Block.__ne__
   :noindex:

.. automethod:: abjad.tools.lilypondfiletools.Block.Block.__repr__
   :noindex:
