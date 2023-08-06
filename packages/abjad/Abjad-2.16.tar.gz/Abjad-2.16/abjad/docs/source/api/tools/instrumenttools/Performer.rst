instrumenttools.Performer
=========================

.. autoclass:: abjad.tools.instrumenttools.Performer.Performer

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
       subgraph cluster_instrumenttools {
           graph [label=instrumenttools];
           "instrumenttools.Performer" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Performer</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "instrumenttools.Performer";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.instrumenttools.Performer.Performer.get_instrument
      ~abjad.tools.instrumenttools.Performer.Performer.instrument_count
      ~abjad.tools.instrumenttools.Performer.Performer.instruments
      ~abjad.tools.instrumenttools.Performer.Performer.is_doubling
      ~abjad.tools.instrumenttools.Performer.Performer.likely_instruments_based_on_performer_name
      ~abjad.tools.instrumenttools.Performer.Performer.list_performer_names
      ~abjad.tools.instrumenttools.Performer.Performer.list_primary_performer_names
      ~abjad.tools.instrumenttools.Performer.Performer.make_performer_name_instrument_dictionary
      ~abjad.tools.instrumenttools.Performer.Performer.most_likely_instrument_based_on_performer_name
      ~abjad.tools.instrumenttools.Performer.Performer.name
      ~abjad.tools.instrumenttools.Performer.Performer.__eq__
      ~abjad.tools.instrumenttools.Performer.Performer.__format__
      ~abjad.tools.instrumenttools.Performer.Performer.__hash__
      ~abjad.tools.instrumenttools.Performer.Performer.__ne__
      ~abjad.tools.instrumenttools.Performer.Performer.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.instrumenttools.Performer.Performer.instrument_count
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Performer.Performer.is_doubling
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Performer.Performer.likely_instruments_based_on_performer_name
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Performer.Performer.most_likely_instrument_based_on_performer_name
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.instrumenttools.Performer.Performer.instruments
   :noindex:

.. autoattribute:: abjad.tools.instrumenttools.Performer.Performer.name
   :noindex:

Methods
-------

.. automethod:: abjad.tools.instrumenttools.Performer.Performer.get_instrument
   :noindex:

Static methods
--------------

.. automethod:: abjad.tools.instrumenttools.Performer.Performer.list_performer_names
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Performer.Performer.list_primary_performer_names
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Performer.Performer.make_performer_name_instrument_dictionary
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.instrumenttools.Performer.Performer.__eq__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Performer.Performer.__format__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Performer.Performer.__hash__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Performer.Performer.__ne__
   :noindex:

.. automethod:: abjad.tools.instrumenttools.Performer.Performer.__repr__
   :noindex:
