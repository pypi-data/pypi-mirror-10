durationtools.Multiplier
========================

.. autoclass:: abjad.tools.durationtools.Multiplier.Multiplier

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
           "durationtools.Duration" [color=3,
               group=2,
               label=Duration,
               shape=box];
           "durationtools.Multiplier" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Multiplier</B>>,
               shape=box,
               style="filled, rounded"];
           "durationtools.Duration" -> "durationtools.Multiplier";
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
           "numbers.Complex" [color=5,
               group=4,
               label=Complex,
               shape=oval,
               style=bold];
           "numbers.Number" [color=5,
               group=4,
               label=Number,
               shape=box];
           "numbers.Rational" [color=5,
               group=4,
               label=Rational,
               shape=oval,
               style=bold];
           "numbers.Real" [color=5,
               group=4,
               label=Real,
               shape=oval,
               style=bold];
           "numbers.Complex" -> "numbers.Real";
           "numbers.Number" -> "numbers.Complex";
           "numbers.Real" -> "numbers.Rational";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "__builtin__.object" -> "numbers.Number";
       "abctools.AbjadObject" -> "durationtools.Duration";
       "fractions.Fraction" -> "durationtools.Duration";
       "numbers.Rational" -> "fractions.Fraction";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.durationtools.Multiplier.Multiplier.conjugate
      ~abjad.tools.durationtools.Multiplier.Multiplier.denominator
      ~abjad.tools.durationtools.Multiplier.Multiplier.dot_count
      ~abjad.tools.durationtools.Multiplier.Multiplier.durations_to_nonreduced_fractions
      ~abjad.tools.durationtools.Multiplier.Multiplier.equal_or_greater_assignable
      ~abjad.tools.durationtools.Multiplier.Multiplier.equal_or_greater_power_of_two
      ~abjad.tools.durationtools.Multiplier.Multiplier.equal_or_lesser_assignable
      ~abjad.tools.durationtools.Multiplier.Multiplier.equal_or_lesser_power_of_two
      ~abjad.tools.durationtools.Multiplier.Multiplier.flag_count
      ~abjad.tools.durationtools.Multiplier.Multiplier.from_decimal
      ~abjad.tools.durationtools.Multiplier.Multiplier.from_float
      ~abjad.tools.durationtools.Multiplier.Multiplier.from_lilypond_duration_string
      ~abjad.tools.durationtools.Multiplier.Multiplier.has_power_of_two_denominator
      ~abjad.tools.durationtools.Multiplier.Multiplier.imag
      ~abjad.tools.durationtools.Multiplier.Multiplier.implied_prolation
      ~abjad.tools.durationtools.Multiplier.Multiplier.is_assignable
      ~abjad.tools.durationtools.Multiplier.Multiplier.is_proper_tuplet_multiplier
      ~abjad.tools.durationtools.Multiplier.Multiplier.is_token
      ~abjad.tools.durationtools.Multiplier.Multiplier.lilypond_duration_string
      ~abjad.tools.durationtools.Multiplier.Multiplier.limit_denominator
      ~abjad.tools.durationtools.Multiplier.Multiplier.numerator
      ~abjad.tools.durationtools.Multiplier.Multiplier.pair
      ~abjad.tools.durationtools.Multiplier.Multiplier.prolation_string
      ~abjad.tools.durationtools.Multiplier.Multiplier.real
      ~abjad.tools.durationtools.Multiplier.Multiplier.reciprocal
      ~abjad.tools.durationtools.Multiplier.Multiplier.to_clock_string
      ~abjad.tools.durationtools.Multiplier.Multiplier.to_score_markup
      ~abjad.tools.durationtools.Multiplier.Multiplier.with_denominator
      ~abjad.tools.durationtools.Multiplier.Multiplier.yield_durations
      ~abjad.tools.durationtools.Multiplier.Multiplier.yield_equivalent_durations
      ~abjad.tools.durationtools.Multiplier.Multiplier.__abs__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__add__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__complex__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__copy__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__deepcopy__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__div__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__divmod__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__eq__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__float__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__floordiv__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__format__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__ge__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__gt__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__hash__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__le__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__lt__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__mod__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__mul__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__ne__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__neg__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__new__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__nonzero__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__pos__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__pow__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__radd__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__rdiv__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__rdivmod__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__repr__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__rfloordiv__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__rmod__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__rmul__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__rpow__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__rsub__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__rtruediv__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__str__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__sub__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__truediv__
      ~abjad.tools.durationtools.Multiplier.Multiplier.__trunc__

Bases
-----

- :py:class:`durationtools.Duration <abjad.tools.durationtools.Duration.Duration>`

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

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.denominator
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.dot_count
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.equal_or_greater_assignable
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.equal_or_greater_power_of_two
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.equal_or_lesser_assignable
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.equal_or_lesser_power_of_two
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.flag_count
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.has_power_of_two_denominator
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.imag
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.implied_prolation
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.is_assignable
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.is_proper_tuplet_multiplier
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.lilypond_duration_string
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.numerator
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.pair
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.prolation_string
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.real
   :noindex:

.. autoattribute:: abjad.tools.durationtools.Multiplier.Multiplier.reciprocal
   :noindex:

Methods
-------

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.conjugate
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.limit_denominator
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.to_clock_string
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.to_score_markup
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.with_denominator
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.yield_equivalent_durations
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.from_decimal
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.from_float
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.durations_to_nonreduced_fractions
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.from_lilypond_duration_string
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.is_token
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.yield_durations
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__abs__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__add__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__complex__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__copy__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__deepcopy__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__div__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__divmod__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__eq__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__float__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__floordiv__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__format__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__ge__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__gt__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__hash__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__le__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__lt__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__mod__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__mul__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__ne__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__neg__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__new__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__nonzero__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__pos__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__pow__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__radd__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__rdiv__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__rdivmod__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__repr__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__rfloordiv__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__rmod__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__rmul__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__rpow__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__rsub__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__rtruediv__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__str__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__sub__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__truediv__
   :noindex:

.. automethod:: abjad.tools.durationtools.Multiplier.Multiplier.__trunc__
   :noindex:
