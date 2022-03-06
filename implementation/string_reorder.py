import pytest


@pytest.mark.parametrize(
    's, expected',
    [('K1KA5CB7', 'ABCKK13'), ('AJKDLSI412K4JSJ9D', 'ADDIJJJKKLSS20')]
)
def test(s, expected):
    result = solution2(s)
    assert result == expected


def solution(s):
    result = ''
    num = 0

    s = sorted(s, key=lambda x: ord(x))

    for c in s:
        if ord(c) < ord('A'):
            num += int(c)
        else:
            result += c

    return result + str(num)


def solution2(s):
    result = []
    value = 0

    for x in s:
        if x.isalpha():
            result.append(x)
        else:
            value += int(x)

    result.sort()

    if value != 0:
        result.append(str(value))

    return ''.join(result)
