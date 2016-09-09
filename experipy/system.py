from .grammar import Executable

class Rm(Executable):
    def __init__(self, *files):
        super(Rm, self).__init__("rm", ["-rf"] + list(files))

class Mkdir(Executable):
    def __init__(self, dirname):
        super(Mkdir, self).__init__("mkdir", [dirname])

class Mkfifo(Executable):
    def __init__(self, pipename):
        super(Mkdir, self).__init__("mkfifo", [pipename])
