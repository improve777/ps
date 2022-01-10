import pytest


# 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.

@pytest.mark.parametrize(
    "n, m, info, map, expected",
    [(4, 4,
      "1 1 0",
      [[1, 1, 1, 1],
       [1, 0, 0, 1],
       [1, 1, 0, 1],
       [1, 1, 1, 1]],
      3),
     (4, 4,
      "0 0 0",
      [[0, 0, 1, 1],
       [1, 0, 0, 1],
       [1, 1, 0, 1],
       [1, 1, 1, 1]],
      5)
     ])
def test_solve(n, m, info, map, expected):
    result = solve1(n, m, info, map)
    assert result == expected


def solve1(n, m, info, field):
    d = [[0] * m for _ in range(n)]
    x, y, direction = map(int, info.split())

    d[x][y] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def turn_left():
        nonlocal direction
        direction -= 1
        if direction == -1:
            direction = 3

    count = 1
    turn_time = 0
    while True:
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 이동
        if d[nx][ny] == 0 and field[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        # 바다인 경우 회전
        else:
            turn_time += 1
        # 네 방향 모두 갈 수 없는 경우
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            if field[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0

    return count
