from os         import path

from .grammar   import Executable

class Cd(Executable):
    def __init__(self, dirname):
        super(Cd, self).__init__("cd", [dirname])

class Cp(Executable):
    def __init__(self, target, dest, opts=""):
        super(Cp, self).__init__("cp", list((opts, '-t', dest, target)))

class Mkdir(Executable):
    def __init__(self, dirname):
        super(Mkdir, self).__init__("mkdir", [dirname])

class Mkfifo(Executable):
    def __init__(self, pipename):
        super(Mkdir, self).__init__("mkfifo", [pipename])

class Rm(Executable):
    def __init__(self, *files):
        super(Rm, self).__init__("rm", ["-rf"] + list(files))

class PythonScript(Executable):
    def __init__(self, script, sopts=[], pythonexe="/usr/bin/python", **kwargs):
        if 'inputs' in kwargs:
            kwargs['inputs'].append(path.abspath(script))
        else:
            kwargs['inputs'] = [path.abspath(script)]

        super(PythonScript, self).__init__(pythonexe, [script] + sopts, **kwargs)

