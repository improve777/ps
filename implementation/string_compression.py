import pytest


@pytest.mark.parametrize(
    's, expected',
    [('aabbaccc', 7),
     ('ababcdcdababcdcd', 9),
     ('abcabcdede', 8),
     ('abcabcabcabcdededededede', 14),
     ('xababcdcdababcdcd', 17)]
)
def test(s, expected):
    result = solution(s)
    assert result == expected


def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1

        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer
