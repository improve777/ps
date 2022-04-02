import pytest


@pytest.mark.parametrize(
    'n, array, expected',
    [(5, [-15, -6, 1, 3, 7], 3),
     (7, [-15, -4, 2, 8, 9, 13, 15], 2),
     (7, [-15, -4, 3, 8, 9, 13, 15], -1),
     ]
)
def test(n, array, expected):
    result = solution(n, array)
    assert result == expected


def solution(n, array):
    def binary_search(array, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            return binary_search(array, start, mid - 1)
        else:
            return binary_search(array, mid + 1, end)

    index = binary_search(array, 0, n - 1)

    return -1 if index is None else index
