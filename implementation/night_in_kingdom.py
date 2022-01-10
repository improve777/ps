import pytest


# 나이트가 이동할 수 있는 위치의 경우의 수 구하기

@pytest.mark.parametrize("coordinate, expected", [("a1", 2), ("d5", 8)])
def test_solve(coordinate, expected):
    result = solve1(coordinate)
    assert result == expected


def solve1(coordinate):
    count = 0

    keys = ["a", "b", "c", "d", "e", "f", "g", "h"]

    x, y = keys.index(coordinate[0]) + 1, int(coordinate[1])

    movement = [(-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2), (-2, -1), (-2, 1)]

    for move in movement:
        dx, dy = x + move[0], y + move[1]
        if dx < 1 or dy < 1 or dx > 8 or dy > 8:
            continue
        count += 1

    return count


def solve2(coordinate):
    row = int(coordinate[1])
    # ord : 문자의 유니코드 값
    column = int(ord(coordinate[0])) - int(ord('a')) + 1

    steps = [(-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2), (-2, -1), (-2, 1)]

    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]
        if 1 <= next_row <= 8 and 1 <= next_column <= 8:
            result += 1

    return result

