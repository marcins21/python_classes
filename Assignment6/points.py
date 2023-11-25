import math


class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other: "Point") -> bool:
        return (other.x == self.x) and (other.y == self.y)

    def __ne__(self, other: "Point") -> bool:
        return (other.x != self.x) or (other.y != self.y)

    def __add__(self, other: "Point") -> "Point":
        return Point((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: "Point") -> "Point":
        return Point((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: "Point") -> float:
        return (self.x * other.x) + (self.y * other.y)

    def length(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __cross__(self, other: "Point") -> int:
        return self.x * other.y - self.y * other.x

    def __hash__(self):
        return hash((self.x, self.y))
