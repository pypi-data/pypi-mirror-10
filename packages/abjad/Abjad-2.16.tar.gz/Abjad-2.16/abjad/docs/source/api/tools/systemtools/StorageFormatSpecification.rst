systemtools.StorageFormatSpecification
======================================

.. autoclass:: abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification

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
           "systemtools.StorageFormatSpecification" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>StorageFormatSpecification</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "systemtools.StorageFormatSpecification";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.body_text
      ~abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.instance
      ~abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.is_bracketed
      ~abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.is_indented
      ~abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.keyword_argument_callables
      ~abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.keyword_argument_names
      ~abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.keywords_ignored_when_false
      ~abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.positional_argument_values
      ~abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.storage_format_pieces
      ~abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.tools_package_name
      ~abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.__eq__
      ~abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.__format__
      ~abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.__hash__
      ~abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.__ne__
      ~abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.body_text
   :noindex:

.. autoattribute:: abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.instance
   :noindex:

.. autoattribute:: abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.is_bracketed
   :noindex:

.. autoattribute:: abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.is_indented
   :noindex:

.. autoattribute:: abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.keyword_argument_callables
   :noindex:

.. autoattribute:: abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.keyword_argument_names
   :noindex:

.. autoattribute:: abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.keywords_ignored_when_false
   :noindex:

.. autoattribute:: abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.positional_argument_values
   :noindex:

.. autoattribute:: abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.storage_format_pieces
   :noindex:

.. autoattribute:: abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.tools_package_name
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.__eq__
   :noindex:

.. automethod:: abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.__format__
   :noindex:

.. automethod:: abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.__hash__
   :noindex:

.. automethod:: abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.__ne__
   :noindex:

.. automethod:: abjad.tools.systemtools.StorageFormatSpecification.StorageFormatSpecification.__repr__
   :noindex:
