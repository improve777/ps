import pytest


@pytest.mark.parametrize(
    'n, m, array, expected',
    [(6, 6,
      [(1, 5),
       (3, 4),
       (4, 2),
       (4, 6),
       (5, 2),
       (5, 4)],
      1)]
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
        a, b = array[i]
        graph[a][b] = 1

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    result = 0
    for i in range(1, n + 1):
        count = 0
        # 모든 노드에 도달이 가능한지 여부 -> 순위를 알 수 있음.
        for j in range(1, n + 1):
            if graph[i][j] != INF or graph[j][i] != INF:
                count += 1
        if count == n:
            result += 1

    return result
