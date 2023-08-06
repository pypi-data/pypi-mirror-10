abctools.AbjadValueObject
=========================

.. autoclass:: abjad.tools.abctools.AbjadValueObject.AbjadValueObject

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
           "abctools.AbjadValueObject" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>AbjadValueObject</B>>,
               shape=box,
               style="filled, rounded"];
           "abctools.AbjadObject" -> "abctools.AbjadValueObject";
           "abctools.AbjadObject.AbstractBase" -> "abctools.AbjadObject";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.abctools.AbjadValueObject.AbjadValueObject.__copy__
      ~abjad.tools.abctools.AbjadValueObject.AbjadValueObject.__eq__
      ~abjad.tools.abctools.AbjadValueObject.AbjadValueObject.__format__
      ~abjad.tools.abctools.AbjadValueObject.AbjadValueObject.__hash__
      ~abjad.tools.abctools.AbjadValueObject.AbjadValueObject.__ne__
      ~abjad.tools.abctools.AbjadValueObject.AbjadValueObject.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.abctools.AbjadValueObject.AbjadValueObject.__copy__
   :noindex:

.. automethod:: abjad.tools.abctools.AbjadValueObject.AbjadValueObject.__eq__
   :noindex:

.. automethod:: abjad.tools.abctools.AbjadValueObject.AbjadValueObject.__format__
   :noindex:

.. automethod:: abjad.tools.abctools.AbjadValueObject.AbjadValueObject.__hash__
   :noindex:

.. automethod:: abjad.tools.abctools.AbjadValueObject.AbjadValueObject.__ne__
   :noindex:

.. automethod:: abjad.tools.abctools.AbjadValueObject.AbjadValueObject.__repr__
   :noindex:
