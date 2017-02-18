2. experipy.exp - The Experiment Runner
***************************************

This module provides the Experiment class for running compositions in the 
grammar, as well as the Exp Namespace for controlling and configuring Experiment 
behavior.

2.1. An Example
===============

::

    from experipy.exp       import Experiment
    from experipy.grammar   import Executable

    exp = Experiment(Executable("echo", ["Hello World"]), 
                     expname="test", 
                     destdir="results")
    exp.run()

This will run the program ``echo`` with the argument ``Hello World`` in a 
directory in ``/tmp``, writing the output and error, along with timing 
information, to the directory ``results``. Directories will be created as 
needed. 

2.2. Experiment objects
=======================

.. autoclass:: experipy.exp.Experiment
   :members:


2.3. The Exp Namespace
======================

Default values for paths and filenames in the Experiment class are controlled 
by a Namespace called ``Exp``. These defaults are listed below, and can be
overridden by setting a new value in the ``.experipyrc`` under the ``[Exp]``
section.

+----------+------------------+-------------------------------------------------+
| Key      | Default Value    | Description                                     |
+==========+==================+=================================================+
| shebang  | #!/bin/bash      | The first line of the generated shell scripts.  |
+----------+------------------+-------------------------------------------------+
| rundir   | /tmp             | Path to the directory where the experiment is   |
|          |                  | going to be run.                                |
+----------+------------------+-------------------------------------------------+
| defname  | exp              | Default name of experiments.                    |
+----------+------------------+-------------------------------------------------+
| runsh    | run.sh           | Name of the generated shell scripts.            |
+----------+------------------+-------------------------------------------------+
| out      | raw.out          | Name of the file which will collect the         |
|          |                  | experiment's standard output.                   |
+----------+------------------+-------------------------------------------------+
| err      | raw.err          | Name of the file which will collect the         |
|          |                  | experiment's standard error.                    |
+----------+------------------+-------------------------------------------------+
| timing   | harness_time.out | When an experiment is run using ``run()``, its  |
|          |                  | run time will be captured in this file.         |
+----------+------------------+-------------------------------------------------+
