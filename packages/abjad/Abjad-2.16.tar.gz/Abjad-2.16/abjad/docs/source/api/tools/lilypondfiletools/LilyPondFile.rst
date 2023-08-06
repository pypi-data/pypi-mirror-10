lilypondfiletools.LilyPondFile
==============================

.. autoclass:: abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile

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
       subgraph cluster_lilypondfiletools {
           graph [label=lilypondfiletools];
           "lilypondfiletools.LilyPondFile" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>LilyPondFile</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "lilypondfiletools.LilyPondFile";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.default_paper_size
      ~abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.file_initial_system_comments
      ~abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.file_initial_system_includes
      ~abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.file_initial_user_comments
      ~abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.file_initial_user_includes
      ~abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.global_staff_size
      ~abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.items
      ~abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.use_relative_includes
      ~abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.__eq__
      ~abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.__format__
      ~abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.__getitem__
      ~abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.__hash__
      ~abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.__illustrate__
      ~abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.__ne__
      ~abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.file_initial_system_comments
   :noindex:

.. autoattribute:: abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.file_initial_system_includes
   :noindex:

.. autoattribute:: abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.file_initial_user_comments
   :noindex:

.. autoattribute:: abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.file_initial_user_includes
   :noindex:

.. autoattribute:: abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.items
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.default_paper_size
   :noindex:

.. autoattribute:: abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.global_staff_size
   :noindex:

.. autoattribute:: abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.use_relative_includes
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.__eq__
   :noindex:

.. automethod:: abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.__format__
   :noindex:

.. automethod:: abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.__getitem__
   :noindex:

.. automethod:: abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.__hash__
   :noindex:

.. automethod:: abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.__illustrate__
   :noindex:

.. automethod:: abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.__ne__
   :noindex:

.. automethod:: abjad.tools.lilypondfiletools.LilyPondFile.LilyPondFile.__repr__
   :noindex:
