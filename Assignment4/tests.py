import unittest
from exercise4 import *


class TestExercises(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(1), 1)

    def test_ruler(self):
        print("\nPrinting Ruler Examples")
        print(make_ruler(10))
        print(make_ruler(5))
        print(make_ruler(15))
        print(make_ruler(20))

    def test_grid(self):
        print("\nPrinting Grid Examples")
        print(make_grid(2, 4))
        print(make_grid(2, 5))
        print(make_grid(3, 2))

    def test_odwracanie_iter(self):
        self.assertEqual(odwracanie_iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 4),[5, 4, 3, 2, 1, 6, 7, 8, 9, 10])
        self.assertEqual(odwracanie_iter([1, 2, 3, 4, 5, 6, 6, 5, 3, 2], 1,3), [1, 4, 3, 2, 5, 6, 6, 5, 3, 2])

    def test_odwracanie_rek(self):
        self.assertEqual(
            odwracanie_rek([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 4),
            [5, 4, 3, 2, 1, 6, 7, 8, 9, 10],
        )
        self.assertEqual(
            odwracanie_rek([1, 2, 3, 4, 5, 6, 6, 5, 3, 2], 1, 2),
            [1, 3, 2, 4, 5, 6, 6, 5, 3, 2],
        )

    def test_sum_seq(self):
        self.assertEqual(sum_seq([1, 2, [3, 3, [1, 2, 3]]]), 15)
        self.assertEqual(sum_seq([1, 2, [4, 3, [1, 2, 3]]]), 16)
        self.assertEqual(sum_seq([1, 1, 1, [[[[5], 3], 4]]]), 15)

    def test_flatten(self):
        seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
        self.assertEqual(flatten(seq), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        # Pozwolilem sobie dodac parametr sort - tak aby wynik był także sortowany
        self.assertEqual(
            flatten([1, 2, [3, 3, [1, 2, 3]]], sort=True), [1, 1, 2, 2, 3, 3, 3]
        )
        self.assertEqual(flatten([1, 2, [3, 3, [1, 2, 3]]]), [1, 2, 3, 3, 1, 2, 3])


if __name__ == "__main__":
    unittest.main()
