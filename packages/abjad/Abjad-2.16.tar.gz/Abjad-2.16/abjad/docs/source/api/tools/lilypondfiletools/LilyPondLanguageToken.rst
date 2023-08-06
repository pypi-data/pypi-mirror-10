lilypondfiletools.LilyPondLanguageToken
=======================================

.. autoclass:: abjad.tools.lilypondfiletools.LilyPondLanguageToken.LilyPondLanguageToken

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
       subgraph cluster_lilypondfiletools {
           graph [label=lilypondfiletools];
           "lilypondfiletools.LilyPondLanguageToken" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>LilyPondLanguageToken</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "lilypondfiletools.LilyPondLanguageToken";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.lilypondfiletools.LilyPondLanguageToken.LilyPondLanguageToken.__eq__
      ~abjad.tools.lilypondfiletools.LilyPondLanguageToken.LilyPondLanguageToken.__format__
      ~abjad.tools.lilypondfiletools.LilyPondLanguageToken.LilyPondLanguageToken.__hash__
      ~abjad.tools.lilypondfiletools.LilyPondLanguageToken.LilyPondLanguageToken.__ne__
      ~abjad.tools.lilypondfiletools.LilyPondLanguageToken.LilyPondLanguageToken.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.lilypondfiletools.LilyPondLanguageToken.LilyPondLanguageToken.__eq__
   :noindex:

.. automethod:: abjad.tools.lilypondfiletools.LilyPondLanguageToken.LilyPondLanguageToken.__format__
   :noindex:

.. automethod:: abjad.tools.lilypondfiletools.LilyPondLanguageToken.LilyPondLanguageToken.__hash__
   :noindex:

.. automethod:: abjad.tools.lilypondfiletools.LilyPondLanguageToken.LilyPondLanguageToken.__ne__
   :noindex:

.. automethod:: abjad.tools.lilypondfiletools.LilyPondLanguageToken.LilyPondLanguageToken.__repr__
   :noindex:
