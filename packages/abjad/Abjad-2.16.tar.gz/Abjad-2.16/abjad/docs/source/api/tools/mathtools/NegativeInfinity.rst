mathtools.NegativeInfinity
==========================

.. autoclass:: abjad.tools.mathtools.NegativeInfinity.NegativeInfinity

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
       subgraph cluster_mathtools {
           graph [label=mathtools];
           "mathtools.Infinity" [color=3,
               group=2,
               label=Infinity,
               shape=box];
           "mathtools.NegativeInfinity" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>NegativeInfinity</B>>,
               shape=box,
               style="filled, rounded"];
           "mathtools.Infinity" -> "mathtools.NegativeInfinity";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "mathtools.Infinity";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__eq__
      ~abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__format__
      ~abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__ge__
      ~abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__gt__
      ~abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__hash__
      ~abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__le__
      ~abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__lt__
      ~abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__ne__
      ~abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__repr__
      ~abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__sub__

Bases
-----

- :py:class:`mathtools.Infinity <abjad.tools.mathtools.Infinity.Infinity>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Special methods
---------------

.. automethod:: abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__eq__
   :noindex:

.. automethod:: abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__format__
   :noindex:

.. automethod:: abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__ge__
   :noindex:

.. automethod:: abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__gt__
   :noindex:

.. automethod:: abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__hash__
   :noindex:

.. automethod:: abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__le__
   :noindex:

.. automethod:: abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__lt__
   :noindex:

.. automethod:: abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__ne__
   :noindex:

.. automethod:: abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__repr__
   :noindex:

.. automethod:: abjad.tools.mathtools.NegativeInfinity.NegativeInfinity.__sub__
   :noindex:
