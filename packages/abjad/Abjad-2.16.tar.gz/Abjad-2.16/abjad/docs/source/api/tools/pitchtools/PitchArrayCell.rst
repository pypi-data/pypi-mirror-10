pitchtools.PitchArrayCell
=========================

.. autoclass:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell

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
           "pitchtools.PitchArrayCell" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>PitchArrayCell</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "pitchtools.PitchArrayCell";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.column_indices
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.indices
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.is_first_in_row
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.is_last_in_row
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.item
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.matches_cell
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.next
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.parent_array
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.parent_column
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.parent_row
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.pitches
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.previous
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.row_index
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.weight
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.width
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.__eq__
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.__format__
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.__hash__
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.__ne__
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.__repr__
      ~abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.__str__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.column_indices
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.indices
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.is_first_in_row
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.is_last_in_row
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.item
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.next
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.parent_array
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.parent_column
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.parent_row
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.previous
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.row_index
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.weight
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.width
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.pitches
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.matches_cell
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayCell.PitchArrayCell.__str__
   :noindex:
