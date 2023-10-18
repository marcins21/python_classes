from points import Point


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.point_1 = Point(x1, y1)
        self.point_2 = Point(x2, y2)

    @property
    def top(self):
        return self.point_2.y

    @property
    def bottom(self):
        return self.point_1.y

    @property
    def right(self):
        return self.point_2.x

    @property
    def left(self):
        return self.point_1.x

    @property
    def topleft(self):
        return Point(self.point_1.x, self.point_2.y)

    @property
    def topright(self):
        return Point(self.point_2.x, self.point_2.y)

    @property
    def bottomright(self):
        return Point(self.point_2.x, self.point_1.y)

    @property
    def bottomleft(self):
        return Point(self.point_1.x, self.point_1.y)

    @property
    def width(self):
        return abs(self.point_2.x - self.point_1.x)

    @property
    def height(self):
        return abs(self.point_2.y - self.point_1.y)

    @classmethod
    def from_points(cls, points):
        if not isinstance(points, tuple):
            raise ValueError("Points need to be a tuple")
        if len(points) != 2:
            raise ValueError("Program needs 2 points")

        result = cls(points[0].x, points[0].y, points[1].x, points[1].y)
        return result


    def __str__(self):
        return f"[{self.point_1.__str__()}, {self.point_2.__str__()}]"

    def __repr__(self):
        return f"Rectangle({self.x1}, {self.y1}, {self.x2}, {self.y2})"

    def __eq__(self, other: "Rectangle"):
        return (
            (self.x1 == other.x1)
            and (self.y1 == other.y1)
            and (self.x2 == other.x2)
            and (self.y2 == other.y2)
        )

    def __ne__(self, other: "Rectangle"):
        return (
            (self.x1 != other.x1)
            or (self.y1 != other.y1)
            or (self.x2 != other.x2)
            or (self.y2 != other.y2)
        )

    def center(self):
        x = (self.x1 + self.x2) / 2
        y = (self.y1 + self.y2) / 2
        return Point(x, y)

    def area(self):
        # Bo wiemy że x1 < x2, y1 < y2
        x = self.x2 - self.x1
        y = self.y2 - self.y1
        return x * y

    def move(self, x, y):
        moving = Point(x, y)
        self.point_1 = self.point_1 + moving
        self.point_2 = self.point_2 + moving
        return f"[{self.point_1}, {self.point_2}]"


    def intersection(self, other: "Rectangle"):
        if (self.point_1.y > other.point_1.y or self.point_2.y < other.point_2.y or self.point_1.x > other.point_1.x or self.point_2.x < other.point_2.x):
            raise ValueError(f"No Intersection Area with {other}")
        new_x_1 = max(self.point_1.x, other.point_1.x)
        new_y_1 = max(self.point_1.y, other.point_1.y)
        new_x_2 = min(self.point_2.x, other.point_2.x)
        new_y_2 = min(self.point_2.y, other.point_2.y)
        return Rectangle(new_x_1,new_y_1,new_x_2,new_y_2)

    def cover(self, other: "Rectangle"):
        new_x_1 = min(self.point_1.x, other.point_1.x)
        new_y_1 = min(self.point_1.y, other.point_1.y)
        new_x_2 = max(self.point_2.x, other.point_2.x)
        new_y_2 = max(self.point_2.y, other.point_2.y)
        return Rectangle(new_x_1,new_y_1,new_x_2,new_y_2)

    # TODO:
    # make4

# rec1 = Rectangle(1, 0, 3, 3)
# rec2 = Rectangle(1, 3, 2, 3)
# print(rec1 == rec2)
# print(rec1.center())
# print(rec1.area())
