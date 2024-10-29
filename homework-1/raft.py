from enum import Enum


class Direction(Enum):
    N = 0,
    NE = 1,
    E = 2,
    SE = 3,
    S = 4,
    SW = 5,
    W = 6,
    NW = 7


def get_nearest_side_or_corner(x1: int, y1: int, x2: int, y2: int, x: int, y: int) -> Direction:
    if y >= y2:
        if x <= x1:
            return Direction.NW
        elif x >= x2:
            return Direction.NE
        return Direction.N
    elif y <= y1:
        if x <= x1:
            return Direction.SW
        elif x >= x2:
            return Direction.SE
        return Direction.S
    if x <= x1:
        return Direction.W
    return Direction.E


if __name__ == '__main__':
    print(get_nearest_side_or_corner(x1=int(input()), y1=int(input()),
                                     x2=int(input()), y2=int(input()),
                                     x=int(input()), y=int(input())).name)

