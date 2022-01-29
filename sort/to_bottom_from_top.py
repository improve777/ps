import pytest


@pytest.mark.parametrize(
    'count, inputs, expected',
    [(3,
      [15, 27, 12],
      [27, 15, 12]),
     (4,
      [4, 8, 10, 2],
      [10, 8, 4, 2])
     ])
def test_solve(count, inputs, expected):
    result = solve(inputs)
    assert result == expected


def solve(inputs):
    return sorted(inputs, reverse=True)
