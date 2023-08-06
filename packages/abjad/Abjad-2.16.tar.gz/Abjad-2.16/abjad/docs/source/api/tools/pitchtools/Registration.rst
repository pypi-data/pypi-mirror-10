pitchtools.Registration
=======================

.. autoclass:: abjad.tools.pitchtools.Registration.Registration

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
       subgraph cluster_datastructuretools {
           graph [label=datastructuretools];
           "datastructuretools.TypedCollection" [color=3,
               group=2,
               label=TypedCollection,
               shape=oval,
               style=bold];
           "datastructuretools.TypedList" [color=3,
               group=2,
               label=TypedList,
               shape=box];
           "datastructuretools.TypedCollection" -> "datastructuretools.TypedList";
       }
       subgraph cluster_pitchtools {
           graph [label=pitchtools];
           "pitchtools.Registration" [color=black,
               fontcolor=white,
               group=3,
               label=<<B>Registration</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "datastructuretools.TypedCollection";
       "datastructuretools.TypedList" -> "pitchtools.Registration";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.pitchtools.Registration.Registration.append
      ~abjad.tools.pitchtools.Registration.Registration.count
      ~abjad.tools.pitchtools.Registration.Registration.extend
      ~abjad.tools.pitchtools.Registration.Registration.index
      ~abjad.tools.pitchtools.Registration.Registration.insert
      ~abjad.tools.pitchtools.Registration.Registration.item_class
      ~abjad.tools.pitchtools.Registration.Registration.items
      ~abjad.tools.pitchtools.Registration.Registration.keep_sorted
      ~abjad.tools.pitchtools.Registration.Registration.pop
      ~abjad.tools.pitchtools.Registration.Registration.remove
      ~abjad.tools.pitchtools.Registration.Registration.reverse
      ~abjad.tools.pitchtools.Registration.Registration.sort
      ~abjad.tools.pitchtools.Registration.Registration.__call__
      ~abjad.tools.pitchtools.Registration.Registration.__contains__
      ~abjad.tools.pitchtools.Registration.Registration.__delitem__
      ~abjad.tools.pitchtools.Registration.Registration.__eq__
      ~abjad.tools.pitchtools.Registration.Registration.__format__
      ~abjad.tools.pitchtools.Registration.Registration.__getitem__
      ~abjad.tools.pitchtools.Registration.Registration.__hash__
      ~abjad.tools.pitchtools.Registration.Registration.__iadd__
      ~abjad.tools.pitchtools.Registration.Registration.__iter__
      ~abjad.tools.pitchtools.Registration.Registration.__len__
      ~abjad.tools.pitchtools.Registration.Registration.__ne__
      ~abjad.tools.pitchtools.Registration.Registration.__repr__
      ~abjad.tools.pitchtools.Registration.Registration.__reversed__
      ~abjad.tools.pitchtools.Registration.Registration.__setitem__

Bases
-----

- :py:class:`datastructuretools.TypedList <abjad.tools.datastructuretools.TypedList.TypedList>`

- :py:class:`datastructuretools.TypedCollection <abjad.tools.datastructuretools.TypedCollection.TypedCollection>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.pitchtools.Registration.Registration.item_class
   :noindex:

.. autoattribute:: abjad.tools.pitchtools.Registration.Registration.items
   :noindex:

Read/write properties
---------------------

.. autoattribute:: abjad.tools.pitchtools.Registration.Registration.keep_sorted
   :noindex:

Methods
-------

.. automethod:: abjad.tools.pitchtools.Registration.Registration.append
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.count
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.extend
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.index
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.insert
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.pop
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.remove
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.reverse
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.sort
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.pitchtools.Registration.Registration.__call__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.__contains__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.__delitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.__eq__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.__format__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.__getitem__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.__hash__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.__iadd__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.__iter__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.__len__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.__ne__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.__repr__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.__reversed__
   :noindex:

.. automethod:: abjad.tools.pitchtools.Registration.Registration.__setitem__
   :noindex:
