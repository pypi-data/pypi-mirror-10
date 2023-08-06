sievetools.ResidueClass
=======================

.. autoclass:: abjad.tools.sievetools.ResidueClass.ResidueClass

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
           "sievetools.BaseResidueClass" [color=3,
               group=2,
               label=BaseResidueClass,
               shape=box];
           "sievetools.ResidueClass" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>ResidueClass</B>>,
               shape=box,
               style="filled, rounded"];
           "sievetools.BaseResidueClass" -> "sievetools.ResidueClass";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "sievetools.BaseResidueClass";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.sievetools.ResidueClass.ResidueClass.get_boolean_train
      ~abjad.tools.sievetools.ResidueClass.ResidueClass.get_congruent_bases
      ~abjad.tools.sievetools.ResidueClass.ResidueClass.modulo
      ~abjad.tools.sievetools.ResidueClass.ResidueClass.residue
      ~abjad.tools.sievetools.ResidueClass.ResidueClass.__and__
      ~abjad.tools.sievetools.ResidueClass.ResidueClass.__eq__
      ~abjad.tools.sievetools.ResidueClass.ResidueClass.__format__
      ~abjad.tools.sievetools.ResidueClass.ResidueClass.__ge__
      ~abjad.tools.sievetools.ResidueClass.ResidueClass.__gt__
      ~abjad.tools.sievetools.ResidueClass.ResidueClass.__hash__
      ~abjad.tools.sievetools.ResidueClass.ResidueClass.__le__
      ~abjad.tools.sievetools.ResidueClass.ResidueClass.__lt__
      ~abjad.tools.sievetools.ResidueClass.ResidueClass.__ne__
      ~abjad.tools.sievetools.ResidueClass.ResidueClass.__or__
      ~abjad.tools.sievetools.ResidueClass.ResidueClass.__repr__
      ~abjad.tools.sievetools.ResidueClass.ResidueClass.__xor__

Bases
-----

- :py:class:`sievetools.BaseResidueClass <abjad.tools.sievetools.BaseResidueClass.BaseResidueClass>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.sievetools.ResidueClass.ResidueClass.modulo
   :noindex:

.. autoattribute:: abjad.tools.sievetools.ResidueClass.ResidueClass.residue
   :noindex:

Methods
-------

.. automethod:: abjad.tools.sievetools.ResidueClass.ResidueClass.get_boolean_train
   :noindex:

.. automethod:: abjad.tools.sievetools.ResidueClass.ResidueClass.get_congruent_bases
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.sievetools.ResidueClass.ResidueClass.__and__
   :noindex:

.. automethod:: abjad.tools.sievetools.ResidueClass.ResidueClass.__eq__
   :noindex:

.. automethod:: abjad.tools.sievetools.ResidueClass.ResidueClass.__format__
   :noindex:

.. automethod:: abjad.tools.sievetools.ResidueClass.ResidueClass.__ge__
   :noindex:

.. automethod:: abjad.tools.sievetools.ResidueClass.ResidueClass.__gt__
   :noindex:

.. automethod:: abjad.tools.sievetools.ResidueClass.ResidueClass.__hash__
   :noindex:

.. automethod:: abjad.tools.sievetools.ResidueClass.ResidueClass.__le__
   :noindex:

.. automethod:: abjad.tools.sievetools.ResidueClass.ResidueClass.__lt__
   :noindex:

.. automethod:: abjad.tools.sievetools.ResidueClass.ResidueClass.__ne__
   :noindex:

.. automethod:: abjad.tools.sievetools.ResidueClass.ResidueClass.__or__
   :noindex:

.. automethod:: abjad.tools.sievetools.ResidueClass.ResidueClass.__repr__
   :noindex:

.. automethod:: abjad.tools.sievetools.ResidueClass.ResidueClass.__xor__
   :noindex:
