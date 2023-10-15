from Assignment6.points import Point


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.point_1 = Point(x1, y1)
        self.point_2 = Point(x2, y2)

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

    # TODO:
    def move(self, x, y):
        pass  # przesunięcie o (x, y)

    def intersection(self, other):
        pass  # część wspólna prostokątów

    def cover(self, other):
        pass  # prostąkąt nakrywający oba

    def make4(self):
        pass  # zwraca krotkę czterech mniejszych


rec1 = Rectangle(1, 0, 3, 3)
rec2 = Rectangle(1, 3, 2, 3)
print(rec1 == rec2)
print(rec1.center())
print(rec1.area())
