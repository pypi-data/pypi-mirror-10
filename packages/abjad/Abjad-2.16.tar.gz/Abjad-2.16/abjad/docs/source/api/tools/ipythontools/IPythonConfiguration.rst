ipythontools.IPythonConfiguration
=================================

.. autoclass:: abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration

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
       subgraph cluster_ipythontools {
           graph [label=ipythontools];
           "ipythontools.IPythonConfiguration" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>IPythonConfiguration</B>>,
               shape=box,
               style="filled, rounded"];
       }
       subgraph cluster_systemtools {
           graph [label=systemtools];
           "systemtools.Configuration" [color=4,
               group=3,
               label=Configuration,
               shape=oval,
               style=bold];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "systemtools.Configuration";
       "systemtools.Configuration" -> "ipythontools.IPythonConfiguration";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.configuration_directory
      ~abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.configuration_file_name
      ~abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.configuration_file_path
      ~abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.home_directory
      ~abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__delitem__
      ~abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__eq__
      ~abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__format__
      ~abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__getitem__
      ~abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__hash__
      ~abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__iter__
      ~abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__len__
      ~abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__ne__
      ~abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__repr__
      ~abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__setitem__

Bases
-----

- :py:class:`systemtools.Configuration <abjad.tools.systemtools.Configuration.Configuration>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.configuration_directory
   :noindex:

.. autoattribute:: abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.configuration_file_name
   :noindex:

.. autoattribute:: abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.configuration_file_path
   :noindex:

.. autoattribute:: abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.home_directory
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__delitem__
   :noindex:

.. automethod:: abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__eq__
   :noindex:

.. automethod:: abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__format__
   :noindex:

.. automethod:: abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__getitem__
   :noindex:

.. automethod:: abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__hash__
   :noindex:

.. automethod:: abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__iter__
   :noindex:

.. automethod:: abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__len__
   :noindex:

.. automethod:: abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__ne__
   :noindex:

.. automethod:: abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__repr__
   :noindex:

.. automethod:: abjad.tools.ipythontools.IPythonConfiguration.IPythonConfiguration.__setitem__
   :noindex:
