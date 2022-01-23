import pytest


@pytest.mark.parametrize(
    "n, m, field, expected",
    [(4, 5,
      ["00110",
       "00011",
       "11111",
       "00000"],
      3
      )]
)
def test_solve(n, m, field, expected):
    result = solve1(n, m, field)
    assert result == expected


def solve1(n, m, graph):
    graph = list(map(list, graph))
    graph = [list(map(int, row)) for row in graph]

    count = 0

    def dfs(x, y):
        # 종료 조건
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False

    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                count += 1

    return count
