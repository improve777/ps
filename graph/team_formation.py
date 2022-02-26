import pytest


@pytest.mark.parametrize(
    'n, m, array, expected',
    [(7, 8,
      [(0, 1, 3),
       (1, 1, 7),
       (0, 7, 6),
       (1, 7, 1),
       (0, 3, 7),
       (0, 4, 2),
       (0, 1, 1),
       (1, 1, 1),
       ],
      "NO\nNO\nYES\n"
      )]
)
def test_solve(n, m, array, expected):
    result = solve(n, m, array)
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


def solve(n, m, array):
    result = ""
    parent = [0] * (n + 1)

    for i in range(n):
        parent[i] = i

    for i in range(m):
        operation, a, b = array[i]

        if operation == 0:
            union_parent(parent, a, b)
        else:
            if find_parent(parent, a) == find_parent(parent, b):
                result += "YES\n"
            else:
                result += "NO\n"

    return result
