lilypondnametools.LilyPondContextSetting
========================================

.. autoclass:: abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting

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
           "lilypondnametools.LilyPondContextSetting" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>LilyPondContextSetting</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "lilypondnametools.LilyPondContextSetting";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.context_name
      ~abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.context_property
      ~abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.format_pieces
      ~abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.is_unset
      ~abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.value
      ~abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.__eq__
      ~abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.__format__
      ~abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.__hash__
      ~abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.__ne__
      ~abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.context_name
   :noindex:

.. autoattribute:: abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.context_property
   :noindex:

.. autoattribute:: abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.format_pieces
   :noindex:

.. autoattribute:: abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.is_unset
   :noindex:

.. autoattribute:: abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.value
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.__eq__
   :noindex:

.. automethod:: abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.__format__
   :noindex:

.. automethod:: abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.__hash__
   :noindex:

.. automethod:: abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.__ne__
   :noindex:

.. automethod:: abjad.tools.lilypondnametools.LilyPondContextSetting.LilyPondContextSetting.__repr__
   :noindex:
