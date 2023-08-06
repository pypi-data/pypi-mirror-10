sequencetools.Sequence
======================

.. autoclass:: abjad.tools.sequencetools.Sequence.Sequence

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
       subgraph cluster_sequencetools {
           graph [label=sequencetools];
           "sequencetools.Sequence" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Sequence</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "sequencetools.Sequence";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.sequencetools.Sequence.Sequence.degree_of_rotational_symmetry
      ~abjad.tools.sequencetools.Sequence.Sequence.is_decreasing
      ~abjad.tools.sequencetools.Sequence.Sequence.is_increasing
      ~abjad.tools.sequencetools.Sequence.Sequence.is_permutation
      ~abjad.tools.sequencetools.Sequence.Sequence.is_repetition_free
      ~abjad.tools.sequencetools.Sequence.Sequence.is_restricted_growth_function
      ~abjad.tools.sequencetools.Sequence.Sequence.period_of_rotation
      ~abjad.tools.sequencetools.Sequence.Sequence.reverse
      ~abjad.tools.sequencetools.Sequence.Sequence.rotate
      ~abjad.tools.sequencetools.Sequence.Sequence.__add__
      ~abjad.tools.sequencetools.Sequence.Sequence.__eq__
      ~abjad.tools.sequencetools.Sequence.Sequence.__format__
      ~abjad.tools.sequencetools.Sequence.Sequence.__getitem__
      ~abjad.tools.sequencetools.Sequence.Sequence.__getslice__
      ~abjad.tools.sequencetools.Sequence.Sequence.__hash__
      ~abjad.tools.sequencetools.Sequence.Sequence.__len__
      ~abjad.tools.sequencetools.Sequence.Sequence.__ne__
      ~abjad.tools.sequencetools.Sequence.Sequence.__radd__
      ~abjad.tools.sequencetools.Sequence.Sequence.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.sequencetools.Sequence.Sequence.degree_of_rotational_symmetry
   :noindex:

.. autoattribute:: abjad.tools.sequencetools.Sequence.Sequence.period_of_rotation
   :noindex:

Methods
-------

.. automethod:: abjad.tools.sequencetools.Sequence.Sequence.is_decreasing
   :noindex:

.. automethod:: abjad.tools.sequencetools.Sequence.Sequence.is_increasing
   :noindex:

.. automethod:: abjad.tools.sequencetools.Sequence.Sequence.is_permutation
   :noindex:

.. automethod:: abjad.tools.sequencetools.Sequence.Sequence.is_repetition_free
   :noindex:

.. automethod:: abjad.tools.sequencetools.Sequence.Sequence.is_restricted_growth_function
   :noindex:

.. automethod:: abjad.tools.sequencetools.Sequence.Sequence.reverse
   :noindex:

.. automethod:: abjad.tools.sequencetools.Sequence.Sequence.rotate
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.sequencetools.Sequence.Sequence.__add__
   :noindex:

.. automethod:: abjad.tools.sequencetools.Sequence.Sequence.__eq__
   :noindex:

.. automethod:: abjad.tools.sequencetools.Sequence.Sequence.__format__
   :noindex:

.. automethod:: abjad.tools.sequencetools.Sequence.Sequence.__getitem__
   :noindex:

.. automethod:: abjad.tools.sequencetools.Sequence.Sequence.__getslice__
   :noindex:

.. automethod:: abjad.tools.sequencetools.Sequence.Sequence.__hash__
   :noindex:

.. automethod:: abjad.tools.sequencetools.Sequence.Sequence.__len__
   :noindex:

.. automethod:: abjad.tools.sequencetools.Sequence.Sequence.__ne__
   :noindex:

.. automethod:: abjad.tools.sequencetools.Sequence.Sequence.__radd__
   :noindex:

.. automethod:: abjad.tools.sequencetools.Sequence.Sequence.__repr__
   :noindex:
