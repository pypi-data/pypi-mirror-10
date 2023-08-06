quantizationtools.SearchTree
============================

.. autoclass:: abjad.tools.quantizationtools.SearchTree.SearchTree

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
       subgraph cluster_quantizationtools {
           graph [label=quantizationtools];
           "quantizationtools.SearchTree" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>SearchTree</B>>,
               shape=oval,
               style="filled, rounded"];
           "quantizationtools.UnweightedSearchTree" [color=3,
               group=2,
               label=UnweightedSearchTree,
               shape=box];
           "quantizationtools.WeightedSearchTree" [color=3,
               group=2,
               label=WeightedSearchTree,
               shape=box];
           "quantizationtools.SearchTree" -> "quantizationtools.UnweightedSearchTree";
           "quantizationtools.SearchTree" -> "quantizationtools.WeightedSearchTree";
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.AbjadObject" -> "quantizationtools.SearchTree";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.quantizationtools.SearchTree.SearchTree.default_definition
      ~abjad.tools.quantizationtools.SearchTree.SearchTree.definition
      ~abjad.tools.quantizationtools.SearchTree.SearchTree.__call__
      ~abjad.tools.quantizationtools.SearchTree.SearchTree.__eq__
      ~abjad.tools.quantizationtools.SearchTree.SearchTree.__format__
      ~abjad.tools.quantizationtools.SearchTree.SearchTree.__hash__
      ~abjad.tools.quantizationtools.SearchTree.SearchTree.__ne__
      ~abjad.tools.quantizationtools.SearchTree.SearchTree.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.quantizationtools.SearchTree.SearchTree.default_definition
   :noindex:

.. autoattribute:: abjad.tools.quantizationtools.SearchTree.SearchTree.definition
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.quantizationtools.SearchTree.SearchTree.__call__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.SearchTree.SearchTree.__eq__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.SearchTree.SearchTree.__format__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.SearchTree.SearchTree.__hash__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.SearchTree.SearchTree.__ne__
   :noindex:

.. automethod:: abjad.tools.quantizationtools.SearchTree.SearchTree.__repr__
   :noindex:
