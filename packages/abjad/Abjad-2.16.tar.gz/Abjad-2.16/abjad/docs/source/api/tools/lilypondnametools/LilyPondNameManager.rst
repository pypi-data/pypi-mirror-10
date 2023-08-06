lilypondnametools.LilyPondNameManager
=====================================

.. autoclass:: abjad.tools.lilypondnametools.LilyPondNameManager.LilyPondNameManager

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
           "lilypondnametools.LilyPondGrobNameManager" [color=3,
               group=2,
               label=LilyPondGrobNameManager,
               shape=box];
           "lilypondnametools.LilyPondNameManager" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>LilyPondNameManager</B>>,
               shape=box,
               style="filled, rounded"];
           "lilypondnametools.LilyPondSettingNameManager" [color=3,
               group=2,
               label=LilyPondSettingNameManager,
               shape=box];
           "lilypondnametools.LilyPondNameManager" -> "lilypondnametools.LilyPondGrobNameManager";
           "lilypondnametools.LilyPondNameManager" -> "lilypondnametools.LilyPondSettingNameManager";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "lilypondnametools.LilyPondNameManager";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.lilypondnametools.LilyPondNameManager.LilyPondNameManager.__eq__
      ~abjad.tools.lilypondnametools.LilyPondNameManager.LilyPondNameManager.__format__
      ~abjad.tools.lilypondnametools.LilyPondNameManager.LilyPondNameManager.__hash__
      ~abjad.tools.lilypondnametools.LilyPondNameManager.LilyPondNameManager.__ne__
      ~abjad.tools.lilypondnametools.LilyPondNameManager.LilyPondNameManager.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.lilypondnametools.LilyPondNameManager.LilyPondNameManager.__eq__
   :noindex:

.. automethod:: abjad.tools.lilypondnametools.LilyPondNameManager.LilyPondNameManager.__format__
   :noindex:

.. automethod:: abjad.tools.lilypondnametools.LilyPondNameManager.LilyPondNameManager.__hash__
   :noindex:

.. automethod:: abjad.tools.lilypondnametools.LilyPondNameManager.LilyPondNameManager.__ne__
   :noindex:

.. automethod:: abjad.tools.lilypondnametools.LilyPondNameManager.LilyPondNameManager.__repr__
   :noindex:
