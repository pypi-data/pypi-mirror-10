datastructuretools.StatalServerCursor
=====================================

.. autoclass:: abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor

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
           "datastructuretools.StatalServerCursor" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>StatalServerCursor</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.StatalServerCursor";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.position
      ~abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.reverse
      ~abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.statal_server
      ~abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.__call__
      ~abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.__eq__
      ~abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.__format__
      ~abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.__hash__
      ~abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.__ne__
      ~abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.position
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.reverse
   :noindex:

.. autoattribute:: abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.statal_server
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.__call__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.__eq__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.__format__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.__hash__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.__ne__
   :noindex:

.. automethod:: abjad.tools.datastructuretools.StatalServerCursor.StatalServerCursor.__repr__
   :noindex:
