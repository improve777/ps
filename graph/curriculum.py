import pytest
from collections import deque
import copy


@pytest.mark.parametrize(
    'n, lectures, expected',
    [(5,
      [(10, -1),
       (10, 1, -1),
       (4, 1, -1),
       (4, 3, 1, -1),
       (3, 3, -1)],
      "10\n20\n14\n18\n17\n"
      )]
)
def test_solve(n, lectures, expected):
    result = solve(n, lectures)
    assert result == expected


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def solve(n, lectures):
    # 진입차수
    indegree = [0] * (n + 1)
    # 간선 정보
    graph = [[] for _ in range(n + 1)]
    # 강의 시간
    time = [0] * (n + 1)

    # 방향 그래프의 모든 간선 정보를 입력받기
    for i in range(1, n + 1):
        lecture = lectures[i - 1]
        time[i] = lecture[0]
        for x in lecture[1:-1]:
            indegree[i] += 1
            graph[x].append(i)

    def topology_sort():
        result = copy.deepcopy(time)
        q = deque()

        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)

        while q:
            now = q.popleft()
            # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            for i in graph[now]:
                result[i] = max(result[i], result[now] + time[i])
                indegree[i] -= 1
                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[i] == 0:
                    q.append(i)

        return result[1:]

    result = ""
    for x in topology_sort():
        result += str(x) + "\n"

    return result
