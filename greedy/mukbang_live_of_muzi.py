import pytest
import heapq


@pytest.mark.parametrize(
    'food_times, k, expected',
    [([3, 1, 2], 5, 1)]
)
def test(food_times, k, expected):
    result = solution(food_times, k)
    assert result == expected


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    # 우선순위 큐
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0
    previous = 0

    length = len(food_times)  # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1  # 다 먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]
