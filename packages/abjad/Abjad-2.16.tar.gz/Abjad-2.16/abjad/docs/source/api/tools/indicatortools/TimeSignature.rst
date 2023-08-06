indicatortools.TimeSignature
============================

.. autoclass:: abjad.tools.indicatortools.TimeSignature.TimeSignature

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
           "abctools.AbjadValueObject" [color=2,
               group=1,
               label=AbjadValueObject,
               shape=box];
           "abctools.AbjadObject" -> "abctools.AbjadValueObject";
           "abctools.AbjadObject.AbstractBase" -> "abctools.AbjadObject";
       }
       subgraph cluster_indicatortools {
           graph [label=indicatortools];
           "indicatortools.TimeSignature" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>TimeSignature</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "indicatortools.TimeSignature";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.denominator
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.duration
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.has_non_power_of_two_denominator
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.implied_prolation
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.numerator
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.pair
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.partial
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.suppress
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.with_power_of_two_denominator
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.__add__
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.__copy__
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.__eq__
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.__format__
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.__ge__
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.__gt__
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.__hash__
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.__le__
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.__lt__
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.__ne__
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.__radd__
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.__repr__
      ~abjad.tools.indicatortools.TimeSignature.TimeSignature.__str__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.indicatortools.TimeSignature.TimeSignature.denominator
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.TimeSignature.TimeSignature.duration
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.TimeSignature.TimeSignature.has_non_power_of_two_denominator
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.TimeSignature.TimeSignature.implied_prolation
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.TimeSignature.TimeSignature.numerator
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.TimeSignature.TimeSignature.pair
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.TimeSignature.TimeSignature.partial
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.indicatortools.TimeSignature.TimeSignature.suppress
   :noindex:

Methods
-------

.. automethod:: abjad.tools.indicatortools.TimeSignature.TimeSignature.with_power_of_two_denominator
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.indicatortools.TimeSignature.TimeSignature.__add__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignature.TimeSignature.__copy__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignature.TimeSignature.__eq__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignature.TimeSignature.__format__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignature.TimeSignature.__ge__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignature.TimeSignature.__gt__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignature.TimeSignature.__hash__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignature.TimeSignature.__le__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignature.TimeSignature.__lt__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignature.TimeSignature.__ne__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignature.TimeSignature.__radd__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignature.TimeSignature.__repr__
   :noindex:

.. automethod:: abjad.tools.indicatortools.TimeSignature.TimeSignature.__str__
   :noindex:
