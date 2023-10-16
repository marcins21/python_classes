from rectangles import Rectangle
from points import Point
import unittest


class TestRectangle(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Rectangle(4, 5, 6, 7)), "[(4, 5), (6, 7)]")
        self.assertEqual(str(Rectangle(3, 1, 10, 11)), "[(3, 1), (10, 11)]")

    def test_rpr(self):
        self.assertEqual(repr(Rectangle(2, 4, 34, 44)), "Rectangle(2, 4, 34, 44)")
        self.assertEqual(repr(Rectangle(0, -99, 123, 83)), "Rectangle(0, -99, 123, 83)")

    def test_eq(self):
        self.assertEqual(Rectangle(3, -2, 23, 14), Rectangle(3, -2, 23, 14))
        self.assertEqual(Rectangle(8, 23, 45, 51), Rectangle(8, 23, 45, 51))

    def test_ne(self):
        self.assertNotEqual(Rectangle(-4, -6, 2, 7), Rectangle(87, 54, 2222, 5675))
        self.assertNotEqual(Rectangle(1, 5, 7221, 893), Rectangle(4, 34, 111, 54839))

    def test_center(self):
        self.assertEqual(Rectangle(1, 2, 5, 5).center(), Point(3.0, 3.5))
        self.assertEqual(Rectangle(5, 2, 9, 12).center(), Point(7.0, 7.0))

    def test_area(self):
        self.assertEqual(Rectangle(2, 3, 4, 5).area(), 4)
        self.assertEqual(Rectangle(11, 13, 56, 45).area(), 1440)

    def test_move(self):
        self.assertEqual(Rectangle(3, 2, 16, 73).move(6, 7), "[(9, 9), (22, 80)]")
        self.assertEqual(Rectangle(-4, -1, 892, 100).move(4, 9), "[(0, 8), (896, 109)]")

    def test_intersection(self):
        self.assertEqual(Rectangle(0, 0, 7, 7).intersection(Rectangle(3, 3, 3, 3)), Rectangle(3, 3, 3, 3))

    def test_cover(self):
        self.assertEqual(Rectangle(2, 2, 5, 5).cover(Rectangle(4, 4, 6, 6)), Rectangle(2, 2, 6, 6))
        self.assertEqual(Rectangle(2, 2, 4, 4).cover(Rectangle(4, 4, 6, 6)), Rectangle(2, 2, 6, 6))


if __name__ == '__main__':
    unittest.main()