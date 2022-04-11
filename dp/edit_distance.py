import pytest


@pytest.mark.parametrize(
    'a, b, expected',
    [('cat', 'cut', 1),
     ('sunday', 'saturday', 3)]
)
def test(a, b, expected):
    result = solution(a, b)
    assert result == expected


def solution(a, b):
    n = len(a)
    m = len(b)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 삽입
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위)
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[n][m]
