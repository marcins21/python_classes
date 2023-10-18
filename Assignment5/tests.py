import unittest
from fracs import *


class TestFracs(unittest.TestCase):
    def test_add_frac(self):
        self.assertEqual(add_frac([1, 9], [3, 27]), [2, 9])
        self.assertEqual(add_frac([1, 3], [3, 27]), [4, 9])
        self.assertEqual(add_frac([1, 17], [81, 27]), [52, 17])
        self.assertEqual(add_frac([0, 17], [0, 27]), 0)
        self.assertEqual(add_frac([1, 0], [81, 27]), "unknown")

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 9], [3, 27]), 0)
        self.assertEqual(sub_frac([1, 17], [81, 27]), [-50, 17])
        self.assertEqual(sub_frac([0, 9], [3, 27]), [-1, 9])
        self.assertEqual(sub_frac([1, 0], [3, 0]), "unknown")
        self.assertEqual(sub_frac([1, 0], [3, 27]), "unknown")

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 9], [3, 27]), [1, 81])
        self.assertEqual(mul_frac([1, 1], [3, 3]), [1, 1])
        self.assertEqual(mul_frac([0, 1], [3, 3]), 0)
        self.assertEqual(mul_frac([1, 0], [3, 3]), "unknown")

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 9], [3, 27]), [1, 1])
        self.assertEqual(div_frac([1, 1], [3, 3]), [1, 1])
        self.assertEqual(div_frac([0, 9], [3, 27]), 0)
        self.assertEqual(div_frac([3, 0], [3, 27]), "unknown")

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 27], [1, 81]), -1)
        self.assertEqual(cmp_frac([1, 2], [1, 81]), -1)
        self.assertEqual(cmp_frac([1, 3], [1, 4]), -1)
        self.assertEqual(cmp_frac([1, 27], [133, 81]), 1)
        self.assertEqual(cmp_frac([1, 1], [3, 3]), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float([6, 3]), 2.0)
        self.assertEqual(frac2float([20, 3]), 6.666666666666667)
        self.assertEqual(frac2float([10, 4]), 2.5)

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertFalse(is_positive([1, -2]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 1]))
        self.assertFalse(is_zero([1, 2]))


if __name__ == "__main__":
    unittest.main()
