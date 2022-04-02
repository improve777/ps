import pytest


@pytest.mark.parametrize(
    'n, c, array, expected',
    [(5, 3, [1, 2, 8, 4, 9], 3)]
)
def test(n, c, array, expected):
    result = solution(n, c, array)
    assert result == expected


def solution(n, c, array):
    array.sort()

    start = array[1] - array[0]
    end = array[-1] - array[0]
    result = 0

    while start <= end:
        mid = (start + end) // 2
        value = array[0]
        count = 1

        # 공유기 설치
        for i in range(1, n):
            if array[i] >= value + mid:
                value = array[i]
                count += 1

        # 거리 증가
        if count >= c:
            start = mid + 1
            result = mid
        # 거리 감소
        else:
            end = mid - 1

    return result
