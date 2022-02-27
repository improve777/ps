import pytest


@pytest.mark.parametrize(
    "n, array, expected",
    [(5,
      [2, 3, 1, 2, 2],
      2),
     (3,
      [1, 1, 1],
      3),
     (4,
      [1, 1, 1, 2],
      3),
     (5,
      [4, 1, 1, 1, 1],
      4)
     ]
)
def test_solve(n, array, expected):
    result = solve3(n, array)
    assert result == expected


# fail
def solve(n, array):
    # 3 2 2 2 1
    array.sort(reverse=True)

    result = 0
    num = n

    for i in range(n):
        if num >= array[i]:
            num -= array[i]
            result += 1

    return result


def solve2(n, array):
    result = 0
    num = n

    count = 0

    for i in range(n):
        for adventurer in array:
            if adventurer == i and num >= adventurer:
                count += 1
                num -= adventurer

        if result < count:
            result = count
        count = 0

    return result


def solve3(n, array):
    array.sort()
    result = 0
    count = 0

    for i in array:
        count += 1
        if count >= i:
            result += 1
            count = 0

    return result
