import math


class Position:
    x: float
    y: float

    def __init__(self, x: float, y: float, polar: bool = False):
        if polar:
            self.x = x * math.cos(y)
            self.y = x * math.sin(y)
        else:
            self.x = x
            self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __getitem__(self, item: int) -> float:
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        else:
            raise IndexError("Index out of range")
