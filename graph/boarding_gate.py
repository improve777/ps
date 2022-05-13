import pytest


@pytest.mark.parametrize(
    'g, p, array, expected',
    [(4, 3, [4, 1, 1], 2)]
)
def test(g, p, array, expected):
    result = solution(g, p, array)
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


def solution(g, p, array):
    parent = [0] + [i for i in range(1, g + 1)]

    result = 0
    for i in array:
        data = find_parent(parent, i)
        if data == 0:
            break
        union_parent(parent, data, data - 1)
        result += 1

    return result
