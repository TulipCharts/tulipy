import unittest

import numpy as np
import tulipy as ti

from sys import float_info

CLOSE = np.array([81.59, 81.06, 82.87, 83, 83.61,
                  83.15, 82.84, 83.99, 84.55, 84.36,
                  85.53, 86.54, 86.89, 87.77, 87.29])

SMA_EXPECTED = np.array([82.426, 82.738, 83.094, 83.318, 83.628,
                         83.778, 84.254, 84.994, 85.574, 86.218,
                         86.804])

RSI_EXPECTED = np.array([72.034, 64.927, 75.936, 79.796, 74.713,
                         83.033, 87.478, 88.755, 91.483, 78.498])

PTI_RSI_EXPECTED = np.array(
    [float_info.max, float_info.max, float_info.max, float_info.max, float_info.max,
     72.034, 64.927, 75.936, 79.796, 74.713,
     83.033, 87.478, 88.755, 91.483, 78.498])


class TestIndicators(unittest.TestCase):
    pst_no_expected = -1

    def test_sma(self):
        print('\n--->', self._testMethodName)
        actual = ti.sma(CLOSE, period=5)
        print(actual)
        self.assertTrue(np.allclose(actual, SMA_EXPECTED))

    def test_pti_init(self):
        print('\n--->', self._testMethodName)
        pst_id = self._testMethodName
        pst_type = "pti_rsi"
        pst_no = ti.pst_ti_init(pst_id, pst_type, [5])
        self.pst_no_expected += 1
        print("pst_no=%d, expected=%d" % (pst_no, self.pst_no_expected))
        self.assertEqual(pst_no, self.pst_no_expected)

    def test_rsi(self):
        print('\n--->', self._testMethodName)
        actual = ti.rsi(CLOSE, period=5)
        print(actual)
        self.assertTrue(np.allclose(actual, RSI_EXPECTED))

    def test_pti_rsi_all(self):
        print('\n--->', self._testMethodName)
        pst_id = self._testMethodName
        pst_type = "pti_rsi"
        pst_no = ti.pst_ti_init(pst_id, pst_type, [5])
        self.pst_no_expected += 1
        print("pst_no=%d, expected=%d" % (pst_no, self.pst_no_expected))

        actual = ti.pti_rsi(CLOSE, pst_no)
        print(actual)
        self.assertTrue(np.allclose(actual, PTI_RSI_EXPECTED))

    def test_pti_rsi_1(self):
        print('--->', self._testMethodName)
        pst_no = ti.pst_ti_init("pst_ti_1", "pti_rsi", [5])
        actual = np.zeros(CLOSE.shape[0], dtype=float)
        for i in range(CLOSE.shape[0]):
            actual[i] = ti.pti_rsi(np.array([CLOSE[i]]), pst_no)[0]
        print("input:", CLOSE)
        print("output:", actual)
        print("expected:", PTI_RSI_EXPECTED)
        self.assertTrue(np.allclose(actual, PTI_RSI_EXPECTED))


if __name__ == '__main__':
    unittest.main()
