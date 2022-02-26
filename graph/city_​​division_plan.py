import pytest


@pytest.mark.parametrize(
    'n, m, array, expected',
    [(7, 12,
      [(1, 2, 3),
       (1, 3, 2),
       (3, 2, 1),
       (2, 5, 2),
       (3, 4, 4),
       (7, 3, 6),
       (5, 1, 5),
       (1, 6, 2),
       (6, 4, 1),
       (6, 5, 3),
       (4, 5, 3),
       (6, 7, 4)],
      8
      )]
)
def test_solve(n, m, array, expected):
    result = solve(n, m, array)
    assert result == expected


def solve(n, m, array):
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    array.sort(key=lambda x: x[2])

    distance = 0
    last = 0

    for i in range(m):
        a, b, cost = array[i]
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            distance += cost
            last = cost

    return distance - last


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
