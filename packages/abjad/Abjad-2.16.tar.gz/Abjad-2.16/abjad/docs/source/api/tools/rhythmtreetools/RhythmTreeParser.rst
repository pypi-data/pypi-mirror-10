rhythmtreetools.RhythmTreeParser
================================

.. autoclass:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser

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
           "abctools.Parser" [color=2,
               group=1,
               label=Parser,
               shape=oval,
               style=bold];
           "abctools.AbjadObject" -> "abctools.Parser";
           "abctools.AbjadObject.AbstractBase" -> "abctools.AbjadObject";
       }
       subgraph cluster_rhythmtreetools {
           graph [label=rhythmtreetools];
           "rhythmtreetools.RhythmTreeParser" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>RhythmTreeParser</B>>,
               shape=box,
               style="filled, rounded"];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.Parser" -> "rhythmtreetools.RhythmTreeParser";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.debug
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.lexer
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.lexer_rules_object
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.logger
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.logger_path
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.output_path
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_container__LPAREN__DURATION__node_list_closed__RPAREN
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_error
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_leaf__INTEGER
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_node__container
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_node__leaf
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_node_list__node_list__node_list_item
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_node_list__node_list_item
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_node_list_closed__LPAREN__node_list__RPAREN
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_node_list_item__node
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_toplevel__EMPTY
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_toplevel__toplevel__node
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.parser
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.parser_rules_object
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.pickle_path
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.t_DURATION
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.t_error
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.t_newline
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.tokenize
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.__call__
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.__eq__
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.__format__
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.__hash__
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.__ne__
      ~abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.__repr__

Bases
-----

- :py:class:`abctools.Parser <abjad.tools.abctools.Parser.Parser>`

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.debug
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.lexer
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.lexer_rules_object
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.logger
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.logger_path
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.output_path
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.parser
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.parser_rules_object
   :noindex:

.. autoattribute:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.pickle_path
   :noindex:

Methods
-------

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_container__LPAREN__DURATION__node_list_closed__RPAREN
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_error
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_leaf__INTEGER
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_node__container
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_node__leaf
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_node_list__node_list__node_list_item
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_node_list__node_list_item
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_node_list_closed__LPAREN__node_list__RPAREN
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_node_list_item__node
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_toplevel__EMPTY
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.p_toplevel__toplevel__node
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.t_DURATION
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.t_error
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.t_newline
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.tokenize
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.__call__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.__eq__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.__format__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.__hash__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.__ne__
   :noindex:

.. automethod:: abjad.tools.rhythmtreetools.RhythmTreeParser.RhythmTreeParser.__repr__
   :noindex:
