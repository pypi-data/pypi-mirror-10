pitchtools.PitchArrayColumn
===========================

.. autoclass:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn

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
           "pitchtools.PitchArrayColumn" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>PitchArrayColumn</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "pitchtools.PitchArrayColumn";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.append
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.cell_tokens
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.cell_widths
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.cells
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.column_index
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.depth
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.dimensions
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.extend
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.has_voice_crossing
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.is_defective
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.parent_array
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.pitches
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.remove_pitches
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.start_cells
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.start_pitches
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.stop_cells
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.stop_pitches
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.weight
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.width
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.__eq__
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.__format__
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.__getitem__
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.__hash__
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.__ne__
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.__repr__
      ~abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.__str__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.cell_tokens
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.cell_widths
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.cells
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.column_index
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.depth
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.dimensions
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.has_voice_crossing
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.is_defective
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.parent_array
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.pitches
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.start_cells
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.start_pitches
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.stop_cells
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.stop_pitches
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.weight
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.width
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.append
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.extend
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.remove_pitches
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.__getitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.PitchArrayColumn.PitchArrayColumn.__str__
   :noindex:
