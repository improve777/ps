import pytest


@pytest.mark.parametrize(
    'n, array, expected',
    [(5,
      [(11, -15, -15),
       (14, -5, -15),
       (-1, -1, -5),
       (10, -4, -1),
       (19, -4, 19)],
      4
      )]
)
def test(n, array, expected):
    result = solution(n, array)
    assert result == expected


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def calculate_distance(a, b):
    return min(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))


def solution(n, array):
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    edges = []
    target = 2
    for i in range(1, n + 1):
        for j in range(target, n + 1):
            a = array[i - 1]
            b = array[j - 1]
            edges.append((calculate_distance(a, b), i - 1, j - 1))
        target += 1

    edges.sort()
    result = 0

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    return result
