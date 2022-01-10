import pytest


# 여행가가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램 작성

@pytest.mark.parametrize("n, plans, expected", [(5, "R R R U D D", "3 4")])
def test_solve(n, plans, expected):
    result = solve1(n, plans)
    assert result == expected


def solve1(n, plans):
    result = (1, 1)

    directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

    for plan in plans.split():
        move = directions.get(plan)
        new = (result[0] + move[0], result[1] + move[1])
        if new[0] < 1 or new[0] > n or new[1] < 1 or new[1] > n:
            continue
        result = new

    return str(result[0]) + " " + str(result[1])


def solve2(n, plans):
    nx, ny = 0, 0
    x, y = 1, 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for plan in plans.split():
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny

    return str(x) + ' ' + str(y)

