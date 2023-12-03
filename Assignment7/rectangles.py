from points import Point


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.point_1 = Point(x1, y1)
        self.point_2 = Point(x2, y2)

    def __str__(self) -> str:
        return f"[{str(self.point_1)}, {str(self.point_2)}]"

    def __repr__(self) -> str:
        return f"Rectangle({self.point_1.x}, {self.point_1.y}, {self.point_2.x}, {self.point_2.y})"

    def __eq__(self, other: "Rectangle") -> bool:
        return (
            (self.point_1.x == other.point_1.x)
            and (self.point_1.y == other.point_1.y)
            and (self.point_2.x == other.point_2.x)
            and (self.point_2.y == other.point_2.y)
        )

    def __ne__(self, other: "Rectangle") -> bool:
        return (
            (self.point_1.x != other.point_1.x)
            or (self.point_1.y != other.point_1.y)
            or (self.point_2.x != other.point_2.x)
            or (self.point_2.y != other.point_2.y)
        )

    def center(self) -> "Point":
        x = (self.point_1.x + self.point_2.x) / 2
        y = (self.point_1.y + self.point_2.y) / 2
        return Point(x, y)

    def area(self) -> float:
        # Bo wiemy że x1 < x2, y1 < y2
        x = self.point_2.x - self.point_1.x
        y = self.point_2.y - self.point_1.y
        return x * y

    def move(self, x, y) -> "Rectangle":
        moving = Point(x, y)
        point_1 = self.point_1 + moving
        point_2 = self.point_2 + moving
        return Rectangle(point_1.x, point_1.y, point_2.x, point_2.y)

    def intersection(self, other: "Rectangle"):
        if (
            self.point_1.y > other.point_1.y
            or self.point_2.y < other.point_2.y
            or self.point_1.x > other.point_1.x
            or self.point_2.x < other.point_2.x
        ):
            raise ValueError(f"No Intersection Area with {other}")
        new_x_1 = max(self.point_1.x, other.point_1.x)
        new_y_1 = max(self.point_1.y, other.point_1.y)
        new_x_2 = min(self.point_2.x, other.point_2.x)
        new_y_2 = min(self.point_2.y, other.point_2.y)
        return Rectangle(new_x_1, new_y_1, new_x_2, new_y_2)

    def cover(self, other: "Rectangle"):
        new_x_1 = min(self.point_1.x, other.point_1.x)
        new_y_1 = min(self.point_1.y, other.point_1.y)
        new_x_2 = max(self.point_2.x, other.point_2.x)
        new_y_2 = max(self.point_2.y, other.point_2.y)
        return Rectangle(new_x_1, new_y_1, new_x_2, new_y_2)


    def make4(self):
        center = self.center()
        x_ab = Point(center.x, self.point_1.y)
        x_dc = Point(center.x, self.point_2.y)
        y_da = Point(self.point_1.x, center.y)
        y_cb = Point(self.point_2.x, center.y)
        return (Rectangle(self.point_1.x,self.point_1.y,center.x, center.y),
                Rectangle(y_da.x, y_da.y, x_dc.x, x_dc.y),
                Rectangle(center.x, center.y, self.point_2.x, self.point_2.y),
                Rectangle(x_ab.x, x_ab.y, y_cb.x, y_cb.y))






rec1 = Rectangle(1, 0, 3, 3)
print(rec1.make4())

# rec2 = Rectangle(1, 3, 2, 3)
# print(rec1 == rec2)
# print(rec1.center())
# print(rec1.area())
