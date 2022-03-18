import pytest


@pytest.mark.parametrize(
    'p, expected',
    [('(()())()', '(()())()'),
     (')(', '()'),
     ('()))((()', '()(())()')]
)
def test(p, expected):
    result = solution(p)
    assert result == expected


# 균형 잡힌 괄호 문자열 인덱스
def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


# 올바른 괄호 문자열 판단
def check_proper(p):
    count = 0
    for c in p:
        if c == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True


def solution(p):
    answer = ''
    if p == '':
        return answer

    index = balanced_index(p)

    u = p[:index + 1]
    v = p[index + 1:]

    if check_proper(u):
        # 재귀적으로 수행
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        # 앞뒤 제거
        u = list(u[1:-1])
        # 반전 수행
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer
