abctools.AbjadObject
====================

.. autoclass:: abjad.tools.abctools.AbjadObject.AbjadObject

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
           "abctools.AbjadObject" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>AbjadObject</B>>,
               shape=box,
               style="filled, rounded"];
           "abctools.AbjadObject.AbstractBase" [color=2,
               group=1,
               label=AbstractBase,
               shape=box];
           "abctools.AbjadObject.AbstractBase" -> "abctools.AbjadObject";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.abctools.AbjadObject.AbjadObject.__eq__
      ~abjad.tools.abctools.AbjadObject.AbjadObject.__format__
      ~abjad.tools.abctools.AbjadObject.AbjadObject.__hash__
      ~abjad.tools.abctools.AbjadObject.AbjadObject.__ne__
      ~abjad.tools.abctools.AbjadObject.AbjadObject.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.abctools.AbjadObject.AbjadObject.__eq__
   :noindex:

.. automethod:: abjad.tools.abctools.AbjadObject.AbjadObject.__format__
   :noindex:

.. automethod:: abjad.tools.abctools.AbjadObject.AbjadObject.__hash__
   :noindex:

.. automethod:: abjad.tools.abctools.AbjadObject.AbjadObject.__ne__
   :noindex:

.. automethod:: abjad.tools.abctools.AbjadObject.AbjadObject.__repr__
   :noindex:
