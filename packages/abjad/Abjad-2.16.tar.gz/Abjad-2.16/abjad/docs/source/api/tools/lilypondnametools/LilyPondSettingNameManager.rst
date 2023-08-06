lilypondnametools.LilyPondSettingNameManager
============================================

.. autoclass:: abjad.tools.lilypondnametools.LilyPondSettingNameManager.LilyPondSettingNameManager

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
           "lilypondnametools.LilyPondNameManager" [color=3,
               group=2,
               label=LilyPondNameManager,
               shape=box];
           "lilypondnametools.LilyPondSettingNameManager" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>LilyPondSettingNameManager</B>>,
               shape=box,
               style="filled, rounded"];
           "lilypondnametools.LilyPondNameManager" -> "lilypondnametools.LilyPondSettingNameManager";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "lilypondnametools.LilyPondNameManager";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.lilypondnametools.LilyPondSettingNameManager.LilyPondSettingNameManager.__eq__
      ~abjad.tools.lilypondnametools.LilyPondSettingNameManager.LilyPondSettingNameManager.__format__
      ~abjad.tools.lilypondnametools.LilyPondSettingNameManager.LilyPondSettingNameManager.__getattr__
      ~abjad.tools.lilypondnametools.LilyPondSettingNameManager.LilyPondSettingNameManager.__hash__
      ~abjad.tools.lilypondnametools.LilyPondSettingNameManager.LilyPondSettingNameManager.__ne__
      ~abjad.tools.lilypondnametools.LilyPondSettingNameManager.LilyPondSettingNameManager.__repr__

Bases
-----

- :py:class:`lilypondnametools.LilyPondNameManager <abjad.tools.lilypondnametools.LilyPondNameManager.LilyPondNameManager>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.lilypondnametools.LilyPondSettingNameManager.LilyPondSettingNameManager.__eq__
   :noindex:

.. automethod:: abjad.tools.lilypondnametools.LilyPondSettingNameManager.LilyPondSettingNameManager.__format__
   :noindex:

.. automethod:: abjad.tools.lilypondnametools.LilyPondSettingNameManager.LilyPondSettingNameManager.__getattr__
   :noindex:

.. automethod:: abjad.tools.lilypondnametools.LilyPondSettingNameManager.LilyPondSettingNameManager.__hash__
   :noindex:

.. automethod:: abjad.tools.lilypondnametools.LilyPondSettingNameManager.LilyPondSettingNameManager.__ne__
   :noindex:

.. automethod:: abjad.tools.lilypondnametools.LilyPondSettingNameManager.LilyPondSettingNameManager.__repr__
   :noindex:
