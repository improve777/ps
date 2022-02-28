import pytest


@pytest.mark.parametrize(
    's, expected',
    [('02984', 576),
     ('567', 210),
     ('019900999', 65610)]
)
def test_solve(s, expected):
    result = solve(s)
    assert result == expected


def solve(s):
    array = list(map(int, s))
    result = array[0]

    for i in array[1:]:
        if i <= 1 or result <= 1:
            result += i
        else:
            result *= i

    return result
