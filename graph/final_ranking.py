import pytest
from collections import deque


@pytest.mark.parametrize(
    'n, t_array, m, m_array, expected',
    [(5,
      [5, 4, 3, 2, 1],
      2,
      [(2, 4), (3, 4)],
      [5, 3, 2, 4, 1]
      )]
)
def test(n, t_array, m, m_array, expected):
    result = solution(n, t_array, m, m_array)
    assert result == expected


def solution(n, data, m, m_array):
    # 진입차수
    indegree = [0] * (n + 1)
    graph = [[False] * (n + 1) for i in range(n + 1)]

    # 방향 그래프 초기화
    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    # 올해 순위
    for rank in m_array:
        a, b = rank
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # Topology Sort
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True  # 위상 정렬 결과가 오직 하나인지 여부
    cycle = False  # 그래프 내 사이클이 존재하는지 여부

    for i in range(n):
        if len(q) == 0:  # 큐가 비어있다면 사이클 발생
            cycle = True
            break
        if len(q) >= 2:  # 큐의 원소가 2개 이상이라면 결과가 여러개
            certain = False
            break
        now = q.popleft()
        result.append(now)

        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        return "IMPOSSIBLE"
    if not certain:
        return "?"
    return result
