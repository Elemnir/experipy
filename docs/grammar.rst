1. experipy.grammar - Composing experiments
*******************************************

This module provides the core elements which compose the Experipy grammar: 
Executables, Wrappers, Pipelines, and Groups. These elements facilitate 
specifying programs to execute as well as the files they depend on.

1.1. Element objects
====================

.. autoclass:: experipy.grammar.Element
   :members:


1.2. Executable objects
=======================

The Executable class extends the base Element class by providing an abstraction 
for describing a program executable. Once instantiated, converting an Executable
object to a string will yield the command string that will be entered into the
shell script.

.. autoclass:: experipy.grammar.Executable
   :members:


1.3. Wrapper objects
====================

Wrappers are executables which accept another Executable and its arguments as a
parameter, and incorporates the wrapped Executable into its argument list and
collection of inputs and outputs.

.. autoclass:: experipy.grammar.Wrapper
   :members:


1.4. Pipeline objects
=====================

The Linux shell supports piping of output from one program into the input of 
another. Pipelines provide a mechanism to support that feature in the 
generated shell scripts. 

.. autoclass:: experipy.grammar.Pipeline
   :members:


1.5. Group objects
==================

Groups allow generation of more complex experiment behavior than the execution 
of a single Executable, Wrapper, or Pipeline. 

.. autoclass:: experipy.grammar.Group
   :members:



