import unittest

from experipy.grammar import Executable, Wrapper, Pipeline, Group

class TestExecutable(unittest.TestCase):
    def test_render(self):
        exe = Executable("cat", ["1.txt", "2.txt"])
        self.assertEqual(str(exe), "cat 1.txt 2.txt")

    def test_output(self):
        exe = Executable("echo", 
            ['"Hello World"', "> test.txt"], 
            outputs=["test.txt"]
        )
        self.assertEqual(list(exe.outputs()),["test.txt"])

    def test_wait(self):
        exe = Executable("ping", wait=False)
        self.assertEqual(str(exe), "ping &")
