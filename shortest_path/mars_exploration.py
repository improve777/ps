import pytest

import heapq


@pytest.mark.parametrize(
    'n, array, expected',
    [(3,
      [[5, 5, 4],
       [3, 9, 1],
       [3, 2, 7]],
      20),
     ]
)
def test(n, array, expected):
    result = solution(n, array)
    assert result == expected


def solution(n, graph):
    INF = int(1e9)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    return distance[n - 1][n - 1]
