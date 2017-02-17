2. experipy.exp - The Experiment Runner
***************************************

.. automodule:: experipy.exp

2.1. Experiment class
=====================

.. autoclass:: experipy.exp.Experiment
   :members:

2.2. An Example
===============

::

    from experipy.exp       import Experiment
    from experipy.grammar   import Executable

    exp = Experiment(Executable("echo", ["Hello World"]), 
                     expname="test", 
                     destdir="results")
    exp.run()

This will run the program ``echo`` with the argument ``Hello World`` in a directory in ``/tmp``, writing the output and error, along with timing information, to the directory ``results``. Directories will be created as needed. 
