import pytest


@pytest.mark.parametrize(
    'n, m, array, expected',
    [(
        5, 14,
        [[1, 2, 2],
         [1, 3, 3],
         [1, 4, 1],
         [1, 5, 10],
         [2, 4, 2],
         [3, 4, 1],
         [3, 5, 1],
         [4, 5, 3],
         [3, 5, 10],
         [3, 1, 8],
         [1, 4, 2],
         [5, 1, 7],
         [3, 4, 2],
         [5, 2, 4]],
        [[0, 2, 3, 1, 4],
         [12, 0, 15, 2, 5],
         [8, 5, 0, 1, 1],
         [10, 7, 13, 0, 3],
         [7, 4, 10, 6, 0]]
    )]
)
def test(n, m, array, expected):
    result = solution(n, m, array)
    assert result == expected


def solution(n, m, array):
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    for i in range(m):
        a, b, c = array[i]
        if c < graph[a][b]:
            graph[a][b] = c

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    result = []

    for a in range(1, n + 1):
        sub = []
        for b in range(1, n + 1):
            if graph[a][b] == INF:
                sub.append(0)
            else:
                sub.append(graph[a][b])
        result.append(sub)

    return result
