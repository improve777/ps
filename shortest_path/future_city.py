import pytest


@pytest.mark.parametrize(
    "n, m, edges, x, k, expected",
    [(5, 7,
      [(1, 2),
       (1, 3),
       (1, 4),
       (2, 4),
       (3, 4),
       (3, 5),
       (4, 5),
       ],
      4, 5,
      3,
      ),
     (4, 2,
      [(1, 3),
       (2, 4),
       ],
      3, 4,
      -1
      )
     ]
)
def test_solve(n, m, edges, x, k, expected):
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    for i in range(m):
        a, b = edges[i]
        graph[a][b] = 1
        graph[b][a] = 1

    result = solve(n, x, k, graph)
    assert result == expected


def solve(n, x, k, graph):
    INF = int(1e9)

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    distance = graph[1][k] + graph[k][x]

    return distance if distance < INF else -1
