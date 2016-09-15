from os import path

from experipy.system import PythonScript
from experipy.exp    import Experiment

if __name__ == "__main__":
    testscript = path.join(path.dirname(__file__), "test.py")
    Experiment(PythonScript(testscript), 
        path.join(path.dirname(__file__), "results/")
    ).run(rm_rundir=False)
