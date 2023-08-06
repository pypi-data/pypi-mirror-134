import unittest

import automata

class TestVersion(unittest.TestCase):

    def test_version(self):
        print("version", automata.__version__)
        self.assertTrue(hasattr(automata, "__version__"))
