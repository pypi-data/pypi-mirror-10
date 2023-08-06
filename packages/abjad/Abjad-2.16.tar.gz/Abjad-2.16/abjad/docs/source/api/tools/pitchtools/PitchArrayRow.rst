pitchtools.PitchArrayRow
========================

.. autoclass:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow

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
       subgraph cluster_pitchtools {
           graph [label=pitchtools];
           "pitchtools.PitchArrayRow" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>PitchArrayRow</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "pitchtools.PitchArrayRow";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.append
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.apply_pitches
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.cell_tokens
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.cell_widths
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.cells
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.copy_subrow
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.depth
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.dimensions
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.empty_pitches
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.extend
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.has_spanning_cell_over_index
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.index
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.is_defective
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.is_in_range
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.merge
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.pad_to_width
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.parent_array
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.pitch_range
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.pitches
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.pop
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.remove
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.row_index
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.to_measure
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.weight
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.width
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.withdraw
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__add__
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__copy__
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__eq__
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__format__
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__getitem__
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__hash__
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__iadd__
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__len__
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__ne__
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__repr__
      ~abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__str__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.cell_tokens
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.cell_widths
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.cells
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.depth
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.dimensions
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.is_defective
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.is_in_range
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.parent_array
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.pitches
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.row_index
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.weight
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.width
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.pitch_range
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.append
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.apply_pitches
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.copy_subrow
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.empty_pitches
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.extend
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.has_spanning_cell_over_index
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.index
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.merge
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.pad_to_width
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.pop
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.remove
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.to_measure
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.withdraw
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__add__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__copy__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__getitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__iadd__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__len__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayRow.PitchArrayRow.__str__
   :noindex:
