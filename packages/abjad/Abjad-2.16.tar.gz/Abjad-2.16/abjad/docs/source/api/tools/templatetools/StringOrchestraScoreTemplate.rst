templatetools.StringOrchestraScoreTemplate
==========================================

.. autoclass:: abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate

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
           "abctools.AbjadValueObject" [color=2,
               group=1,
               label=AbjadValueObject,
               shape=box];
           "abctools.AbjadObject" -> "abctools.AbjadValueObject";
           "abctools.AbjadObject.AbstractBase" -> "abctools.AbjadObject";
       }
       subgraph cluster_templatetools {
           graph [label=templatetools];
           "templatetools.StringOrchestraScoreTemplate" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>StringOrchestraScoreTemplate</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "templatetools.StringOrchestraScoreTemplate";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.cello_count
      ~abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.context_name_abbreviations
      ~abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.contrabass_count
      ~abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.split_hands
      ~abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.use_percussion_clefs
      ~abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.viola_count
      ~abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.violin_count
      ~abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.__call__
      ~abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.__copy__
      ~abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.__eq__
      ~abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.__format__
      ~abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.__hash__
      ~abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.__ne__
      ~abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.__repr__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.cello_count
   :noindex:

.. autoattribute:: abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.context_name_abbreviations
   :noindex:

.. autoattribute:: abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.contrabass_count
   :noindex:

.. autoattribute:: abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.split_hands
   :noindex:

.. autoattribute:: abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.use_percussion_clefs
   :noindex:

.. autoattribute:: abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.viola_count
   :noindex:

.. autoattribute:: abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.violin_count
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.__call__
   :noindex:

.. automethod:: abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.__copy__
   :noindex:

.. automethod:: abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.__eq__
   :noindex:

.. automethod:: abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.__format__
   :noindex:

.. automethod:: abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.__hash__
   :noindex:

.. automethod:: abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.__ne__
   :noindex:

.. automethod:: abjad.tools.templatetools.StringOrchestraScoreTemplate.StringOrchestraScoreTemplate.__repr__
   :noindex:
