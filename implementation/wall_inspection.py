import pytest
from itertools import permutations


@pytest.mark.parametrize(
    'n, weak, dist, expected',
    [(12, [1, 5, 6, 10], [1, 2, 3, 4], 2),
     (12, [1, 3, 4, 9, 10], [3, 5, 7], 1)]
)
def test(n, weak, dist, expected):
    result = solution(n, weak, dist)
    assert result == expected


def solution(n, weak, dist):
    length = len(weak)

    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    for i in range(length):
        weak.append(weak[i] + n)

    # 투입할 친구 수의 최댓값 + 1 으로 초기화
    answer = len(dist) + 1

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)

    if answer > len(dist):
        return - 1
    return answer
