.. experipy documentation master file, created by
   sphinx-quickstart on Thu Feb 16 21:19:56 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

experipy: Automating Script Generation
======================================

``experipy`` is a framework for writing and running Computational Science
experiments. It provides facilities for describing an experiment as a shell 
script, and mechanisms for running them. Experiments can be run locally and also
submitted to a cluster's job queuing system as a PBS script.

::

    from experipy.exp       import Experiment
    from experipy.grammar   import Executable

    echo = Executable("echo", 
        ["Hello World", "> test.out"], 
        outputs=["test.out"]
    )

    exp = Experiment(echo, expname="test", destdir="results")
    exp.run()
    
The intention of ``experipy`` is to act as the core of a researcher's scripting
framework. In the author's research group, projects often involved running 
dozens of benchmarks with hundreds of configurations in parallel across a 
cluster, so ``experipy`` was designed to ease the design and scripting of new
experiments and configurations.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   grammar
   exp
   system
   utils


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
