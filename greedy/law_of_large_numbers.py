import pytest


# 배열의 크기 N
# 주어진 수를 M번 더하여 가장 큰 수
# 연속해서 K번 초과 불가
# 배열 array
@pytest.mark.parametrize("n,m,k,data,expected", [(5, 8, 3, [2, 4, 5, 4, 6], 46)])
def test_solve(n, m, k, data, expected):
    result = solve2(n, m, k, data)
    assert result == expected


def solve1(n, m, k, data):
    data.sort()
    first = data[n - 1]
    second = data[n - 2]

    result = 0

    while True:
        for i in range(k):
            if m == 0:
                break
            result += first
            m -= 1
        if m == 0:
            break
        result += second
        m -= 1

    return result


def solve2(n, m, k, data):
    data.sort()
    first = data[n - 1]
    second = data[n - 2]

    count = int(m / (k + 1)) * k
    count += m % (k + 1)

    result = 0
    result += count * first
    result += (m - count) * second

    return result
