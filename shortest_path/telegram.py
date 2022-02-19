import pytest
import heapq


@pytest.mark.parametrize(
    "n, m, c, edges, expected",
    [(3, 2, 1,
      [(1, 2, 4),
       (1, 3, 2)],
      "2 4"
      )]
)
def test_solve(n, m, c, edges, expected):
    graph = [[] for _ in range(n + 1)]
    for x, y, z in edges:
        graph[x].append((y, z))

    result = solve(n, c, graph)
    assert result == expected


def solve(n, c, graph):
    INF = int(1e9)

    distance = [INF] * (n + 1)

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(c)

    count = 0
    max_distance = 0

    for d in distance:
        if d != INF:
            count += 1
            max_distance = max(max_distance, d)

    result = "%d %d" % (count - 1, max_distance)
    return result
