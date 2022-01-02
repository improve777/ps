import pytest


@pytest.mark.parametrize("n,k,expected", [(25, 5, 2), (107, 3, 10)])
def test_solve(n, k, expected):
    count = solve3(n, k)
    assert count == expected


def solve1(n, k):
    count = 0

    while True:
        if n % k == 0:
            n = n / k
            count += 1
        else:
            n -= 1
            count += 1
        if n == 1:
            break

    return count


def solve2(n, k):
    count = 0

    while n >= k:
        while n % k != 0:
            n -= 1
            count += 1
        n //= k
        count += 1

    while n > 1:
        n -= 1
        count += 1

    return count


def solve3(n, k):
    count = 0

    while True:
        # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
        target = (n // k) * k
        count += (n - target)
        n = target
        # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
        if n < k:
            break
        count += 1
        n //= k

    # 마지막으로 남은 수에 대하여 1씩 빼기
    count += (n - 1)

    return count
