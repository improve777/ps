import pytest


@pytest.mark.parametrize(
    'n, lost, reserve, expected',
    [(5, [2, 4], [1, 3, 5], 5),
     (5, [2, 4], [3], 4),
     (3, [3], [1], 2)]
)
def test(n, lost, reserve, expected):
    result = solution(n, lost, reserve)
    assert result == expected


def solution(n, lost, reserve):
    answer = 0
    students = [1] * n

    for i in reserve:
        students[i - 1] += 1

    for i in lost:
        students[i - 1] -= 1

    for i in range(0, len(students)):
        f = i - 1
        if f >= 0 and students[f] > 1 and students[i] == 0:
            students[i] += 1
            students[f] -= 1
            continue
        b = i + 1
        if b < len(students) and students[b] > 1 and students[i] == 0:
            students[i] += 1
            students[b] -= 1

    for i in students:
        if i > 0:
            answer += 1

    return answer


def solution2(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
