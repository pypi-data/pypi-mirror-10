datastructuretools.StatalServer
===============================

.. autoclass:: abjad.tools.datastructuretools.StatalServer.StatalServer

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
           "datastructuretools.StatalServer" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>StatalServer</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.StatalServer";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.datastructuretools.StatalServer.StatalServer.cyclic_tree
      ~abjad.tools.datastructuretools.StatalServer.StatalServer.last_node
      ~abjad.tools.datastructuretools.StatalServer.StatalServer.__call__
      ~abjad.tools.datastructuretools.StatalServer.StatalServer.__eq__
      ~abjad.tools.datastructuretools.StatalServer.StatalServer.__format__
      ~abjad.tools.datastructuretools.StatalServer.StatalServer.__hash__
      ~abjad.tools.datastructuretools.StatalServer.StatalServer.__ne__
      ~abjad.tools.datastructuretools.StatalServer.StatalServer.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.datastructuretools.StatalServer.StatalServer.cyclic_tree
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.StatalServer.StatalServer.last_node
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.datastructuretools.StatalServer.StatalServer.__call__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.StatalServer.StatalServer.__eq__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.StatalServer.StatalServer.__format__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.StatalServer.StatalServer.__hash__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.StatalServer.StatalServer.__ne__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.StatalServer.StatalServer.__repr__
   :noindex:
