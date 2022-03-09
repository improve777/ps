import pytest


@pytest.mark.parametrize(
    'n, k, apples, l, directions, expected',
    [(6, 3,
      [(3, 4), (2, 5), (5, 3)],
      3,
      [(3, 'D'), (15, 'L'), (17, 'D')],
      9),
     (10, 4,
      [(1, 2), (1, 3), (1, 4), (1, 5)],
      4,
      [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')],
      21),
     (10, 5,
      [(1, 5), (1, 3), (1, 2), (1, 6), (1, 7)],
      4,
      [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')],
      13)
     ]
)
def test(n, k, apples, l, directions, expected):
    result = solution(n, k, apples, l, directions)
    assert result == expected


def scan(map):
    print()
    n = len(map[0])
    for i in range(n):
        line = ''
        for j in range(n):
            line += str(map[i][j])
        print(line)


def solution(n, k, apples, l, directions):
    time = 0

    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_d = 0

    def rotate(c):
        nonlocal current_d
        if c == 'D':
            current_d += 1
            if current_d == 4:
                current_d = 0
        else:
            current_d -= 1
            if current_d == -1:
                current_d = 3

    map = []

    # field
    for i in range(n + 2):
        if i == 0 or i == n + 1:
            map.append([1] * (n + 2))
        else:
            map.append([0] * (n + 2))
            map[i][0] = 1
            map[i][n + 1] = 1

    # apple
    for (x, y) in apples:
        map[x][y] = 3

    # snake
    map[1][1] = 2

    snake = [(1, 1)]
    next_rotate_time = directions[0][0]

    while True:
        if time == next_rotate_time:
            _, c = directions.pop(0)
            rotate(c)
            if len(directions) > 0:
                next_rotate_time = directions[0][0]

        point = d[current_d]
        head = snake[len(snake) - 1]
        mx = head[0] + point[0]
        my = head[1] + point[1]
        moved = map[mx][my]

        # border, body
        if moved == 1 or moved == 2:
            time += 1
            break

        # apple
        if moved != 3:
            tx, ty = snake.pop(0)
            map[tx][ty] = 0

        map[mx][my] = 2
        snake.append((mx, my))
        time += 1

    return time
