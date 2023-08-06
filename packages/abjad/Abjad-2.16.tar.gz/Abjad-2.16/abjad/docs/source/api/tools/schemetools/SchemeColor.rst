schemetools.SchemeColor
=======================

.. autoclass:: abjad.tools.schemetools.SchemeColor.SchemeColor

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
           "schemetools.SchemeColor" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>SchemeColor</B>>,
               shape=box,
               style="filled, rounded"];
           "schemetools.Scheme" -> "schemetools.SchemeColor";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "schemetools.Scheme";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.schemetools.SchemeColor.SchemeColor.force_quotes
      ~abjad.tools.schemetools.SchemeColor.SchemeColor.format_embedded_scheme_value
      ~abjad.tools.schemetools.SchemeColor.SchemeColor.format_scheme_value
      ~abjad.tools.schemetools.SchemeColor.SchemeColor.quoting
      ~abjad.tools.schemetools.SchemeColor.SchemeColor.verbatim
      ~abjad.tools.schemetools.SchemeColor.SchemeColor.__copy__
      ~abjad.tools.schemetools.SchemeColor.SchemeColor.__eq__
      ~abjad.tools.schemetools.SchemeColor.SchemeColor.__format__
      ~abjad.tools.schemetools.SchemeColor.SchemeColor.__hash__
      ~abjad.tools.schemetools.SchemeColor.SchemeColor.__ne__
      ~abjad.tools.schemetools.SchemeColor.SchemeColor.__repr__
      ~abjad.tools.schemetools.SchemeColor.SchemeColor.__str__

Bases
-----

- :py:class:`schemetools.Scheme <abjad.tools.schemetools.Scheme.Scheme>`

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.schemetools.SchemeColor.SchemeColor.force_quotes
   :noindex:

.. autoattribute:: abjad.tools.schemetools.SchemeColor.SchemeColor.quoting
   :noindex:

.. autoattribute:: abjad.tools.schemetools.SchemeColor.SchemeColor.verbatim
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.schemetools.SchemeColor.SchemeColor.format_embedded_scheme_value
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeColor.SchemeColor.format_scheme_value
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.schemetools.SchemeColor.SchemeColor.__copy__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeColor.SchemeColor.__eq__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeColor.SchemeColor.__format__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeColor.SchemeColor.__hash__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeColor.SchemeColor.__ne__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeColor.SchemeColor.__repr__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeColor.SchemeColor.__str__
   :noindex:
