
import unittest
import numpy as np
from evidence_theory_simulation import __version__
from evidence_theory_simulation import core


class TestFunctions(unittest.TestCase):

    def test_version(self):
        self.assertEqual(__version__, '0.1.0')

    def test_powerset(self):
        m = 3
        ps = core.powerset(m)
        self.assertEqual(ps.shape[0], 2**m)

    def test__sample_mass_values(self):
        n = 4
        w = core._sample_mass_values(n)
        self.assertAlmostEqual(np.sum(w), 1)
