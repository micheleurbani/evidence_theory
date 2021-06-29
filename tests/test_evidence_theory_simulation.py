
import unittest
from evidence_theory_simulation import __version__
from evidence_theory_simulation import core


class TestFunctions(unittest.TestCase):

    def test_version(self):
        self.assertEqual(__version__, '0.1.0')

    def test_powerset(self):
        test_set = [1, 2, 3, 4]
        power_set = core.powerset(test_set)
        self.assertEqual(power_set, [[], [1], [2], [1, 2], [3], [1, 3],
                         [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4],
                         [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]])
