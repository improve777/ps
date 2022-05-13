import pytest


@pytest.mark.parametrize(
    'n, m, array, expected',
    [(7, 11,
      [(0, 1, 7),
      (0, 3, 5),
      (1, 2, 8),
      (1, 3, 9),
      (1, 4, 7),
      (2, 4, 5),
      (3, 4, 15),
      (3, 5, 6),
      (4, 5, 8),
      (4, 6, 9),
      (5, 6, 11)],
      51
      )]
)
def test(n, m, array, expected):
    result = solution(n, m, array)
    assert result == expected


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, m, array):
    parent = [0] * (n + 1)
    result = 0

    for i in range(1, n + 1):
        parent[i] = i

    array.sort(key=lambda x: x[2])
    total = 0

    for edge in array:
        a, b, cost = edge
        total += cost

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    return total - result
