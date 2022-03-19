import pytest
from itertools import permutations


@pytest.mark.parametrize(
    'n, array, operator, expected',
    [
        (2, [5, 6], [0, 0, 1, 0], [30, 30]),
        (3, [3, 4, 5], [1, 0, 1, 0], [35, 17]),
        (6, [1, 2, 3, 4, 5, 6], [2, 1, 1, 1], [54, -24]),
    ]
)
def test(n, array, operator, expected):
    result = solution2(n, array, operator)
    assert result == expected


def solution(n, array, operator):
    if n == 1:
        return [array[0], array[0]]

    min_value = int(1e9)
    max_value = 0

    # 오퍼레이션 목록 풀기
    operator_list = []
    for i in range(4):
        for _ in range(operator[i]):
            operator_list.append(i)

    # 모든 순열
    operators = list(map(list, permutations(operator_list)))

    for op_list in operators:
        temp_nums = []
        for n in array:
            temp_nums.append(n)

        temp = temp_nums.pop(0)

        while temp_nums:
            next = temp_nums.pop(0)
            op = op_list.pop(0)
            if op == 0:
                temp += next
            elif op == 1:
                temp -= next
            elif op == 2:
                temp *= next
            else:
                if temp < 0:
                    temp = -(-temp // next)
                else:
                    temp //= next

        max_value = max(max_value, temp)
        min_value = min(min_value, temp)

    return [max_value, min_value]


def solution2(n, array, operator):
    min_value = int(1e9)
    max_value = -int(1e9)

    add, sub, mul, div = operator[0], operator[1], operator[2], operator[3],

    def dfs(i, now):
        nonlocal min_value, max_value, add, sub, mul, div
        if i == n:
            min_value = min(min_value, now)
            max_value = max(max_value, now)
        else:
            if add > 0:
                add -= 1
                dfs(i + 1, now + array[i])
                add += 1
            if sub > 0:
                sub -= 1
                dfs(i + 1, now - array[i])
                sub += 1
            if mul > 0:
                mul -= 1
                dfs(i + 1, now * array[i])
                mul += 1
            if div > 0:
                div -= 1
                dfs(i + 1, int(now / array[i]))
                div += 1

    dfs(1, array[0])

    return [max_value, min_value]

