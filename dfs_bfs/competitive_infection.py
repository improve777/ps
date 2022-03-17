import pytest
import heapq
from collections import deque


@pytest.mark.parametrize(
    'n, k, array, expected',
    [(3, 3,
      [[1, 0, 2],
       [0, 0, 0],
       [3, 0, 0],
       [2, 3, 2]],
      3),
     (3, 3,
      [[1, 0, 2],
       [0, 0, 0],
       [3, 0, 0],
       [1, 2, 2]],
      0),
     ]
)
def test(n, k, array, expected):
    result = solution2(n, k, array)
    assert result == expected


def solution(n, k, array):
    row = array[n]
    s, x, y = row[0], row[1], row[2]
    array = array[:n]

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    second = 0

    def infect(virus, x, y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == 0:
                array[nx][ny] = virus

    q = []

    while second < s:
        second += 1

        for i in range(n):
            for j in range(n):
                virus = array[i][j]
                if virus != 0:
                    heapq.heappush(q, (virus, i, j))

        for (virus, i, j) in q:
            infect(virus, i, j)

    return array[x - 1][y - 1]


def solution2(n, k, array):
    row = array[n]
    target_s, target_x, target_y = row[0], row[1], row[2]
    graph = array[:n]

    data = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                data.append((graph[i][j], 0, i, j))

    data.sort()
    q = deque(data)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        virus, s, x, y = q.popleft()
        if s == target_s:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus
                    q.append((virus, s + 1, nx, ny))

    return graph[target_x - 1][target_y - 1]
