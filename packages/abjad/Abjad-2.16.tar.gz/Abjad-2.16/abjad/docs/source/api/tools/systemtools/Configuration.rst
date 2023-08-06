systemtools.Configuration
=========================

.. autoclass:: abjad.tools.systemtools.Configuration.Configuration

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
           "ipythontools.IPythonConfiguration" [color=4,
               group=3,
               label=IPythonConfiguration,
               shape=box];
       }
       subgraph cluster_systemtools {
           graph [label=systemtools];
           "systemtools.AbjadConfiguration" [color=5,
               group=4,
               label=AbjadConfiguration,
               shape=box];
           "systemtools.Configuration" [color=black,
               fontcolor=white,
               group=4,
               label=<<B>Configuration</B>>,
               shape=oval,
               style="filled, rounded"];
           "systemtools.Configuration" -> "systemtools.AbjadConfiguration";
       }
       subgraph cluster_ide {
           graph [label=ide];
           "ide.idetools.Configuration" [color=3,
               group=2,
               label=Configuration,
               shape=box];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "systemtools.Configuration";
       "systemtools.AbjadConfiguration" -> "ide.idetools.Configuration";
       "systemtools.Configuration" -> "ipythontools.IPythonConfiguration";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.systemtools.Configuration.Configuration.configuration_directory
      ~abjad.tools.systemtools.Configuration.Configuration.configuration_file_name
      ~abjad.tools.systemtools.Configuration.Configuration.configuration_file_path
      ~abjad.tools.systemtools.Configuration.Configuration.home_directory
      ~abjad.tools.systemtools.Configuration.Configuration.__delitem__
      ~abjad.tools.systemtools.Configuration.Configuration.__eq__
      ~abjad.tools.systemtools.Configuration.Configuration.__format__
      ~abjad.tools.systemtools.Configuration.Configuration.__getitem__
      ~abjad.tools.systemtools.Configuration.Configuration.__hash__
      ~abjad.tools.systemtools.Configuration.Configuration.__iter__
      ~abjad.tools.systemtools.Configuration.Configuration.__len__
      ~abjad.tools.systemtools.Configuration.Configuration.__ne__
      ~abjad.tools.systemtools.Configuration.Configuration.__repr__
      ~abjad.tools.systemtools.Configuration.Configuration.__setitem__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.systemtools.Configuration.Configuration.configuration_directory
   :noindex:

.. autoattribute:: abjad.tools.systemtools.Configuration.Configuration.configuration_file_name
   :noindex:

.. autoattribute:: abjad.tools.systemtools.Configuration.Configuration.configuration_file_path
   :noindex:

.. autoattribute:: abjad.tools.systemtools.Configuration.Configuration.home_directory
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.systemtools.Configuration.Configuration.__delitem__
   :noindex:

.. automethod:: abjad.tools.systemtools.Configuration.Configuration.__eq__
   :noindex:

.. automethod:: abjad.tools.systemtools.Configuration.Configuration.__format__
   :noindex:

.. automethod:: abjad.tools.systemtools.Configuration.Configuration.__getitem__
   :noindex:

.. automethod:: abjad.tools.systemtools.Configuration.Configuration.__hash__
   :noindex:

.. automethod:: abjad.tools.systemtools.Configuration.Configuration.__iter__
   :noindex:

.. automethod:: abjad.tools.systemtools.Configuration.Configuration.__len__
   :noindex:

.. automethod:: abjad.tools.systemtools.Configuration.Configuration.__ne__
   :noindex:

.. automethod:: abjad.tools.systemtools.Configuration.Configuration.__repr__
   :noindex:

.. automethod:: abjad.tools.systemtools.Configuration.Configuration.__setitem__
   :noindex:
