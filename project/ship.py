from typing import List
from settings import LARGE_SHIP_SIZE, MEDIUM_SHIP_SIZE, SMALL_SHIP_SIZE


class Ship:
    def __init__(self, width: int, cords: List[List[int]]):
        self.width = width
        self._destroyed_parts = 0
        self.cords = cords

    def check_if_hit(self, target: List[int]):
        if target in self.cords:
            self._destroyed_parts += 1
            return True
        return False

    def check_if_destroyed(self):
        if self._destroyed_parts == self.width:
            return True
        return False


class SmallShip(Ship):
    def __init__(self, cords: List[List[int]]):
        super().__init__(SMALL_SHIP_SIZE, cords)


class MediumShip(Ship):
    def __init__(self, cords: List[List[int]]):
        super().__init__(MEDIUM_SHIP_SIZE, cords)


class LargeShip(Ship):
    def __init__(self, cords: List[List[int]]):
        super().__init__(LARGE_SHIP_SIZE, cords)
