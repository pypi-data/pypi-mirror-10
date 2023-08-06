abjadbooktools.AbjadBookProcessor
=================================

.. autoclass:: abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor

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
       subgraph cluster_abjadbooktools {
           graph [label=abjadbooktools];
           "abjadbooktools.AbjadBookProcessor" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>AbjadBookProcessor</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "abjadbooktools.AbjadBookProcessor";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.directory
      ~abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.image_prefix
      ~abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.lines
      ~abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.output_format
      ~abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.skip_rendering
      ~abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.update_status
      ~abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.verbose
      ~abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.__call__
      ~abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.__eq__
      ~abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.__format__
      ~abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.__hash__
      ~abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.__ne__
      ~abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.directory
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.image_prefix
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.lines
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.output_format
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.skip_rendering
   :noindex:

.. autoattribute:: abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.verbose
   :noindex:

Methods
-------

.. automethod:: abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.update_status
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.__call__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.__eq__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.__format__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.__hash__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.__ne__
   :noindex:

.. automethod:: abjad.tools.abjadbooktools.AbjadBookProcessor.AbjadBookProcessor.__repr__
   :noindex:
