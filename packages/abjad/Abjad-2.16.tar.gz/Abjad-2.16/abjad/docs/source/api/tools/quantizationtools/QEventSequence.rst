quantizationtools.QEventSequence
================================

.. autoclass:: abjad.tools.quantizationtools.QEventSequence.QEventSequence

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
       subgraph cluster_quantizationtools {
           graph [label=quantizationtools];
           "quantizationtools.QEventSequence" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>QEventSequence</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.QEventSequence";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.QEventSequence.QEventSequence.duration_in_ms
      ~abjad.tools.quantizationtools.QEventSequence.QEventSequence.from_millisecond_durations
      ~abjad.tools.quantizationtools.QEventSequence.QEventSequence.from_millisecond_offsets
      ~abjad.tools.quantizationtools.QEventSequence.QEventSequence.from_millisecond_pitch_pairs
      ~abjad.tools.quantizationtools.QEventSequence.QEventSequence.from_tempo_scaled_durations
      ~abjad.tools.quantizationtools.QEventSequence.QEventSequence.from_tempo_scaled_leaves
      ~abjad.tools.quantizationtools.QEventSequence.QEventSequence.sequence
      ~abjad.tools.quantizationtools.QEventSequence.QEventSequence.__contains__
      ~abjad.tools.quantizationtools.QEventSequence.QEventSequence.__eq__
      ~abjad.tools.quantizationtools.QEventSequence.QEventSequence.__format__
      ~abjad.tools.quantizationtools.QEventSequence.QEventSequence.__getitem__
      ~abjad.tools.quantizationtools.QEventSequence.QEventSequence.__hash__
      ~abjad.tools.quantizationtools.QEventSequence.QEventSequence.__iter__
      ~abjad.tools.quantizationtools.QEventSequence.QEventSequence.__len__
      ~abjad.tools.quantizationtools.QEventSequence.QEventSequence.__ne__
      ~abjad.tools.quantizationtools.QEventSequence.QEventSequence.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.QEventSequence.QEventSequence.duration_in_ms
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.QEventSequence.QEventSequence.sequence
   :noindex:

Class methods
-------------

.. automethod:: abjad.tools.quantizationtools.QEventSequence.QEventSequence.from_millisecond_durations
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEventSequence.QEventSequence.from_millisecond_offsets
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEventSequence.QEventSequence.from_millisecond_pitch_pairs
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEventSequence.QEventSequence.from_tempo_scaled_durations
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEventSequence.QEventSequence.from_tempo_scaled_leaves
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.QEventSequence.QEventSequence.__contains__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEventSequence.QEventSequence.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEventSequence.QEventSequence.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEventSequence.QEventSequence.__getitem__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEventSequence.QEventSequence.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEventSequence.QEventSequence.__iter__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEventSequence.QEventSequence.__len__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEventSequence.QEventSequence.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.QEventSequence.QEventSequence.__repr__
   :noindex:
