# 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우
if __name__ == '__main__':
    INF = int(1e9)

    # 노드, 간선
    n = 4
    m = 7

    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    graph[1][2] = 4
    graph[1][4] = 6
    graph[2][1] = 3
    graph[2][3] = 7
    graph[3][1] = 5
    graph[3][4] = 4
    graph[4][3] = 2

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == INF:
                print("INFINITY", end=" ")
            else:
                print(graph[a][b], end=" ")
        print()

