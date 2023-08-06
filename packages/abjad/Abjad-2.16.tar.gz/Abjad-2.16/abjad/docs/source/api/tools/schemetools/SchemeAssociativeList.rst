schemetools.SchemeAssociativeList
=================================

.. autoclass:: abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList

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
           "schemetools.Scheme" [color=3,
               group=2,
               label=Scheme,
               shape=box];
           "schemetools.SchemeAssociativeList" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>SchemeAssociativeList</B>>,
               shape=box,
               style="filled, rounded"];
           "schemetools.Scheme" -> "schemetools.SchemeAssociativeList";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "schemetools.Scheme";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.force_quotes
      ~abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.format_embedded_scheme_value
      ~abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.format_scheme_value
      ~abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.quoting
      ~abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.verbatim
      ~abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.__copy__
      ~abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.__eq__
      ~abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.__format__
      ~abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.__hash__
      ~abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.__ne__
      ~abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.__repr__
      ~abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.__str__

Bases
-----

- :py:class:`schemetools.Scheme <abjad.tools.schemetools.Scheme.Scheme>`

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.force_quotes
   :noindex:

.. autoattribute:: abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.quoting
   :noindex:

.. autoattribute:: abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.verbatim
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.format_embedded_scheme_value
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.format_scheme_value
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.__copy__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.__eq__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.__format__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.__hash__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.__ne__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.__repr__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeAssociativeList.SchemeAssociativeList.__str__
   :noindex:
