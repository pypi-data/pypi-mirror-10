pitchtools.Accidental
=====================

.. autoclass:: abjad.tools.pitchtools.Accidental.Accidental

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
       subgraph cluster_pitchtools {
           graph [label=pitchtools];
           "pitchtools.Accidental" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Accidental</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "pitchtools.Accidental";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.Accidental.Accidental.abbreviation
      ~abjad.tools.pitchtools.Accidental.Accidental.is_abbreviation
      ~abjad.tools.pitchtools.Accidental.Accidental.is_adjusted
      ~abjad.tools.pitchtools.Accidental.Accidental.is_symbolic_string
      ~abjad.tools.pitchtools.Accidental.Accidental.name
      ~abjad.tools.pitchtools.Accidental.Accidental.semitones
      ~abjad.tools.pitchtools.Accidental.Accidental.symbolic_string
      ~abjad.tools.pitchtools.Accidental.Accidental.__add__
      ~abjad.tools.pitchtools.Accidental.Accidental.__eq__
      ~abjad.tools.pitchtools.Accidental.Accidental.__format__
      ~abjad.tools.pitchtools.Accidental.Accidental.__ge__
      ~abjad.tools.pitchtools.Accidental.Accidental.__gt__
      ~abjad.tools.pitchtools.Accidental.Accidental.__hash__
      ~abjad.tools.pitchtools.Accidental.Accidental.__le__
      ~abjad.tools.pitchtools.Accidental.Accidental.__lt__
      ~abjad.tools.pitchtools.Accidental.Accidental.__ne__
      ~abjad.tools.pitchtools.Accidental.Accidental.__neg__
      ~abjad.tools.pitchtools.Accidental.Accidental.__nonzero__
      ~abjad.tools.pitchtools.Accidental.Accidental.__repr__
      ~abjad.tools.pitchtools.Accidental.Accidental.__str__
      ~abjad.tools.pitchtools.Accidental.Accidental.__sub__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.Accidental.Accidental.abbreviation
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Accidental.Accidental.is_adjusted
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Accidental.Accidental.name
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Accidental.Accidental.semitones
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Accidental.Accidental.symbolic_string
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.pitchtools.Accidental.Accidental.is_abbreviation
   :noindex:

.. automethod:: abjad.tools.pitchtools.Accidental.Accidental.is_symbolic_string
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.Accidental.Accidental.__add__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Accidental.Accidental.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Accidental.Accidental.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Accidental.Accidental.__ge__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Accidental.Accidental.__gt__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Accidental.Accidental.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Accidental.Accidental.__le__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Accidental.Accidental.__lt__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Accidental.Accidental.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Accidental.Accidental.__neg__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Accidental.Accidental.__nonzero__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Accidental.Accidental.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Accidental.Accidental.__str__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Accidental.Accidental.__sub__
   :noindex:
