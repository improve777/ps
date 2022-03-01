import pytest


@pytest.mark.parametrize(
    's, expected',
    [('0001100', 1), ('101010', 3), ('1111', 0)]
)
def test_solve(s, expected):
    result = solve(s)
    assert result == expected


def solve(s):
    last = -1
    counter = [0] * 2

    for c in s:
        i = int(c)
        if last != i:
            counter[i] += 1
            last = i

    return min(counter[0], counter[1])


def solve2(s):
    count0 = 0
    count1 = 0

    if s[0] == '1':
        count0 += 1
    else:
        count1 += 1

    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            if s[i + 1] == '1':
                count0 += 1
            else:
                count1 += 1

    return min(count0, count1)
