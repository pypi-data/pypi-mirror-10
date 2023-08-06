lilypondparsertools.GuileProxy
==============================

.. autoclass:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy

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
       subgraph cluster_lilypondparsertools {
           graph [label=lilypondparsertools];
           "lilypondparsertools.GuileProxy" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>GuileProxy</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "lilypondparsertools.GuileProxy";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.acciaccatura
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.appoggiatura
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.bar
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.breathe
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.clef
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.grace
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.key
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.language
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.makeClusters
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.mark
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.one_voice
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.relative
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.skip
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.slashed_grace_container
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.time
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.times
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.transpose
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.voiceFour
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.voiceOne
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.voiceThree
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.voiceTwo
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.__call__
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.__eq__
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.__format__
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.__hash__
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.__ne__
      ~abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Methods
-------

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.acciaccatura
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.appoggiatura
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.bar
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.breathe
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.clef
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.grace
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.key
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.language
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.makeClusters
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.mark
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.one_voice
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.relative
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.skip
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.slashed_grace_container
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.time
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.times
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.transpose
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.voiceFour
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.voiceOne
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.voiceThree
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.voiceTwo
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.__call__
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.__eq__
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.__format__
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.__hash__
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.__ne__
   :noindex:

.. automethod:: abjad.tools.lilypondparsertools.GuileProxy.GuileProxy.__repr__
   :noindex:
