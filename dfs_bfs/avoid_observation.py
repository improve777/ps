import pytest
from itertools import combinations


@pytest.mark.parametrize(
    'n, array, expected',
    [(5,
      [['X', 'S', 'X', 'X', 'T'],
       ['T', 'X', 'S', 'X', 'X'],
       ['X', 'X', 'X', 'X', 'X'],
       ['X', 'T', 'X', 'X', 'X'],
       ['X', 'X', 'T', 'X', 'X']],
      'YES'
      ),
     (4,
      [['S', 'S', 'S', 'T'],
       ['X', 'X', 'X', 'X'],
       ['X', 'X', 'X', 'X'],
       ['T', 'T', 'T', 'X']],
      'NO'
      )
     ]
)
def test(n, array, expected):
    result = solution2(n, array)
    assert result == expected


def solution(n, array):
    avoid = []

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    teachers = []
    for i in range(n):
        for j in range(n):
            if array[i][j] == 'T':
                teachers.append((i, j))

    def avoid_all_teachers():
        for (x, y) in teachers:
            # 교사가 학생 감시를 했을 경우
            if check_observation(x, y):
                return False
        return True

    # 학생 감시 성공 여부
    def check_observation(x, y):
        for j in range(4):
            for i in range(1, n):
                nx = x + dx[j] * i
                ny = y + dy[j] * i

                if 0 <= nx < n and 0 <= ny < n:
                    if array[nx][ny] == 'O':
                        break
                    elif array[nx][ny] == 'S':
                        return True
        return False

    def dfs(count, array):
        if count == 3:
            avoid.append(avoid_all_teachers())
        else:
            for i in range(n):
                for j in range(n):
                    if array[i][j] == 'X':
                        array[i][j] = 'O'
                        dfs(count + 1, array)
                        array[i][j] = 'X'

    dfs(0, array)

    for b in avoid:
        if b:
            return 'YES'

    return 'NO'


def solution2(n, board):
    teachers = []
    spaces = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'T':
                teachers.append((i, j))
            if board[i][j] == 'X':
                spaces.append((i, j))

    def watch(x, y, direction):
        if direction == 0:
            while y >= 0:
                if board[x][y] == 'S':
                    return True
                if board[x][y] == 'O':
                    return False
                y -= 1
        if direction == 1:
            while y < n:
                if board[x][y] == 'S':
                    return True
                if board[x][y] == 'O':
                    return False
                y += 1
        if direction == 2:
            while x >= 0:
                if board[x][y] == 'S':
                    return True
                if board[x][y] == 'O':
                    return False
                x -= 1
        if direction == 3:
            while x < n:
                if board[x][y] == 'S':
                    return True
                if board[x][y] == 'O':
                    return False
                x += 1
        return False

    def process():
        for x, y in teachers:
            for i in range(4):
                if watch(x, y, i):
                    return True
        return False

    find = False

    for data in combinations(spaces, 3):
        for x, y in data:
            board[x][y] = 'O'
        if not process():
            find = True
            break
        for x, y in data:
            board[x][y] = 'X'

    return 'YES' if find else 'NO'
