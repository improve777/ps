import pytest
from itertools import combinations


@pytest.mark.parametrize(
    'n, m, city, expected',
    [(5, 3,
      [[0, 0, 1, 0, 0],
       [0, 0, 2, 0, 1],
       [0, 1, 2, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 0, 0, 2]],
      5),
     (5, 2,
      [[0, 2, 0, 1, 0],
       [1, 0, 1, 0, 0],
       [0, 0, 0, 0, 0],
       [2, 0, 0, 1, 1],
       [2, 2, 0, 1, 2]],
      10),
     (5, 1,
      [[1, 2, 0, 0, 0],
       [1, 2, 0, 0, 0],
       [1, 2, 0, 0, 0],
       [1, 2, 0, 0, 0],
       [1, 2, 0, 0, 0]],
      11)
     ]
)
def test(n, m, city, expected):
    result = solution(n, m, city)
    assert result == expected


def solution(n, m, city):
    houses = []
    chickens = []

    for x in range(n):
        for y in range(n):
            value = city[x][y]
            if value == 1:
                houses.append((x, y))
            elif value == 2:
                chickens.append((x, y))

    candidates = list(combinations(chickens, m))

    def get_sum(candidate):
        result = 0

        for hx, hy in houses:
            temp = 1e9
            for cx, cy in candidate:
                temp = min(temp, abs(hx - cx) + abs(hy - cy))
            result += temp

        return result

    result = 1e9
    for candidate in candidates:
        result = min(result, get_sum(candidate))

    return result
