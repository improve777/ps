import pytest


# 1 <= n <= 1000
# 1 <= m <= 10000
@pytest.mark.parametrize(
    'n, m, currency, expected',
    [(2, 15,
      [2, 3],
      5)]
)
def test_solve(n, m, currency, expected):
    result = solve(n, m, currency)
    assert result == expected


def solve(n, m, currency):
    d = [10001] * (m + 1)

    d[0] = 0
    for i in range(n):
        for j in range(currency[i], m + 1):
            if d[j - currency[i]] != 10001:
                d[j] = min(d[j], d[j - currency[i]] + 1)

    if d[m] == 10001:
        return -1
    else:
        return d[m]
