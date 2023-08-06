schemetools.SchemeVector
========================

.. autoclass:: abjad.tools.schemetools.SchemeVector.SchemeVector

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
           "schemetools.SchemeVector" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>SchemeVector</B>>,
               shape=box,
               style="filled, rounded"];
           "schemetools.Scheme" -> "schemetools.SchemeVector";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "schemetools.Scheme";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.schemetools.SchemeVector.SchemeVector.force_quotes
      ~abjad.tools.schemetools.SchemeVector.SchemeVector.format_embedded_scheme_value
      ~abjad.tools.schemetools.SchemeVector.SchemeVector.format_scheme_value
      ~abjad.tools.schemetools.SchemeVector.SchemeVector.quoting
      ~abjad.tools.schemetools.SchemeVector.SchemeVector.verbatim
      ~abjad.tools.schemetools.SchemeVector.SchemeVector.__copy__
      ~abjad.tools.schemetools.SchemeVector.SchemeVector.__eq__
      ~abjad.tools.schemetools.SchemeVector.SchemeVector.__format__
      ~abjad.tools.schemetools.SchemeVector.SchemeVector.__hash__
      ~abjad.tools.schemetools.SchemeVector.SchemeVector.__ne__
      ~abjad.tools.schemetools.SchemeVector.SchemeVector.__repr__
      ~abjad.tools.schemetools.SchemeVector.SchemeVector.__str__

Bases
-----

- :py:class:`schemetools.Scheme <abjad.tools.schemetools.Scheme.Scheme>`

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.schemetools.SchemeVector.SchemeVector.force_quotes
   :noindex:

.. autoattribute:: abjad.tools.schemetools.SchemeVector.SchemeVector.quoting
   :noindex:

.. autoattribute:: abjad.tools.schemetools.SchemeVector.SchemeVector.verbatim
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.schemetools.SchemeVector.SchemeVector.format_embedded_scheme_value
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeVector.SchemeVector.format_scheme_value
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.schemetools.SchemeVector.SchemeVector.__copy__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeVector.SchemeVector.__eq__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeVector.SchemeVector.__format__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeVector.SchemeVector.__hash__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeVector.SchemeVector.__ne__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeVector.SchemeVector.__repr__
   :noindex:

.. automethod:: abjad.tools.schemetools.SchemeVector.SchemeVector.__str__
   :noindex:
