import pytest


@pytest.mark.parametrize("n,expected", [(1260, 6)])
def test_solve(n, expected):
    count = 0
    coin_types = [500, 100, 50, 10]

    for coin in coin_types:
        count += n // coin
        n %= coin

    assert count == expected
