import pytest


# 3 <= n <= 100
# 0 <= k <= 1000
@pytest.mark.parametrize(
    'n, store, expected',
    [(4,
      [1, 3, 1, 5],
      8
    )])
def test_solve(n, store, expected):
    result = solve(n, store)
    assert result == expected


def solve(n, store):
    d = [0] * 100

    d[0] = store[0]
    d[1] = max(store[0], store[1])

    for i in range(2, n):
        d[i] = max(d[i - 1], d[i - 2] + store[i])

    return d[n]
