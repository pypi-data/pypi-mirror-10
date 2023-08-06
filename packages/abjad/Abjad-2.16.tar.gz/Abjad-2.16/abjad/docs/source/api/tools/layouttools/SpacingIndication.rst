layouttools.SpacingIndication
=============================

.. autoclass:: abjad.tools.layouttools.SpacingIndication.SpacingIndication

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
       subgraph cluster_layouttools {
           graph [label=layouttools];
           "layouttools.SpacingIndication" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>SpacingIndication</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "layouttools.SpacingIndication";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.layouttools.SpacingIndication.SpacingIndication.normalized_spacing_duration
      ~abjad.tools.layouttools.SpacingIndication.SpacingIndication.proportional_notation_duration
      ~abjad.tools.layouttools.SpacingIndication.SpacingIndication.tempo_indication
      ~abjad.tools.layouttools.SpacingIndication.SpacingIndication.__eq__
      ~abjad.tools.layouttools.SpacingIndication.SpacingIndication.__format__
      ~abjad.tools.layouttools.SpacingIndication.SpacingIndication.__hash__
      ~abjad.tools.layouttools.SpacingIndication.SpacingIndication.__ne__
      ~abjad.tools.layouttools.SpacingIndication.SpacingIndication.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.layouttools.SpacingIndication.SpacingIndication.normalized_spacing_duration
   :noindex:

.. autoattribute:: abjad.tools.layouttools.SpacingIndication.SpacingIndication.proportional_notation_duration
   :noindex:

.. autoattribute:: abjad.tools.layouttools.SpacingIndication.SpacingIndication.tempo_indication
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.layouttools.SpacingIndication.SpacingIndication.__eq__
   :noindex:

.. automethod:: abjad.tools.layouttools.SpacingIndication.SpacingIndication.__format__
   :noindex:

.. automethod:: abjad.tools.layouttools.SpacingIndication.SpacingIndication.__hash__
   :noindex:

.. automethod:: abjad.tools.layouttools.SpacingIndication.SpacingIndication.__ne__
   :noindex:

.. automethod:: abjad.tools.layouttools.SpacingIndication.SpacingIndication.__repr__
   :noindex:
