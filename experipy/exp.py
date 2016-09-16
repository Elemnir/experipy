import shutil
import sys

from datetime   import datetime
from os         import chmod, makedirs, path
from subprocess import call
from time       import time

from .grammar   import ElementBase
from .system    import Cd, Cp, Mkdir
from .utils     import Namespace

Exp = Namespace(
    runsh   = "run.sh",
    shebang = "#!/bin/bash",
    rundir  = "/tmp",
    defname = "exp",
    out     = "raw.out",
    err     = "raw.err",
    timing  = "harness_time.out"
)

class ExpError(Exception):
    pass

class Experiment(object):
    def __init__(self, cmd, destdir):
        if not isinstance(cmd, ElementBase):
            raise ExpError("'{}' is not an instance of ElementBase".format(cmd))

        self.cmd     = cmd
        self.destdir = path.abspath(destdir)
    
    def write_runscript(self, fname=Exp.runsh, dryrun=False):
        # Open the file and write the preamble
        f = open(fname, "w") if not dryrun else sys.stdout
        f.write(Exp.shebang + "\n\n")
        
        # Collect experiment input files
        f.write("# Experiment setup\n")
        for infile in self.cmd.inputs:
            f.write(str(Cp(infile, "."))+"\n")
        
        # Execute the experiment components
        f.write("\n# Run experiment\n")
        f.write(str(self.cmd)+"\n\n")
        
        # Exfill the experiment output files we care about, including runscript and output
        f.write("# Collect output files\n")
        for outfile in self.cmd.outputs:
            f.write(str(Cp(outfile, self.destdir))+"\n")
        f.write(str(Cp(fname, self.destdir))+"\n")
        f.write(str(Cp(Exp.out, self.destdir))+"\n")
        f.write(str(Cp(Exp.err, self.destdir))+"\n")

        if f != sys.stdout:
            f.close()
            chmod(fname, 0755)

    def run(self, expname=Exp.defname, rm_rundir=True):
        # Determine and create the experiment directory
        rundir = path.join(Exp.rundir, expname + "." + str(int(time())))
        fname  = path.join(rundir, Exp.runsh)
        if not path.exists(rundir):
            makedirs(rundir)

        # Create the results directory as necessary, deleting any previous contents
        if path.exists(self.destdir):
            shutil.rmtree(self.destdir)
        makedirs(self.destdir)
        
        # Open the output, error and timing file handles for call
        out = open(path.join(rundir, Exp.out), 'w')
        err = open(path.join(rundir, Exp.err), 'w')
        timing = open(path.join(self.destdir, Exp.timing), 'w')

        # Write the runscript in the exp dir
        self.write_runscript(fname)
        
        # Execute call and time the result
        start = datetime.now()
        call(fname, stdout=out, stderr=err, cwd=rundir)
        runtime = datetime.now() - start
        timing.write(str(runtime)+"\n")

        # Clean up, close file descriptors and delete the rundir (if needed)
        out.close()
        err.close()
        timing.close()
        if rm_rundir:
            shutil.rmtree(rundir)
        

    def queue(self):
        pass
