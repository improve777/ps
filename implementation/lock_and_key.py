import pytest


@pytest.mark.parametrize(
    'key, lock, expected',
    [([[0, 0, 0],
       [1, 0, 0],
       [0, 1, 1]],
      [[1, 1, 1],
       [1, 1, 0],
       [1, 0, 1]],
      True
      )]
)
def test(key, lock, expected):
    result = solution(key, lock)
    assert result == expected


def solution(key, lock):
    m = len(key[0])
    n = len(lock[0])

    total_hole = 0
    for i in range(n):
        total_hole += lock[i].count(0)

    def rotate():
        nonlocal key
        temp = [[0] * m for _ in range(0, m)]

        for i in range(0, m):
            for j in range(0, m):
                temp[i][j] = key[j][m - 1 - i]

        key = temp

    def match(x, y):
        count = 0

        for i in range(0, m):
            for j in range(0, m):
                if not (0 <= i + x < n and 0 <= j + y < n):
                    continue

                if key[i][j] == lock[i + x][j + y]:
                    return False

                if key[i][j] == 1:
                    count += 1

        if count == total_hole:
            return True
        else:
            return False

    # 회전
    for r in range(0, 4):
        rotate()
        for x in range(-(m - 1), n):
            for y in range(-(m - 1), n):
                if match(x, y):
                    return True

    return False
