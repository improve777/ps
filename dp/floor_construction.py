import pytest


# 1 <= n <= 1000
@pytest.mark.parametrize(
    'n, expected',
    ([3, 5])
)
def test_solve(n, expected):
    result = solve(n)
    assert result == expected


def solve(n):
    d = [0] * 1001

    d[1] = 1
    d[2] = 3

    for i in range(3, n):
        d[i] = (d[i - 1] + d[i - 2] * 2) % 796796

    return d[n]
