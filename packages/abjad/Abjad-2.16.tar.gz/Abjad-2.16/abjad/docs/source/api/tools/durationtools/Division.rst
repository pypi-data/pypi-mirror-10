durationtools.Division
======================

.. autoclass:: abjad.tools.durationtools.Division.Division

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
           "durationtools.Division" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Division</B>>,
               shape=box,
               style="filled, rounded"];
       }
       subgraph cluster_mathtools {
           graph [label=mathtools];
           "mathtools.NonreducedFraction" [color=5,
               group=4,
               label=NonreducedFraction,
               shape=box];
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

      ~abjad.tools.durationtools.Division.Division.conjugate
      ~abjad.tools.durationtools.Division.Division.denominator
      ~abjad.tools.durationtools.Division.Division.from_decimal
      ~abjad.tools.durationtools.Division.Division.from_float
      ~abjad.tools.durationtools.Division.Division.imag
      ~abjad.tools.durationtools.Division.Division.limit_denominator
      ~abjad.tools.durationtools.Division.Division.multiply_with_cross_cancelation
      ~abjad.tools.durationtools.Division.Division.multiply_with_numerator_preservation
      ~abjad.tools.durationtools.Division.Division.multiply_without_reducing
      ~abjad.tools.durationtools.Division.Division.numerator
      ~abjad.tools.durationtools.Division.Division.pair
      ~abjad.tools.durationtools.Division.Division.real
      ~abjad.tools.durationtools.Division.Division.reduce
      ~abjad.tools.durationtools.Division.Division.with_denominator
      ~abjad.tools.durationtools.Division.Division.with_multiple_of_denominator
      ~abjad.tools.durationtools.Division.Division.__abs__
      ~abjad.tools.durationtools.Division.Division.__add__
      ~abjad.tools.durationtools.Division.Division.__complex__
      ~abjad.tools.durationtools.Division.Division.__copy__
      ~abjad.tools.durationtools.Division.Division.__deepcopy__
      ~abjad.tools.durationtools.Division.Division.__div__
      ~abjad.tools.durationtools.Division.Division.__divmod__
      ~abjad.tools.durationtools.Division.Division.__eq__
      ~abjad.tools.durationtools.Division.Division.__float__
      ~abjad.tools.durationtools.Division.Division.__floordiv__
      ~abjad.tools.durationtools.Division.Division.__format__
      ~abjad.tools.durationtools.Division.Division.__ge__
      ~abjad.tools.durationtools.Division.Division.__gt__
      ~abjad.tools.durationtools.Division.Division.__hash__
      ~abjad.tools.durationtools.Division.Division.__le__
      ~abjad.tools.durationtools.Division.Division.__lt__
      ~abjad.tools.durationtools.Division.Division.__mod__
      ~abjad.tools.durationtools.Division.Division.__mul__
      ~abjad.tools.durationtools.Division.Division.__ne__
      ~abjad.tools.durationtools.Division.Division.__neg__
      ~abjad.tools.durationtools.Division.Division.__new__
      ~abjad.tools.durationtools.Division.Division.__nonzero__
      ~abjad.tools.durationtools.Division.Division.__pos__
      ~abjad.tools.durationtools.Division.Division.__pow__
      ~abjad.tools.durationtools.Division.Division.__radd__
      ~abjad.tools.durationtools.Division.Division.__rdiv__
      ~abjad.tools.durationtools.Division.Division.__rdivmod__
      ~abjad.tools.durationtools.Division.Division.__repr__
      ~abjad.tools.durationtools.Division.Division.__rfloordiv__
      ~abjad.tools.durationtools.Division.Division.__rmod__
      ~abjad.tools.durationtools.Division.Division.__rmul__
      ~abjad.tools.durationtools.Division.Division.__rpow__
      ~abjad.tools.durationtools.Division.Division.__rsub__
      ~abjad.tools.durationtools.Division.Division.__rtruediv__
      ~abjad.tools.durationtools.Division.Division.__str__
      ~abjad.tools.durationtools.Division.Division.__sub__
      ~abjad.tools.durationtools.Division.Division.__truediv__
      ~abjad.tools.durationtools.Division.Division.__trunc__

Bases
-----

- :py:class:`mathtools.NonreducedFraction <abjad.tools.mathtools.NonreducedFraction.NonreducedFraction>`

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

.. autoattribute:: abjad.tools.durationtools.Division.Division.denominator
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Division.Division.imag
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Division.Division.numerator
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Division.Division.pair
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Division.Division.real
   :noindex:

Methods
-------

.. automethod:: abjad.tools.durationtools.Division.Division.conjugate
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.limit_denominator
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.multiply_with_cross_cancelation
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.multiply_with_numerator_preservation
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.multiply_without_reducing
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.reduce
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.with_denominator
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.with_multiple_of_denominator
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.durationtools.Division.Division.from_decimal
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.from_float
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.durationtools.Division.Division.__abs__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__add__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__complex__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__copy__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__div__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__divmod__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__eq__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__float__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__floordiv__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__format__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__ge__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__gt__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__hash__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__le__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__lt__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__mod__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__mul__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__ne__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__neg__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__new__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__nonzero__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__pos__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__pow__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__radd__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__rdiv__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__rdivmod__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__repr__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__rfloordiv__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__rmod__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__rmul__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__rpow__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__rsub__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__rtruediv__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__str__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__sub__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__truediv__
   :noindex:

.. automethod:: abjad.tools.durationtools.Division.Division.__trunc__
   :noindex:
