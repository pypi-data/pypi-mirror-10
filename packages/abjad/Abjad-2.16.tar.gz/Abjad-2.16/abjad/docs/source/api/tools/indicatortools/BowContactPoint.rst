indicatortools.BowContactPoint
==============================

.. autoclass:: abjad.tools.indicatortools.BowContactPoint.BowContactPoint

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
           "indicatortools.BowContactPoint" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>BowContactPoint</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "indicatortools.BowContactPoint";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.indicatortools.BowContactPoint.BowContactPoint.contact_point
      ~abjad.tools.indicatortools.BowContactPoint.BowContactPoint.markup
      ~abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__copy__
      ~abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__eq__
      ~abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__format__
      ~abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__ge__
      ~abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__gt__
      ~abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__hash__
      ~abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__le__
      ~abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__lt__
      ~abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__ne__
      ~abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__repr__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.indicatortools.BowContactPoint.BowContactPoint.contact_point
   :noindex:

.. autoattribute:: abjad.tools.indicatortools.BowContactPoint.BowContactPoint.markup
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__copy__
   :noindex:

.. automethod:: abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__eq__
   :noindex:

.. automethod:: abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__format__
   :noindex:

.. automethod:: abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__ge__
   :noindex:

.. automethod:: abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__gt__
   :noindex:

.. automethod:: abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__hash__
   :noindex:

.. automethod:: abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__le__
   :noindex:

.. automethod:: abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__lt__
   :noindex:

.. automethod:: abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__ne__
   :noindex:

.. automethod:: abjad.tools.indicatortools.BowContactPoint.BowContactPoint.__repr__
   :noindex:
