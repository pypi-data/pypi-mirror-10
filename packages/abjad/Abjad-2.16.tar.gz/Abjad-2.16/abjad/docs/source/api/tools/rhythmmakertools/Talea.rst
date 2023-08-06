rhythmmakertools.Talea
======================

.. autoclass:: abjad.tools.rhythmmakertools.Talea.Talea

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
       subgraph cluster_rhythmmakertools {
           graph [label=rhythmmakertools];
           "rhythmmakertools.Talea" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Talea</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadValueObject" -> "rhythmmakertools.Talea";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmmakertools.Talea.Talea.counts
      ~abjad.tools.rhythmmakertools.Talea.Talea.denominator
      ~abjad.tools.rhythmmakertools.Talea.Talea.__copy__
      ~abjad.tools.rhythmmakertools.Talea.Talea.__eq__
      ~abjad.tools.rhythmmakertools.Talea.Talea.__format__
      ~abjad.tools.rhythmmakertools.Talea.Talea.__getitem__
      ~abjad.tools.rhythmmakertools.Talea.Talea.__hash__
      ~abjad.tools.rhythmmakertools.Talea.Talea.__iter__
      ~abjad.tools.rhythmmakertools.Talea.Talea.__len__
      ~abjad.tools.rhythmmakertools.Talea.Talea.__ne__
      ~abjad.tools.rhythmmakertools.Talea.Talea.__repr__

Bases
-----

- :py:class:`abctools.AbjadValueObject <abjad.tools.abctools.AbjadValueObject.AbjadValueObject>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmmakertools.Talea.Talea.counts
   :noindex:

.. autoattribute:: abjad.tools.rhythmmakertools.Talea.Talea.denominator
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmmakertools.Talea.Talea.__copy__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.Talea.Talea.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.Talea.Talea.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.Talea.Talea.__getitem__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.Talea.Talea.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.Talea.Talea.__iter__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.Talea.Talea.__len__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.Talea.Talea.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmmakertools.Talea.Talea.__repr__
   :noindex:
