schemetools.Scheme
==================

.. autoclass:: abjad.tools.schemetools.Scheme.Scheme

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
       subgraph cluster_schemetools {
           graph [label=schemetools];
           "schemetools.Scheme" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Scheme</B>>,
               shape=box,
               style="filled, rounded"];
           "schemetools.SchemeAssociativeList" [color=3,
               group=2,
               label=SchemeAssociativeList,
               shape=box];
           "schemetools.SchemeColor" [color=3,
               group=2,
               label=SchemeColor,
               shape=box];
           "schemetools.SchemeMoment" [color=3,
               group=2,
               label=SchemeMoment,
               shape=box];
           "schemetools.SchemePair" [color=3,
               group=2,
               label=SchemePair,
               shape=box];
           "schemetools.SchemeSymbol" [color=3,
               group=2,
               label=SchemeSymbol,
               shape=box];
           "schemetools.SchemeVector" [color=3,
               group=2,
               label=SchemeVector,
               shape=box];
           "schemetools.SchemeVectorConstant" [color=3,
               group=2,
               label=SchemeVectorConstant,
               shape=box];
           "schemetools.Scheme" -> "schemetools.SchemeAssociativeList";
           "schemetools.Scheme" -> "schemetools.SchemeColor";
           "schemetools.Scheme" -> "schemetools.SchemeMoment";
           "schemetools.Scheme" -> "schemetools.SchemePair";
           "schemetools.Scheme" -> "schemetools.SchemeSymbol";
           "schemetools.Scheme" -> "schemetools.SchemeVector";
           "schemetools.Scheme" -> "schemetools.SchemeVectorConstant";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "schemetools.Scheme";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.schemetools.Scheme.Scheme.force_quotes
      ~abjad.tools.schemetools.Scheme.Scheme.format_embedded_scheme_value
      ~abjad.tools.schemetools.Scheme.Scheme.format_scheme_value
      ~abjad.tools.schemetools.Scheme.Scheme.quoting
      ~abjad.tools.schemetools.Scheme.Scheme.verbatim
      ~abjad.tools.schemetools.Scheme.Scheme.__copy__
      ~abjad.tools.schemetools.Scheme.Scheme.__eq__
      ~abjad.tools.schemetools.Scheme.Scheme.__format__
      ~abjad.tools.schemetools.Scheme.Scheme.__hash__
      ~abjad.tools.schemetools.Scheme.Scheme.__ne__
      ~abjad.tools.schemetools.Scheme.Scheme.__repr__
      ~abjad.tools.schemetools.Scheme.Scheme.__str__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.schemetools.Scheme.Scheme.force_quotes
   :noindex:

.. autoattribute:: abjad.tools.schemetools.Scheme.Scheme.quoting
   :noindex:

.. autoattribute:: abjad.tools.schemetools.Scheme.Scheme.verbatim
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.schemetools.Scheme.Scheme.format_embedded_scheme_value
   :noindex:

.. automethod:: abjad.tools.schemetools.Scheme.Scheme.format_scheme_value
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.schemetools.Scheme.Scheme.__copy__
   :noindex:

.. automethod:: abjad.tools.schemetools.Scheme.Scheme.__eq__
   :noindex:

.. automethod:: abjad.tools.schemetools.Scheme.Scheme.__format__
   :noindex:

.. automethod:: abjad.tools.schemetools.Scheme.Scheme.__hash__
   :noindex:

.. automethod:: abjad.tools.schemetools.Scheme.Scheme.__ne__
   :noindex:

.. automethod:: abjad.tools.schemetools.Scheme.Scheme.__repr__
   :noindex:

.. automethod:: abjad.tools.schemetools.Scheme.Scheme.__str__
   :noindex:
