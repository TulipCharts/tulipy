import unittest

import numpy as np
import tulipy as ti

CLOSE = np.array([81.59, 81.06, 82.87, 83,    83.61,
                  83.15, 82.84, 83.99, 84.55, 84.36,
                  85.53, 86.54, 86.89, 87.77, 87.29])

class TestIndicators(unittest.TestCase):

    def test_sma(self):
        expected = {
            'sma': np.array([82.426, 82.738, 83.094, 83.318, 83.628,
                             83.778, 84.254, 84.994, 85.574, 86.218,
                             86.804]),
        }

        inputs = {'real': CLOSE}
        options = {'period': 5.0}

        actual = ti.sma(inputs, options)

        self.assertIn('sma', actual)
        self.assertTrue(np.allclose(actual['sma'], expected['sma']))

if __name__ == '__main__':
    unittest.main()

