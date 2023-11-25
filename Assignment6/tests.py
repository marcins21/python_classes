import unittest
from points import Point
from rectangles import Rectangle

from math import sqrt


class TestRectangleAndPoint(unittest.TestCase):
    #Point
    def setUp(self) -> None:
        self.point_a = Point(1, 1)
        self.point_b = Point(3, 3)
        self.point_c = Point(1, 1)
        self.point_d = Point(3, 19)

    def test_str(self):
        self.assertTrue(str(self.point_a) == "(1, 1)")
        self.assertTrue(str(self.point_b) == "(3, 3)")

    def test_repr(self):
        self.assertTrue(repr(self.point_a) == "Point(1, 1)")
        self.assertTrue(repr(self.point_b) == "Point(3, 3)")

    def test_eq(self):
        self.assertFalse(self.point_a == self.point_b)
        self.assertTrue(self.point_a == self.point_c)

    def test_ne(self):
        self.assertTrue(self.point_a != self.point_b)
        self.assertFalse(self.point_a != self.point_c)

    def test_add(self):
        self.assertTrue((self.point_a + self.point_b) == Point(4, 4))
        self.assertTrue((self.point_a + self.point_c) == Point(2, 2))

    def test_sub(self):
        self.assertTrue((self.point_a - self.point_b) == Point(-2, -2))
        self.assertTrue((self.point_a - self.point_c) == Point(0, 0))

    def test_mul(self):
        self.assertEquals((self.point_a * self.point_b), 6)
        self.assertEquals((self.point_a * self.point_c), 2)

    def test_length(self):
        self.assertEqual(self.point_a.length(), sqrt(2))
        self.assertEqual(self.point_b.length(), sqrt(18))
        self.assertEqual(self.point_c.length(), sqrt(2))

    def test_cross(self):
        self.assertEquals((self.point_a.__cross__(self.point_b)), 0)
        self.assertEquals((self.point_a.__cross__(self.point_d)), 16)
        self.assertEquals((self.point_a.__cross__(self.point_b)), 0)

    def test_hash(self):
        self.assertEquals(self.point_a.__hash__(), 8389048192121911274)

    #Rectangle
    def test_init(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.point_1, Point(1, 2))
        self.assertEqual(rect.point_2, Point(3, 4))

    def test_rec_str(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(rect), "[(1, 2), (3, 4)]")

    def test_rec_repr(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(repr(rect), "Rectangle(1, 2, 3, 4)")

    def test_rec_eq(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect1, rect2)

    def test_rec_ne(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(5, 6, 7, 8)
        self.assertNotEqual(rect1, rect2)

    def test_center(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.center(), Point(2, 3))

    def test_area(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.area(), 4)

    def test_move(self):
        rect = Rectangle(1, 2, 3, 4)
        rect_moved = rect.move(1, 1)
        self.assertEqual(rect_moved.point_1, Point(2, 3))
        self.assertEqual(rect_moved.point_2, Point(4, 5))
        self.assertEqual(rect_moved, Rectangle(2, 3, 4, 5))

if __name__ == "__main__":
    unittest.main()
