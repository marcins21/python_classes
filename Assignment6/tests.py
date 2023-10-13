import unittest
from points import Point
from math import sqrt


class TestPoint(unittest.TestCase):
    def setUp(self) -> None:
        self.point_a = Point(1, 1)
        self.point_b = Point(3, 3)
        self.point_c = Point(1, 1)
        self.point_d = Point(3, 19)

    def test_str(self):
        self.assertTrue(self.point_a.__str__() == "(1, 1)")
        self.assertTrue(self.point_b.__str__() == "(3, 3)")

    def test_repr(self):
        self.assertTrue(self.point_a.__repr__() == "Point(1, 1)")
        self.assertTrue(self.point_b.__repr__() == "Point(3, 3)")

    def test_eq(self):
        self.assertFalse(self.point_a == self.point_b)
        self.assertTrue(self.point_a == self.point_c)

    def test_ne(self):
        self.assertTrue(self.point_a != self.point_b)
        self.assertFalse(self.point_a != self.point_c)

    def test_add(self):
        self.assertTrue((self.point_a + self.point_b) == (4, 4))
        self.assertTrue((self.point_a + self.point_c) == (2, 2))

    def test_sub(self):
        self.assertTrue((self.point_a - self.point_b) == (-2, -2))
        self.assertTrue((self.point_a - self.point_c) == (0, 0))

    def test_mul(self):
        self.assertEquals((self.point_a * self.point_b), 6)
        self.assertEquals((self.point_a * self.point_c), 2)

    def test_length(self):
        self.assertEquals(self.point_a.length(), sqrt(2))
        self.assertEquals(self.point_b.length(), sqrt(18))
        self.assertEquals(self.point_c.length(), sqrt(2))

    def test_cross(self):
        self.assertEquals((self.point_a.__cross__(self.point_b)), 0)
        self.assertEquals((self.point_a.__cross__(self.point_d)), 16)
        self.assertEquals((self.point_a.__cross__(self.point_b)), 0)

    def test_hash(self):
        self.assertEquals(self.point_a.__hash__(), 8389048192121911274)


if __name__ == "__main__":
    unittest.main()
