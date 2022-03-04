import pytest


@pytest.mark.parametrize(
    'n, m, array, expected',
    [(5, 3,
      [1, 3, 2, 3, 2],
      8),
     (8, 5,
      [1, 5, 4, 3, 2, 4, 5, 2],
      25)]
)
def test(n, m, array, expected):
    result = solution3(n, m, array)
    assert result == expected


def solution(n, m, array):
    pairs = set()

    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if (j, i) not in pairs and array[i] != array[j]:
                pairs.add((i, j))

    return len(pairs)


def solution2(n, m, array):
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if array[i] != array[j]:
                count += 1

    return count


# 1 3 2 3 2 -> 5(n)
# 1 : 1 -> 1 * 4(n) = 4
# 2 : 2 -> 2 * 2(n) = 4
# 3 : 2 -> 2 * 0(n) = 0
def solution3(n, m, array):
    # 가능한 무게
    weights = [0] * 11
    for x in array:
        weights[x] += 1

    count = 0
    # 각 무게에 대하여 처리
    for i in range(1, m + 1):
        n -= weights[i]
        count += weights[i] * n

    return count
