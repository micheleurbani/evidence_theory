
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

    def test_sample_mass(self):
        n = 4
        m = 6
        w = core.sample_mass(n, m)
        self.assertAlmostEqual(np.sum(w), 1)

    def test_belief_plausibility(self):
        m = 4
        n = 3
        powerset = core.powerset(m)
        mass = core.sample_mass(n, len(powerset))
        belief = core.mass2belief(powerset, mass)
        plausibility = core.mass2plausibility(powerset, mass)
        self.assertTrue(np.all(belief <= plausibility))

    def test_hohle(self):
        m = 4  # number of elements in the X
        n = 6  # number of focal points
        assert n <= 2**m
        powerset = core.powerset(m)
        mass = core.sample_mass(n, len(powerset))
        df = core.generate_dataset(powerset, mass)
        ho = core.hohle(df)
