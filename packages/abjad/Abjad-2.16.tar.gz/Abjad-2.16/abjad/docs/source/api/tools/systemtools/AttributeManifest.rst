systemtools.AttributeManifest
=============================

.. autoclass:: abjad.tools.systemtools.AttributeManifest.AttributeManifest

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
           "systemtools.AttributeManifest" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>AttributeManifest</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "systemtools.AttributeManifest";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.systemtools.AttributeManifest.AttributeManifest.attribute_details
      ~abjad.tools.systemtools.AttributeManifest.AttributeManifest.__eq__
      ~abjad.tools.systemtools.AttributeManifest.AttributeManifest.__format__
      ~abjad.tools.systemtools.AttributeManifest.AttributeManifest.__getitem__
      ~abjad.tools.systemtools.AttributeManifest.AttributeManifest.__hash__
      ~abjad.tools.systemtools.AttributeManifest.AttributeManifest.__ne__
      ~abjad.tools.systemtools.AttributeManifest.AttributeManifest.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.systemtools.AttributeManifest.AttributeManifest.attribute_details
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.systemtools.AttributeManifest.AttributeManifest.__eq__
   :noindex:

.. automethod:: abjad.tools.systemtools.AttributeManifest.AttributeManifest.__format__
   :noindex:

.. automethod:: abjad.tools.systemtools.AttributeManifest.AttributeManifest.__getitem__
   :noindex:

.. automethod:: abjad.tools.systemtools.AttributeManifest.AttributeManifest.__hash__
   :noindex:

.. automethod:: abjad.tools.systemtools.AttributeManifest.AttributeManifest.__ne__
   :noindex:

.. automethod:: abjad.tools.systemtools.AttributeManifest.AttributeManifest.__repr__
   :noindex:
