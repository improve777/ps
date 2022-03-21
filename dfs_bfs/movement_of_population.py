import pytest
from collections import deque


@pytest.mark.parametrize(
    'n, l, r, array, expected',
    [
        (2, 20, 50,
         [[50, 30],
          [20, 40]],
         1),
        (2, 20, 50,
         [[50, 30],
          [30, 40]],
         1),
        (3, 5, 10,
         [[10, 15, 20],
          [20, 30, 25],
          [40, 22, 10]],
         2),
        (4, 10, 50,
         [[10, 100, 20, 90],
          [80, 100, 60, 70],
          [70, 20, 30, 40],
          [50, 20, 100, 10]],
         3),
    ]
)
def test(n, l, r, array, expected):
    result = solution(n, l, r, array)
    assert result == expected


def solution(n, l, r, array):
    unions = []

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def make_union(x, y, union):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if added[nx][ny] == 1:  # 이미 연합을 이뤘다면
                    continue

                if l <= abs(array[x][y] - array[nx][ny]) <= r:  # 인구차이
                    added[nx][ny] = 1
                    union.append((nx, ny))
                    make_union(nx, ny, union)

    def check_unions():
        for i in range(n):
            for j in range(n):
                if added[i][j] == 0:  # 연합이 아니라면
                    union = [(i, j)]
                    added[i][j] = 1
                    make_union(i, j, union)
                    if len(union) > 1:
                        unions.append(union)

    count = 0

    unions = []
    added = [[0] * n for _ in range(n)]
    check_unions()

    while len(unions) != 0:
        count += 1

        # 인구 이동
        for union in unions:
            sum = 0
            for (x, y) in union:
                sum += array[x][y]
            population = sum // len(union)

            for (x, y) in union:
                array[x][y] = population

        # 다시 연합 체크
        unions = []
        added = [[0] * n for _ in range(n)]
        check_unions()

    return count


def solution2(n, l, r, graph):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    total_count = 0

    def process(x, y, index):
        united = []
        united.append((x, y))

        q = deque()
        q.append((x, y))
        union[x][y] = index

        summary = graph[x][y]  # 현재 연합의 전체 인구수
        count = 1

        while q:
            x, y = q.popleft()
            #
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                    if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                        q.append((nx, ny))
                        union[nx][ny] = index
                        summary += graph[nx][ny]
                        count += 1
                        united.append((nx, ny))

        for i, j in united:
            graph[i][j] = summary // count

    while True:
        # 연합 참가 여부 체크
        union = [[-1] * n for _ in range(n)]
        # 어느 연합인지
        index = 0
        for i in range(n):
            for j in range(n):
                if union[i][j] == -1:
                    process(i, j, index)
                    index += 1

        # 모든 인구 이동이 끝난 경우 -> 모두 다 연합을 이룰 수 없을 때
        if index == n * n:
            break
        total_count += 1

    return total_count
