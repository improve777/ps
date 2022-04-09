import pytest


@pytest.mark.parametrize(
    'n, array, expected',
    [(7, [(3, 10), (5, 20), (1, 10), (1, 20), (2, 15), (4, 40), (2, 200)], 45),
     (10, [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10)], 55)
     ]
)
def test(n, array, expected):
    result = solution(n, array)
    assert result == expected


# 1 <= n <= 15
# array[ (1 <= t <= 5, 1 <= p <= 1000) ]
def solution(n, array):
    incomes = [0] * (n + 1)

    # 상담 기간 1 ~ 5일
    for i in range(1, 6):
        for j in range(n):
            t, p = array[j]
            # 상담 기간이 일치
            if t == i:
                if j + t - 1 >= n:
                    continue
                last_p = sum(incomes[j:j + t])
                if p > last_p:
                    for k in range(j, j + t):
                        incomes[k] = 0
                    incomes[j + t - 1] = p

    return sum(incomes)


def solution2(n, array):
    dp = [0] * (n + 1)
    max_value = 0

    for i in range(n - 1, -1, -1):
        t, p = array[i]
        time = t + i

        if time <= n:
            dp[i] = max(p[i] + dp[time], max_value)
            max_value = dp[i]
        else:
            dp[i] = max_value

    return max_value
