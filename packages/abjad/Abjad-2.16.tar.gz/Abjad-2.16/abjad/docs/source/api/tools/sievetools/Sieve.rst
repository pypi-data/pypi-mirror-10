sievetools.Sieve
================

.. autoclass:: abjad.tools.sievetools.Sieve.Sieve

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
           "sievetools.Sieve" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Sieve</B>>,
               shape=box,
               style="filled, rounded"];
           "sievetools.BaseResidueClass" -> "sievetools.Sieve";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "sievetools.BaseResidueClass";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.sievetools.Sieve.Sieve.from_cycle_tokens
      ~abjad.tools.sievetools.Sieve.Sieve.get_boolean_train
      ~abjad.tools.sievetools.Sieve.Sieve.get_congruent_bases
      ~abjad.tools.sievetools.Sieve.Sieve.is_congruent_base
      ~abjad.tools.sievetools.Sieve.Sieve.logical_operator
      ~abjad.tools.sievetools.Sieve.Sieve.period
      ~abjad.tools.sievetools.Sieve.Sieve.rcs
      ~abjad.tools.sievetools.Sieve.Sieve.representative_boolean_train
      ~abjad.tools.sievetools.Sieve.Sieve.representative_congruent_bases
      ~abjad.tools.sievetools.Sieve.Sieve.__and__
      ~abjad.tools.sievetools.Sieve.Sieve.__eq__
      ~abjad.tools.sievetools.Sieve.Sieve.__format__
      ~abjad.tools.sievetools.Sieve.Sieve.__hash__
      ~abjad.tools.sievetools.Sieve.Sieve.__ne__
      ~abjad.tools.sievetools.Sieve.Sieve.__or__
      ~abjad.tools.sievetools.Sieve.Sieve.__repr__
      ~abjad.tools.sievetools.Sieve.Sieve.__xor__

Bases
-----

- :py:class:`sievetools.BaseResidueClass <abjad.tools.sievetools.BaseResidueClass.BaseResidueClass>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.sievetools.Sieve.Sieve.logical_operator
   :noindex:

.. autoattribute:: abjad.tools.sievetools.Sieve.Sieve.period
   :noindex:

.. autoattribute:: abjad.tools.sievetools.Sieve.Sieve.rcs
   :noindex:

.. autoattribute:: abjad.tools.sievetools.Sieve.Sieve.representative_boolean_train
   :noindex:

.. autoattribute:: abjad.tools.sievetools.Sieve.Sieve.representative_congruent_bases
   :noindex:

Methods
-------

.. automethod:: abjad.tools.sievetools.Sieve.Sieve.get_boolean_train
   :noindex:

.. automethod:: abjad.tools.sievetools.Sieve.Sieve.get_congruent_bases
   :noindex:

.. automethod:: abjad.tools.sievetools.Sieve.Sieve.is_congruent_base
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.sievetools.Sieve.Sieve.from_cycle_tokens
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.sievetools.Sieve.Sieve.__and__
   :noindex:

.. automethod:: abjad.tools.sievetools.Sieve.Sieve.__eq__
   :noindex:

.. automethod:: abjad.tools.sievetools.Sieve.Sieve.__format__
   :noindex:

.. automethod:: abjad.tools.sievetools.Sieve.Sieve.__hash__
   :noindex:

.. automethod:: abjad.tools.sievetools.Sieve.Sieve.__ne__
   :noindex:

.. automethod:: abjad.tools.sievetools.Sieve.Sieve.__or__
   :noindex:

.. automethod:: abjad.tools.sievetools.Sieve.Sieve.__repr__
   :noindex:

.. automethod:: abjad.tools.sievetools.Sieve.Sieve.__xor__
   :noindex:
