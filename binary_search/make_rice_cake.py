import pytest


@pytest.mark.parametrize(
    "n, m, array, expected",
    [(4, 6,
      [19, 15, 10, 17],
      15
      )])
def test_solve(n, m, array, expected):
    h = solve(m, array)
    assert h == expected


# 파라메트릭 서치 : 최적화 문제를 결정 문제(예, 아니오)로 바꾸어 해결하는 기법
#               원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에 주로 사용함
def solve(m, array):
    start = 0
    end = max(array)

    h = binary_search(array, m, start, end)
    return h


def binary_search(array, m, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2

        size = 0
        for rice in array:
            if rice > mid:
                size += rice - mid

        if size < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return result
