from points import Point

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.point_1 = Point(x1, y1)
        self.point_2 = Point(x2, y2)

    def __str__(self):
        return f"[{str(self.point_1)}, {str(self.point_2)}]"

    def __repr__(self):
        return f"Rectangle({self.point_1.x}, {self.point_1.y}, {self.point_2.x}, {self.point_2.y})"

    def __eq__(self, other: "Rectangle"):
        return (
            (self.point_1.x == other.point_1.x)
            and (self.point_1.y == other.point_1.y)
            and (self.point_2.x == other.point_2.x)
            and (self.point_2.y == other.point_2.y)
        )

    def __ne__(self, other: "Rectangle"):
        return (
            (self.point_1.x != other.point_1.x)
            or (self.point_1.y != other.point_1.y)
            or (self.point_2.x != other.point_2.x)
            or (self.point_2.y != other.point_2.y)
        )

    def center(self):
        x = (self.point_1.x + self.point_2.x) / 2
        y = (self.point_1.y + self.point_2.y) / 2
        return Point(x, y)

    def area(self):
        # Bo wiemy że x1 < x2, y1 < y2
        x = self.point_2.x - self.point_1.x
        y = self.point_2.y - self.point_1.y
        return x * y

    def move(self, x, y):
        moving = Point(x, y)
        point_1 = self.point_1 + moving
        point_2 = self.point_2 + moving
        return Rectangle(point_1.x, point_1.y,  point_2.x, point_2.y)