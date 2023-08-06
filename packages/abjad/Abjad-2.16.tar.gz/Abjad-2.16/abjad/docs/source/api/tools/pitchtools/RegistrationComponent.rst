pitchtools.RegistrationComponent
================================

.. autoclass:: abjad.tools.pitchtools.RegistrationComponent.RegistrationComponent

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
           "pitchtools.RegistrationComponent" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>RegistrationComponent</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "pitchtools.RegistrationComponent";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.RegistrationComponent.RegistrationComponent.source_pitch_range
      ~abjad.tools.pitchtools.RegistrationComponent.RegistrationComponent.target_octave_start_pitch
      ~abjad.tools.pitchtools.RegistrationComponent.RegistrationComponent.__eq__
      ~abjad.tools.pitchtools.RegistrationComponent.RegistrationComponent.__format__
      ~abjad.tools.pitchtools.RegistrationComponent.RegistrationComponent.__hash__
      ~abjad.tools.pitchtools.RegistrationComponent.RegistrationComponent.__ne__
      ~abjad.tools.pitchtools.RegistrationComponent.RegistrationComponent.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.RegistrationComponent.RegistrationComponent.source_pitch_range
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.RegistrationComponent.RegistrationComponent.target_octave_start_pitch
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.RegistrationComponent.RegistrationComponent.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationComponent.RegistrationComponent.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationComponent.RegistrationComponent.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationComponent.RegistrationComponent.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.RegistrationComponent.RegistrationComponent.__repr__
   :noindex:
