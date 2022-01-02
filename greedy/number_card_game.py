import pytest


# 행, 열, 배열
@pytest.mark.parametrize(
    "n,m,data,expected",
    [(2, 4, [7, 3, 1, 8, 3, 3, 3, 4], 3),
     (3, 3, [3, 1, 2, 4, 1, 4, 2, 2, 2], 2)]
)
def test_solve(n, m, data, expected):
    num = solve2(n, m, data)
    assert num == expected


def solve1(n, m, data):
    num = 0

    for i in range(n):
        row_min = 10001
        for j in range(m):
            index = j + (i * m)
            if row_min > data[index]:
                row_min = data[index]
        if num < row_min:
            num = row_min

    return num


def solve2(n, m, data):
    num = 0

    for i in range(n):
        row_min = min(data[(i * m):m + (i * m)])
        num = max(num, row_min)

    return num
