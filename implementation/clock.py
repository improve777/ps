import pytest


# 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성.

@pytest.mark.parametrize('n, expected', [(5, 11475)])
def test_solve(n, expected):
    result = solve1(n)
    assert result == expected


def solve1(n):
    count = 0
    for h in range(n + 1):
        for m in range(60):
            for s in range(60):
                if "3" in str(h) + str(m) + str(s):
                    count += 1

    return count

