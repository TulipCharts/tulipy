import unittest

import numpy as np
import pandas as pd
import tulipy as ti

CLOSE = np.array([81.59, 81.06, 82.87, 83,    83.61,
                  83.15, 82.84, 83.99, 84.55, 84.36,
                  85.53, 86.54, 86.89, 87.77, 87.29])


class TestIndicators(unittest.TestCase):

    EXPECTED = np.array([82.426, 82.738, 83.094, 83.318, 83.628,
                         83.778, 84.254, 84.994, 85.574, 86.218,
                         86.804]),

    def test_sma(self):
        actual = ti.sma(CLOSE, period=5, pad_none=False)
        self.assertTrue(np.allclose(actual, self.EXPECTED))

    def test_sma_accept_series(self):
        actual = ti.sma(pd.Series(CLOSE), period=5, pad_none=False)
        self.assertTrue(np.allclose(actual, self.EXPECTED))

    def test_sma_output_len_equal_input(self):
        actual = ti.sma(pd.Series(CLOSE), period=5)
        print(actual)
        self.assertEqual(len(actual), len(CLOSE))


if __name__ == '__main__':
    unittest.main()
