import pytest
from rectangles import Rectangle
from points import Point


def test_attributes():
    rec = Rectangle(1, 2, 4, 6)
    assert rec.top == 6
    assert rec.left == 1
    assert rec.bottom == 2
    assert rec.right == 4
    assert rec.width == 3
    assert rec.height == 4
    assert rec.topleft == Point(1, 6)
    assert rec.bottomleft == Point(1, 2)
    assert rec.topright == Point(4, 6)
    assert rec.bottomright == Point(4, 2)


def test_from_points():
    point1 = Point(1, 2)
    point2 = Point(3, 4)
    rectangle = Rectangle.from_points((point1, point2))
    assert rectangle == Rectangle(1, 2, 3, 4)


if __name__ == "__main__":
    pytest.main()
