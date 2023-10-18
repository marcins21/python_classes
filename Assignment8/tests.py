import unittest
from rectangles import Rectangle
from points import Point

class TestRectangle(unittest.TestCase):
    def test_properties(self):
        testing_rectangle = Rectangle(1,1,3,3)
        self.assertEqual(testing_rectangle.top, 3)
        self.assertEqual(testing_rectangle.bottom, 1)
        self.assertEqual(testing_rectangle.left, 1)
        self.assertEqual(testing_rectangle.right, 3)
        self.assertEqual(testing_rectangle.height, 2)
        self.assertEqual(testing_rectangle.width, 2)

    def test_properties_with_point(self):
        testing_rectangle = Rectangle(1,1,3,3)
        self.assertEqual(testing_rectangle.topleft, Point(1, 3))
        self.assertEqual(testing_rectangle.bottomleft, Point(1, 1))
        self.assertEqual(testing_rectangle.topright, Point(3, 3))
        self.assertEqual(testing_rectangle.bottomright, Point(3, 1))

    def test_from_points(self):
        testing_rectangle = Rectangle.from_points(points=(Point(1,1),Point(3,3)))
        self.assertEqual(testing_rectangle.point_1, Point(1, 1))
        self.assertEqual(testing_rectangle.point_2, Point(3, 3))

