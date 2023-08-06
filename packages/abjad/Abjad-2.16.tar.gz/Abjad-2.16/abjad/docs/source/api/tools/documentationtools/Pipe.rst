documentationtools.Pipe
=======================

.. autoclass:: abjad.tools.documentationtools.Pipe.Pipe

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
       subgraph cluster_documentationtools {
           graph [label=documentationtools];
           "documentationtools.Pipe" [color=black,
               fontcolor=white,
               group=2,
               label=<<B>Pipe</B>>,
               shape=box,
               style="filled, rounded"];
       }
       subgraph cluster_subprocess {
           graph [label=subprocess];
           "subprocess.Popen" [color=4,
               group=3,
               label=Popen,
               shape=box];
       }
       "__builtin__.object" -> "abctools.AbjadObject.AbstractBase";
       "__builtin__.object" -> "subprocess.Popen";
       "abctools.AbjadObject" -> "documentationtools.Pipe";
       "subprocess.Popen" -> "documentationtools.Pipe";
   }

.. only:: html

   Attribute summary
   -----------------

   .. autosummary::

      ~abjad.tools.documentationtools.Pipe.Pipe.arguments
      ~abjad.tools.documentationtools.Pipe.Pipe.close
      ~abjad.tools.documentationtools.Pipe.Pipe.communicate
      ~abjad.tools.documentationtools.Pipe.Pipe.executable
      ~abjad.tools.documentationtools.Pipe.Pipe.kill
      ~abjad.tools.documentationtools.Pipe.Pipe.poll
      ~abjad.tools.documentationtools.Pipe.Pipe.read
      ~abjad.tools.documentationtools.Pipe.Pipe.read_wait
      ~abjad.tools.documentationtools.Pipe.Pipe.send_signal
      ~abjad.tools.documentationtools.Pipe.Pipe.terminate
      ~abjad.tools.documentationtools.Pipe.Pipe.timeout
      ~abjad.tools.documentationtools.Pipe.Pipe.wait
      ~abjad.tools.documentationtools.Pipe.Pipe.write
      ~abjad.tools.documentationtools.Pipe.Pipe.write_line
      ~abjad.tools.documentationtools.Pipe.Pipe.__del__
      ~abjad.tools.documentationtools.Pipe.Pipe.__eq__
      ~abjad.tools.documentationtools.Pipe.Pipe.__format__
      ~abjad.tools.documentationtools.Pipe.Pipe.__hash__
      ~abjad.tools.documentationtools.Pipe.Pipe.__ne__
      ~abjad.tools.documentationtools.Pipe.Pipe.__repr__

Bases
-----

- :py:class:`abctools.AbjadObject <abjad.tools.abctools.AbjadObject.AbjadObject>`

- :py:class:`abctools.AbjadObject.AbstractBase <abjad.tools.abctools.AbjadObject.AbstractBase>`

- :py:class:`subprocess.Popen <subprocess.Popen>`

- :py:class:`__builtin__.object <object>`

Read-only properties
--------------------

.. autoattribute:: abjad.tools.documentationtools.Pipe.Pipe.arguments
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.Pipe.Pipe.executable
   :noindex:

.. autoattribute:: abjad.tools.documentationtools.Pipe.Pipe.timeout
   :noindex:

Methods
-------

.. automethod:: abjad.tools.documentationtools.Pipe.Pipe.close
   :noindex:

.. automethod:: abjad.tools.documentationtools.Pipe.Pipe.communicate
   :noindex:

.. automethod:: abjad.tools.documentationtools.Pipe.Pipe.kill
   :noindex:

.. automethod:: abjad.tools.documentationtools.Pipe.Pipe.poll
   :noindex:

.. automethod:: abjad.tools.documentationtools.Pipe.Pipe.read
   :noindex:

.. automethod:: abjad.tools.documentationtools.Pipe.Pipe.read_wait
   :noindex:

.. automethod:: abjad.tools.documentationtools.Pipe.Pipe.send_signal
   :noindex:

.. automethod:: abjad.tools.documentationtools.Pipe.Pipe.terminate
   :noindex:

.. automethod:: abjad.tools.documentationtools.Pipe.Pipe.wait
   :noindex:

.. automethod:: abjad.tools.documentationtools.Pipe.Pipe.write
   :noindex:

.. automethod:: abjad.tools.documentationtools.Pipe.Pipe.write_line
   :noindex:

Special methods
---------------

.. automethod:: abjad.tools.documentationtools.Pipe.Pipe.__del__
   :noindex:

.. automethod:: abjad.tools.documentationtools.Pipe.Pipe.__eq__
   :noindex:

.. automethod:: abjad.tools.documentationtools.Pipe.Pipe.__format__
   :noindex:

.. automethod:: abjad.tools.documentationtools.Pipe.Pipe.__hash__
   :noindex:

.. automethod:: abjad.tools.documentationtools.Pipe.Pipe.__ne__
   :noindex:

.. automethod:: abjad.tools.documentationtools.Pipe.Pipe.__repr__
   :noindex:
