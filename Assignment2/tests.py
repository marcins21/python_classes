import unittest
from exercises210_219 import *


class TestExercises(unittest.TestCase):
    def test_exercise_2_10(self):
        self.assertEqual(exercise_2_10("This is a test"), 4)

    def test_exercise_2_11(self):
        self.assertEqual(exercise_2_11("Hello"), "H_e_l_l_o")

    def test_exercise_2_12(self):
        self.assertEqual(exercise_2_12("This is a test"), ("Tiat", "ssat"))

    def test_exercise_2_13(self):
        self.assertEqual(exercise_2_13("This is a test"), 11)

    def test_exercise_2_14(self):
        self.assertEqual(exercise_2_14("This is a test"), ("This", 4))

    def test_exercise_2_15(self):
        self.assertEqual(exercise_2_15([1, 2, 3, 4]), "1234")

    def test_exercise_2_16(self):
        self.assertEqual(
            exercise_2_16("GvR is the creator of Python"),
            "Guido van Rossum is the creator of Python",
        )

    def test_exercise_2_17(self):
        self.assertEqual(
            exercise_2_17("Python is great and easy"),
            ("Python and easy great is", "is and easy great Python"),
        )

    def test_exercise_2_18(self):
        self.assertEqual(exercise_2_18(1020304050), 5)

    def test_exercise_2_19(self):
        self.assertEqual(exercise_2_19([1, 23, 456]), ["001", "023", "456"])


if __name__ == "__main__":
    unittest.main()
