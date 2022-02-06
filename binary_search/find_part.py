import pytest


@pytest.mark.parametrize(
    "n, array, m, parts, expected",
    [(5,
      [8, 3, 7, 9, 2],
      3,
      [5, 7, 9],
      "no yes yes"
      )])
def test_solve(n, array, m, parts, expected):
    result = solve3(n, array, parts)
    assert result == expected


def solve(n, array, parts):
    sorted_array = sorted(array)

    result = ""

    for part in parts:
        index = binary_search(sorted_array, part, 0, n - 1)
        if index is None:
            result += "no "
        else:
            result += "yes "

    return result.strip()


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


# 계수정렬 풀이
def solve2(n, array, parts):
    count_array = [0] * 1000001

    for i in array:
        count_array[i] = 1

    result = ""

    for part in parts:
        if count_array[part] != 1:
            result += "no "
        else:
            result += "yes "

    return result.strip()


# 집합 자료형 이용
def solve3(n, array, parts):
    my_set = set(array)

    result = ""

    for part in parts:
        if part in my_set:
            result += "yes "
        else:
            result += "no "

    return result.strip()



