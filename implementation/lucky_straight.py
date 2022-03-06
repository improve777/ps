import pytest


@pytest.mark.parametrize(
    'n, expected',
    [(123402, "LUCKY"), (7755, "READY")]
)
def test(n, expected):
    result = solution(n)
    assert result == expected


def solution(n):
    mid = len(str(n)) / 2
    left = 0
    right = 0

    for i, c in enumerate(str(n)):
        if i < mid:
            left += int(c)
        else:
            right += int(c)

    if right == left:
        return "LUCKY"
    else:
        return "READY"


def solution2(n):
    s = str(n)
    length = len(s)
    summary = 0

    for i in range(length // 2):
        summary += int(s[i])

    for i in range(length // 2, length):
        summary -= int(n[i])

    if summary == 0:
        return "LUCKY"
    else:
        return "READY"
