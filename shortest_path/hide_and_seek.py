import pytest

import heapq


@pytest.mark.parametrize(
    'n, m, array, expected',
    [(6, 7,
      [(3, 6),
       (4, 3),
       (3, 2),
       (1, 3),
       (1, 2),
       (2, 4),
       (5, 2)],
      [4, 2, 3])]
)
def test(n, m, array, expected):
    result = solution(n, m, array)
    assert result == expected


def solution(n, m, array):
    INF = int(1e9)

    start = 1

    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for i in range(m):
        a, b = array[i]
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for nodes in graph[now]:
                cost = dist + nodes[1]
                if cost < distance[nodes[0]]:
                    distance[nodes[0]] = cost
                    heapq.heappush(q, (cost, nodes[0]))

    dijkstra(start)

    max_node = 0
    max_distance = 0
    result = []

    for i in range(1, n + 1):
        if max_distance < distance[i]:
            max_node = i
            max_distance = distance[i]
            result = [max_node]
        elif max_distance == distance[i]:
            result.append(i)

    return [max_node, max_distance, len(result)]
