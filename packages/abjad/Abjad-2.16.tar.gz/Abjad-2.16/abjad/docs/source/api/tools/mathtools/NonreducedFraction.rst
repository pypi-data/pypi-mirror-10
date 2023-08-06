mathtools.NonreducedFraction
============================

.. autoclass:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction

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
       subgraph cluster_durationtools {
           graph [label=durationtools];
           "durationtools.Division" [color=3,
               group=2,
               label=Division,
               shape=box];
       }
       subgraph cluster_mathtools {
           graph [label=mathtools];
           "mathtools.NonreducedFraction" [color=black,
               fontcolor=white,
               group=4,
               label=<<B>NonreducedFraction</B>>,
               shape=box,
               style="filled, rounded"];
       }
       subgraph cluster_fractions {
           graph [label=fractions];
           "fractions.Fraction" [color=4,
               group=3,
               label=Fraction,
               shape=box];
       }
       subgraph cluster_numbers {
           graph [label=numbers];
           "numbers.Complex" [color=6,
               group=5,
               label=Complex,
               shape=oval,
               style=bold];
           "numbers.Number" [color=6,
               group=5,
               label=Number,
               shape=box];
           "numbers.Rational" [color=6,
               group=5,
               label=Rational,
               shape=oval,
               style=bold];
           "numbers.Real" [color=6,
               group=5,
               label=Real,
               shape=oval,
               style=bold];
           "numbers.Complex" -> "numbers.Real";
           "numbers.Number" -> "numbers.Complex";
           "numbers.Real" -> "numbers.Rational";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "__builtin__.object" -> "numbers.Number";
       "abctools.AbjadObject" -> "mathtools.NonreducedFraction";
       "mathtools.NonreducedFraction" -> "durationtools.Division";
       "fractions.Fraction" -> "mathtools.NonreducedFraction";
       "numbers.Rational" -> "fractions.Fraction";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.conjugate
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.denominator
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.from_decimal
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.from_float
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.imag
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.limit_denominator
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.multiply_with_cross_cancelation
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.multiply_with_numerator_preservation
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.multiply_without_reducing
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.numerator
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.pair
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.real
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.reduce
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.with_denominator
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.with_multiple_of_denominator
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__abs__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__add__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__complex__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__copy__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__deepcopy__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__div__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__divmod__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__eq__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__float__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__floordiv__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__format__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__ge__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__gt__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__hash__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__le__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__lt__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__mod__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__mul__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__ne__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__neg__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__new__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__nonzero__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__pos__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__pow__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__radd__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__rdiv__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__rdivmod__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__repr__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__rfloordiv__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__rmod__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__rmul__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__rpow__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__rsub__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__rtruediv__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__str__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__sub__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__truediv__
      ~abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__trunc__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`fractions.Fraction <fractions.Fraction>`

- :py:class:`numbers.Rational <numbers.Rational>`

- :py:class:`numbers.Real <numbers.Real>`

- :py:class:`numbers.Complex <numbers.Complex>`

- :py:class:`numbers.Number <numbers.Number>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.denominator
   :noindex:

.. autoattribute:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.imag
   :noindex:

.. autoattribute:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.numerator
   :noindex:

.. autoattribute:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.pair
   :noindex:

.. autoattribute:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.real
   :noindex:

Methods
-------

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.conjugate
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.limit_denominator
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.multiply_with_cross_cancelation
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.multiply_with_numerator_preservation
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.multiply_without_reducing
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.reduce
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.with_denominator
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.with_multiple_of_denominator
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.from_decimal
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.from_float
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__abs__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__add__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__complex__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__copy__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__div__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__divmod__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__eq__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__float__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__floordiv__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__format__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__ge__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__gt__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__hash__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__le__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__lt__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__mod__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__mul__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__ne__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__neg__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__new__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__nonzero__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__pos__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__pow__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__radd__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__rdiv__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__rdivmod__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__repr__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__rfloordiv__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__rmod__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__rmul__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__rpow__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__rsub__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__rtruediv__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__str__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__sub__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__truediv__
   :noindex:

.. automethod:: abjad.tools.mathtools.NonreducedFraction.NonreducedFraction.__trunc__
   :noindex:
