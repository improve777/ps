from collections import deque

import pytest

# 시작 (1,1), 출구 (n, m)
# 괴물을 피해 탈출하기 위해 움직여야 하는 최소 칸의 개수
@pytest.mark.parametrize(
    "n, m, field, expected",
    [(5, 6,
      ["101010",
       "111111",
       "000001",
       "111111",
       "111111"],
      10)]
)
def test_solve(n, m, field, expected):
    result = solve(n, m, field)
    assert result == expected


def solve(n, m, field):
    maze = [list(map(int, row)) for row in field]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if maze[nx][ny] == 0:
                    continue
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx, ny))
        return maze[n - 1][m - 1]

    return bfs(0, 0)

