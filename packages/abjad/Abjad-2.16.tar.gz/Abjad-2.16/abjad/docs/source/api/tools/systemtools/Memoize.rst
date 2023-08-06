systemtools.Memoize
===================

.. autoclass:: abjad.tools.systemtools.Memoize.Memoize

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
           "__builtin__.dict" [color=1,
               group=0,
               label=dict,
               shape=box];
           "__builtin__.object" [color=1,
               group=0,
               label=object,
               shape=box];
           "__builtin__.object" -> "__builtin__.dict";
       }
       subgraph cluster_systemtools {
           graph [label=systemtools];
           "systemtools.Memoize" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>Memoize</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.dict" -> "systemtools.Memoize";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.systemtools.Memoize.Memoize.clear
      ~abjad.tools.systemtools.Memoize.Memoize.copy
      ~abjad.tools.systemtools.Memoize.Memoize.get
      ~abjad.tools.systemtools.Memoize.Memoize.has_key
      ~abjad.tools.systemtools.Memoize.Memoize.items
      ~abjad.tools.systemtools.Memoize.Memoize.iteritems
      ~abjad.tools.systemtools.Memoize.Memoize.iterkeys
      ~abjad.tools.systemtools.Memoize.Memoize.itervalues
      ~abjad.tools.systemtools.Memoize.Memoize.keys
      ~abjad.tools.systemtools.Memoize.Memoize.pop
      ~abjad.tools.systemtools.Memoize.Memoize.popitem
      ~abjad.tools.systemtools.Memoize.Memoize.setdefault
      ~abjad.tools.systemtools.Memoize.Memoize.update
      ~abjad.tools.systemtools.Memoize.Memoize.values
      ~abjad.tools.systemtools.Memoize.Memoize.viewitems
      ~abjad.tools.systemtools.Memoize.Memoize.viewkeys
      ~abjad.tools.systemtools.Memoize.Memoize.viewvalues
      ~abjad.tools.systemtools.Memoize.Memoize.__call__
      ~abjad.tools.systemtools.Memoize.Memoize.__cmp__
      ~abjad.tools.systemtools.Memoize.Memoize.__contains__
      ~abjad.tools.systemtools.Memoize.Memoize.__delitem__
      ~abjad.tools.systemtools.Memoize.Memoize.__eq__
      ~abjad.tools.systemtools.Memoize.Memoize.__ge__
      ~abjad.tools.systemtools.Memoize.Memoize.__getitem__
      ~abjad.tools.systemtools.Memoize.Memoize.__gt__
      ~abjad.tools.systemtools.Memoize.Memoize.__iter__
      ~abjad.tools.systemtools.Memoize.Memoize.__le__
      ~abjad.tools.systemtools.Memoize.Memoize.__len__
      ~abjad.tools.systemtools.Memoize.Memoize.__lt__
      ~abjad.tools.systemtools.Memoize.Memoize.__missing__
      ~abjad.tools.systemtools.Memoize.Memoize.__ne__
      ~abjad.tools.systemtools.Memoize.Memoize.__repr__
      ~abjad.tools.systemtools.Memoize.Memoize.__setitem__

Bases
-----

- :py:class:`__builtin__.dict <dict>`

- :py:class:`__builtin__.object <object>`

Methods
-------

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.clear
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.copy
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.get
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.has_key
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.items
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.iteritems
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.iterkeys
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.itervalues
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.keys
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.pop
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.popitem
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.setdefault
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.update
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.values
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.viewitems
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.viewkeys
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.viewvalues
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.__call__
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.__cmp__
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.__contains__
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.__delitem__
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.__eq__
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.__ge__
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.__getitem__
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.__gt__
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.__iter__
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.__le__
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.__len__
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.__lt__
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.__missing__
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.__ne__
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.__repr__
   :noindex:

.. automethod:: abjad.tools.systemtools.Memoize.Memoize.__setitem__
   :noindex:
