import pytest


@pytest.mark.parametrize(
    't, size, fields, expected',
    [(2,
      [(3, 4), (4, 4)],
      [
          [[1, 3, 3, 2],
           [2, 1, 4, 1],
           [0, 6, 4, 7]],

          [[1, 3, 1, 5],
           [2, 2, 4, 1],
           [5, 0, 2, 3],
           [0, 6, 1, 2]]
      ],
      [19, 16]
      )]
)
def test(t, size, fields, expected):
    result = solution2(t, size, fields)
    assert result == expected


def solution(t, size, fields):
    result = []

    for i in range(t):
        n, m = size[i]
        field = fields[i]

        gold = max_gold(n, m, field)
        result.append(gold)

    return result


def max_gold(n, m, field):
    dx = [-1, 0, 1]
    max_g = -1

    def dfs(x, y, gold):
        nonlocal max_g
        if y == m - 1:
            max_g = max(max_g, gold)
        else:
            for i in range(3):
                mx = x + dx[i]
                my = y + 1

                if mx < n and 0 <= my < m:
                    dfs(mx, my, gold + field[mx][my])

    for x in range(n):
        dfs(x, 0, field[x][0])

    return max_g


def solution2(t, size, fields):
    results = []

    for tc in range(t):
        n, m = size[tc]
        field = fields[tc]

        for j in range(1, m):
            for i in range(n):
                left_j = j - 1
                # 왼쪽 위에서 오는 경우
                if i == 0:
                    left_up = 0
                else:
                    left_up = field[i - 1][left_j]
                # 왼쪽 아래에서 오는 경우
                if i == n - 1:
                    left_down = 0
                else:
                    left_down = field[i + 1][left_j]
                # 왼쪽에서 오는 경우
                left = field[i][left_j]

                field[i][j] = field[i][j] + max(left_up, left_down, left)

        result = 0
        for i in range(n):
            result = max(result, field[i][m - 1])

        results.append(result)

    return results
