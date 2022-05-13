import pytest


@pytest.mark.parametrize(
    'n, m, array, plan, expected',
    [(5, 4,
      [[0, 1, 0, 1, 1],
       [1, 0, 1, 1, 0],
       [0, 1, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 0, 0, 0, 0]],
      [2, 3, 4, 3],
      "YES"
      )]
)
def test(n, m, array, plan, expected):
    result = solution(n, m, array, plan)
    assert result == expected


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, m, array, plan):
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    for i in range(n):
        for j in range(n):
            if array[i][j] == 1:
                union_parent(parent, i + 1, j + 1)

    result = "YES"

    for i in range(m - 1):
        if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
            result = "NO"

    return result
