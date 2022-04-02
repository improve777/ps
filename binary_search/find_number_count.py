import pytest
from bisect import bisect_left, bisect_right


@pytest.mark.parametrize(
    'n, x, array, expected',
    [(7, 2, [1, 1, 2, 2, 2, 2, 3], 4),
     (7, 4, [1, 1, 2, 2, 2, 2, 3], -1),
     ]
)
def test(n, x, array, expected):
    result = solution2(n, x, array)
    assert result == expected


def solution(n, x, array):
    def count_by_value(array, x):
        a = first(array, x, 0, n - 1)
        if a is None:
            return 0

        b = last(array, x, 0, n - 1)
        return b - a + 1

    def first(array, target, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
            return mid
        elif array[mid] >= target:
            return first(array, target, start, mid - 1)
        else:
            return first(array, target, mid + 1, end)

    def last(array, target, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
            return mid
        elif array[mid] > target:
            return last(array, target, start, mid - 1)
        else:
            return last(array, target, mid + 1, end)

    count = count_by_value(array, x)
    return -1 if count == 0 else count


def solution2(n, x, array):
    def count_by_range(array, left_value, right_value):
        right_index = bisect_right(array, right_value)
        left_index = bisect_left(array, left_value)
        return right_index - left_index

    count = count_by_range(array, x, x)

    return -1 if count == 0 else count
