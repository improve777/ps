import pytest


@pytest.mark.parametrize(
    'n, m, field, expected',
    [(7, 7,
      [[2, 0, 0, 0, 1, 1, 0],
       [0, 0, 1, 0, 1, 2, 0],
       [0, 1, 1, 0, 1, 0, 0],
       [0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 1],
       [0, 1, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0],
       ],
      27),
     ]
)
def test(n, m, field, expected):
    result = solution(n, m, field)
    assert result == expected


def solution(n, m, field):
    temp = [[0] * m for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    result = 0

    # 재귀적으로 주변에 바이러스 전파
    def virus(x, y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    virus(nx, ny)

    # 스코어 계산
    def get_score():
        score = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    score += 1
        return score

    def dfs(count):
        nonlocal result
        if count == 3:
            for i in range(n):
                for j in range(m):
                    temp[i][j] = field[i][j]
            # 각 바이러스의 위치에서 전파 진행
            for i in range(n):
                for j in range(m):
                    if temp[i][j] == 2:
                        virus(i, j)
            # 안전 영역의 최댓값 계산
            result = max(result, get_score())
            return
        # 빈 공간에 울타리 설치
        for i in range(n):
            for j in range(m):
                if field[i][j] == 0:
                    field[i][j] = 1
                    count += 1
                    dfs(count)
                    field[i][j] = 0
                    count -= 1

    dfs(0)
    return result
