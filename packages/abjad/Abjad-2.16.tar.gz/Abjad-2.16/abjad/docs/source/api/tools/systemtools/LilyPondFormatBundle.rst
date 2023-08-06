systemtools.LilyPondFormatBundle
================================

.. autoclass:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle

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
       subgraph cluster_systemtools {
           graph [label=systemtools];
           "systemtools.LilyPondFormatBundle" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>LilyPondFormatBundle</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "systemtools.LilyPondFormatBundle";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.after
      ~abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.alphabetize
      ~abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.before
      ~abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.closing
      ~abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.context_settings
      ~abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.get
      ~abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.grob_overrides
      ~abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.grob_reverts
      ~abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.make_immutable
      ~abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.opening
      ~abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.right
      ~abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.update
      ~abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.__eq__
      ~abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.__format__
      ~abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.__hash__
      ~abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.__ne__
      ~abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.after
   :noindex:

.. autoattribute:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.before
   :noindex:

.. autoattribute:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.closing
   :noindex:

.. autoattribute:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.context_settings
   :noindex:

.. autoattribute:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.grob_overrides
   :noindex:

.. autoattribute:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.grob_reverts
   :noindex:

.. autoattribute:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.opening
   :noindex:

.. autoattribute:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.right
   :noindex:

Methods
-------

.. automethod:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.alphabetize
   :noindex:

.. automethod:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.get
   :noindex:

.. automethod:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.make_immutable
   :noindex:

.. automethod:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.update
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.__eq__
   :noindex:

.. automethod:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.__format__
   :noindex:

.. automethod:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.__hash__
   :noindex:

.. automethod:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.__ne__
   :noindex:

.. automethod:: abjad.tools.systemtools.LilyPondFormatBundle.LilyPondFormatBundle.__repr__
   :noindex:
