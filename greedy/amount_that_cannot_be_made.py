import pytest


@pytest.mark.parametrize(
    'n, array, expected',
    [(5, [3, 2, 1, 1, 9], 8),
     (3, [3, 5, 7], 1),
     (4, [1, 2, 3, 8], 7),
     (4, [1, 2, 2, 8], 6)]
)
def test_solve(n, array, expected):
    result = solve(n, array)
    assert result == expected


def solve(n, array):
    array.sort()

    target = 1
    for x in array:
        if target < x:
            break
        target += x

    return target
