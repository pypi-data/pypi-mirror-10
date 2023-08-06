abctools.Parser
===============

.. autoclass:: abjad.tools.abctools.Parser.Parser

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
           "abctools.Parser" [color=black,
               fontcolor=white,
               group=1,
               label=<<B>Parser</B>>,
               shape=oval,
               style="filled, rounded"];
           "abctools.AbjadObject" -> "abctools.Parser";
           "abctools.AbjadObject.AbstractBase" -> "abctools.AbjadObject";
       }
       subgraph cluster_lilypondparsertools {
           graph [label=lilypondparsertools];
           "lilypondparsertools.LilyPondParser" [color=3,
               group=2,
               label=LilyPondParser,
               shape=box];
           "lilypondparsertools.ReducedLyParser" [color=3,
               group=2,
               label=ReducedLyParser,
               shape=box];
           "lilypondparsertools.SchemeParser" [color=3,
               group=2,
               label=SchemeParser,
               shape=box];
       }
       subgraph cluster_rhythmtreetools {
           graph [label=rhythmtreetools];
           "rhythmtreetools.RhythmTreeParser" [color=4,
               group=3,
               label=RhythmTreeParser,
               shape=box];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "abctools.Parser" -> "lilypondparsertools.LilyPondParser";
       "abctools.Parser" -> "lilypondparsertools.ReducedLyParser";
       "abctools.Parser" -> "lilypondparsertools.SchemeParser";
       "abctools.Parser" -> "rhythmtreetools.RhythmTreeParser";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.abctools.Parser.Parser.debug
      ~abjad.tools.abctools.Parser.Parser.lexer
      ~abjad.tools.abctools.Parser.Parser.lexer_rules_object
      ~abjad.tools.abctools.Parser.Parser.logger
      ~abjad.tools.abctools.Parser.Parser.logger_path
      ~abjad.tools.abctools.Parser.Parser.output_path
      ~abjad.tools.abctools.Parser.Parser.parser
      ~abjad.tools.abctools.Parser.Parser.parser_rules_object
      ~abjad.tools.abctools.Parser.Parser.pickle_path
      ~abjad.tools.abctools.Parser.Parser.tokenize
      ~abjad.tools.abctools.Parser.Parser.__call__
      ~abjad.tools.abctools.Parser.Parser.__eq__
      ~abjad.tools.abctools.Parser.Parser.__format__
      ~abjad.tools.abctools.Parser.Parser.__hash__
      ~abjad.tools.abctools.Parser.Parser.__ne__
      ~abjad.tools.abctools.Parser.Parser.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.abctools.Parser.Parser.debug
   :noindex:

.. autoattribute:: abjad.tools.abctools.Parser.Parser.lexer
   :noindex:

.. autoattribute:: abjad.tools.abctools.Parser.Parser.lexer_rules_object
   :noindex:

.. autoattribute:: abjad.tools.abctools.Parser.Parser.logger
   :noindex:

.. autoattribute:: abjad.tools.abctools.Parser.Parser.logger_path
   :noindex:

.. autoattribute:: abjad.tools.abctools.Parser.Parser.output_path
   :noindex:

.. autoattribute:: abjad.tools.abctools.Parser.Parser.parser
   :noindex:

.. autoattribute:: abjad.tools.abctools.Parser.Parser.parser_rules_object
   :noindex:

.. autoattribute:: abjad.tools.abctools.Parser.Parser.pickle_path
   :noindex:

Methods
-------

.. automethod:: abjad.tools.abctools.Parser.Parser.tokenize
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.abctools.Parser.Parser.__call__
   :noindex:

.. automethod:: abjad.tools.abctools.Parser.Parser.__eq__
   :noindex:

.. automethod:: abjad.tools.abctools.Parser.Parser.__format__
   :noindex:

.. automethod:: abjad.tools.abctools.Parser.Parser.__hash__
   :noindex:

.. automethod:: abjad.tools.abctools.Parser.Parser.__ne__
   :noindex:

.. automethod:: abjad.tools.abctools.Parser.Parser.__repr__
   :noindex:
