sievetools.BaseResidueClass
===========================

.. autoclass:: abjad.tools.sievetools.BaseResidueClass.BaseResidueClass

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
       subgraph cluster_sievetools {
           graph [label=sievetools];
           "sievetools.BaseResidueClass" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>BaseResidueClass</B>>,
               shape=box,
               style="filled, rounded"];
           "sievetools.ResidueClass" [color=3,
               group=2,
               label=ResidueClass,
               shape=box];
           "sievetools.Sieve" [color=3,
               group=2,
               label=Sieve,
               shape=box];
           "sievetools.BaseResidueClass" -> "sievetools.ResidueClass";
           "sievetools.BaseResidueClass" -> "sievetools.Sieve";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "sievetools.BaseResidueClass";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.sievetools.BaseResidueClass.BaseResidueClass.__and__
      ~abjad.tools.sievetools.BaseResidueClass.BaseResidueClass.__eq__
      ~abjad.tools.sievetools.BaseResidueClass.BaseResidueClass.__format__
      ~abjad.tools.sievetools.BaseResidueClass.BaseResidueClass.__hash__
      ~abjad.tools.sievetools.BaseResidueClass.BaseResidueClass.__ne__
      ~abjad.tools.sievetools.BaseResidueClass.BaseResidueClass.__or__
      ~abjad.tools.sievetools.BaseResidueClass.BaseResidueClass.__repr__
      ~abjad.tools.sievetools.BaseResidueClass.BaseResidueClass.__xor__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.sievetools.BaseResidueClass.BaseResidueClass.__and__
   :noindex:

.. automethod:: abjad.tools.sievetools.BaseResidueClass.BaseResidueClass.__eq__
   :noindex:

.. automethod:: abjad.tools.sievetools.BaseResidueClass.BaseResidueClass.__format__
   :noindex:

.. automethod:: abjad.tools.sievetools.BaseResidueClass.BaseResidueClass.__hash__
   :noindex:

.. automethod:: abjad.tools.sievetools.BaseResidueClass.BaseResidueClass.__ne__
   :noindex:

.. automethod:: abjad.tools.sievetools.BaseResidueClass.BaseResidueClass.__or__
   :noindex:

.. automethod:: abjad.tools.sievetools.BaseResidueClass.BaseResidueClass.__repr__
   :noindex:

.. automethod:: abjad.tools.sievetools.BaseResidueClass.BaseResidueClass.__xor__
   :noindex:
