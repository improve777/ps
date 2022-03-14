import pytest
import heapq


@pytest.mark.parametrize(
    'n, m, k, x, array, expected',
    [(4, 4, 2, 1,
      [(1, 2), (1, 3), (2, 3), (2, 4)],
      "4"),
     (4, 3, 2, 1,
      [(1, 2), (1, 3), (1, 4)],
      "-1"),
     (4, 4, 1, 1,
      [(1, 2), (1, 3), (2, 3), (2, 4)],
      "2\n3"),
     ]
)
def test(n, m, k, x, array, expected):
    result = solution(n, m, k, x, array)
    assert result == expected


# 도시 개수, 도로 개수, 거리 정보, 출발 도시
def solution(n, m, k, x, array):
    distance = [int(1e9)] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for a, b in array:
        graph[a].append(b)

    def dijkstra(x):
        q = []
        heapq.heappush(q, (0, x))
        distance[x] = 0

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for b in graph[now]:
                cost = dist + 1
                if cost < distance[b]:
                    distance[b] = cost
                    heapq.heappush(q, (cost, b))

    dijkstra(x)

    result = ''
    for i in range(0, len(distance)):
        dist = distance[i]
        if dist == k:
            result += str(i) + '\n'

    if result == '':
        return '-1'

    return result[:len(result) - 1]
