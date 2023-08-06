indicatortools.StaffChange
==========================

.. autoclass:: abjad.tools.indicatortools.StaffChange.StaffChange

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
       subgraph cluster_indicatortools {
           graph [label=indicatortools];
           "indicatortools.StaffChange" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>StaffChange</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "indicatortools.StaffChange";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.indicatortools.StaffChange.StaffChange.staff
      ~abjad.tools.indicatortools.StaffChange.StaffChange.__copy__
      ~abjad.tools.indicatortools.StaffChange.StaffChange.__eq__
      ~abjad.tools.indicatortools.StaffChange.StaffChange.__format__
      ~abjad.tools.indicatortools.StaffChange.StaffChange.__hash__
      ~abjad.tools.indicatortools.StaffChange.StaffChange.__ne__
      ~abjad.tools.indicatortools.StaffChange.StaffChange.__repr__
      ~abjad.tools.indicatortools.StaffChange.StaffChange.__str__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.indicatortools.StaffChange.StaffChange.staff
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.indicatortools.StaffChange.StaffChange.__copy__
   :noindex:

.. automethod:: abjad.tools.indicatortools.StaffChange.StaffChange.__eq__
   :noindex:

.. automethod:: abjad.tools.indicatortools.StaffChange.StaffChange.__format__
   :noindex:

.. automethod:: abjad.tools.indicatortools.StaffChange.StaffChange.__hash__
   :noindex:

.. automethod:: abjad.tools.indicatortools.StaffChange.StaffChange.__ne__
   :noindex:

.. automethod:: abjad.tools.indicatortools.StaffChange.StaffChange.__repr__
   :noindex:

.. automethod:: abjad.tools.indicatortools.StaffChange.StaffChange.__str__
   :noindex:
