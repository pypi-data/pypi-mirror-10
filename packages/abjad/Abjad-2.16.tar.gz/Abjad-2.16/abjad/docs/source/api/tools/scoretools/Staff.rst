scoretools.Staff
================

.. autoclass:: abjad.tools.scoretools.Staff.Staff

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
       subgraph cluster_scoretools {
           graph [label=scoretools];
           "scoretools.Component" [color=3,
               group=2,
               label=Component,
               shape=oval,
               style=bold];
           "scoretools.Container" [color=3,
               group=2,
               label=Container,
               shape=box];
           "scoretools.Context" [color=3,
               group=2,
               label=Context,
               shape=box];
           "scoretools.Staff" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Staff</B>>,
               shape=box,
               style="filled, rounded"];
           "scoretools.Component" -> "scoretools.Container";
           "scoretools.Container" -> "scoretools.Context";
           "scoretools.Context" -> "scoretools.Staff";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "scoretools.Component";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.scoretools.Staff.Staff.append
      ~abjad.tools.scoretools.Staff.Staff.consists_commands
      ~abjad.tools.scoretools.Staff.Staff.context_name
      ~abjad.tools.scoretools.Staff.Staff.extend
      ~abjad.tools.scoretools.Staff.Staff.index
      ~abjad.tools.scoretools.Staff.Staff.insert
      ~abjad.tools.scoretools.Staff.Staff.is_nonsemantic
      ~abjad.tools.scoretools.Staff.Staff.is_semantic
      ~abjad.tools.scoretools.Staff.Staff.is_simultaneous
      ~abjad.tools.scoretools.Staff.Staff.name
      ~abjad.tools.scoretools.Staff.Staff.pop
      ~abjad.tools.scoretools.Staff.Staff.remove
      ~abjad.tools.scoretools.Staff.Staff.remove_commands
      ~abjad.tools.scoretools.Staff.Staff.reverse
      ~abjad.tools.scoretools.Staff.Staff.select_leaves
      ~abjad.tools.scoretools.Staff.Staff.__contains__
      ~abjad.tools.scoretools.Staff.Staff.__copy__
      ~abjad.tools.scoretools.Staff.Staff.__delitem__
      ~abjad.tools.scoretools.Staff.Staff.__eq__
      ~abjad.tools.scoretools.Staff.Staff.__format__
      ~abjad.tools.scoretools.Staff.Staff.__getitem__
      ~abjad.tools.scoretools.Staff.Staff.__graph__
      ~abjad.tools.scoretools.Staff.Staff.__hash__
      ~abjad.tools.scoretools.Staff.Staff.__illustrate__
      ~abjad.tools.scoretools.Staff.Staff.__len__
      ~abjad.tools.scoretools.Staff.Staff.__mul__
      ~abjad.tools.scoretools.Staff.Staff.__ne__
      ~abjad.tools.scoretools.Staff.Staff.__repr__
      ~abjad.tools.scoretools.Staff.Staff.__rmul__
      ~abjad.tools.scoretools.Staff.Staff.__setitem__

Bases
-----

- :py:class:`scoretools.Context <abjad.tools.scoretools.Context.Context>`

- :py:class:`scoretools.Container <abjad.tools.scoretools.Container.Container>`

- :py:class:`scoretools.Component <abjad.tools.scoretools.Component.Component>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.scoretools.Staff.Staff.consists_commands
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Staff.Staff.is_semantic
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Staff.Staff.remove_commands
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.scoretools.Staff.Staff.context_name
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Staff.Staff.is_nonsemantic
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Staff.Staff.is_simultaneous
   :noindex:

.. autoattribute:: abjad.tools.scoretools.Staff.Staff.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.scoretools.Staff.Staff.append
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.extend
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.index
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.insert
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.pop
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.remove
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.reverse
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.select_leaves
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.scoretools.Staff.Staff.__contains__
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.__copy__
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.__delitem__
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.__eq__
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.__format__
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.__getitem__
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.__graph__
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.__hash__
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.__illustrate__
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.__len__
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.__mul__
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.__ne__
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.__repr__
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.__rmul__
   :noindex:

.. automethod:: abjad.tools.scoretools.Staff.Staff.__setitem__
   :noindex:
