lilypondnametools.LilyPondGrobOverride
======================================

.. autoclass:: abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride

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
       subgraph cluster_lilypondnametools {
           graph [label=lilypondnametools];
           "lilypondnametools.LilyPondGrobOverride" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>LilyPondGrobOverride</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "lilypondnametools.LilyPondGrobOverride";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.context_name
      ~abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.grob_name
      ~abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.is_once
      ~abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.is_revert
      ~abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.property_path
      ~abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.revert_format_pieces
      ~abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.value
      ~abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.__eq__
      ~abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.__format__
      ~abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.__hash__
      ~abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.__ne__
      ~abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.context_name
   :noindex:

.. autoattribute:: abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.grob_name
   :noindex:

.. autoattribute:: abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.is_once
   :noindex:

.. autoattribute:: abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.is_revert
   :noindex:

.. autoattribute:: abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.property_path
   :noindex:

.. autoattribute:: abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.revert_format_pieces
   :noindex:

.. autoattribute:: abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.value
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.__eq__
   :noindex:

.. automethod:: abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.__format__
   :noindex:

.. automethod:: abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.__hash__
   :noindex:

.. automethod:: abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.__ne__
   :noindex:

.. automethod:: abjad.tools.lilypondnametools.LilyPondGrobOverride.LilyPondGrobOverride.__repr__
   :noindex:
