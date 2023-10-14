import unittest
from exercise3 import *


class TestExercises(unittest.TestCase):
    def test_modulo_3_3(self):
        print("\nPrinting 0-30 number without numbers divisible by 3")
        exercise_3_3()

    def test_cube(self):
        print("\nEnter number to get cubic number, enter 'stop' to stop")
        exercise_3_4()

    def test_ruler(self):
        print("\nPrinting Ruler Examples")
        print(exercise_3_5(10))
        print(exercise_3_5(5))
        print(exercise_3_5(15))
        print(exercise_3_5(20))

    def test_grid(self):
        print("\nPrinting Grid Examples")
        print(exercise_3_6(2, 4))
        print(exercise_3_6(2, 5))
        print(exercise_3_6(3, 2))

    def test_sum_of_lists(self):
        self.assertEqual(
            exercise_3_9([[], [4], (1, 2), [3, 4], (5, 6, 7)]), [0, 4, 3, 7, 18]
        )
        self.assertEqual(exercise_3_9([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [6, 15, 24])

    def test_roman_to_arabic(self):
        self.assertEqual(exercise_3_10("MIV"), 1004)
        self.assertEqual(exercise_3_10("XCIV"), 94)
        self.assertEqual(exercise_3_10("XXI"), 21)

    def test_intersection_3_8(self):
        intersection, union = exercise_3_8([1, 2, 3, 4], [3, 4, 6, 7, 7])
        self.assertEqual(intersection, [3, 4])
        self.assertEqual(union, [1, 2, 3, 4, 6, 7])

        intersection, union = exercise_3_8([1, 2, 3], [4, 5, 6, 3])
        self.assertEqual(intersection, [3])
        self.assertEqual(union, [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
