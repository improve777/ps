import heapq

if __name__ == '__main__':
    INF = int(1e9)

    n, m = 6, 11
    start = 1
    graph = [[] for i in range(n + 1)]
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)

    graph[1].append((2, 2))
    graph[1].append((3, 5))
    graph[1].append((4, 1))
    graph[2].append((3, 3))
    graph[2].append((4, 2))
    graph[3].append((2, 3))
    graph[3].append((6, 5))
    graph[4].append((3, 3))
    graph[4].append((5, 1))
    graph[5].append((3, 1))
    graph[5].append((6, 2))

    # O(ElogV)
    def dijkstra(start):
        q = []
        # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
        heapq.heappush(q, (0, start))
        distance[start] = 0

        # 큐가 비어 있지 않다면
        while q:
            # 가장 최단 거리가 짧ㅇ느 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(q)
            # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            if distance[now] < dist:
                continue
            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for i in graph[now]:
                cost = dist + i[1]
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(start)

    for i in range(1, n + 1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])
