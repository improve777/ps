import pytest
from bisect import bisect_left, bisect_right


@pytest.mark.parametrize(
    'words, queries, expected',
    [(
            ['frodo', 'front', 'frost', 'frozen', 'frame', 'kakao'],
            ['fro??', '????o', 'fr???', 'fro???', 'pro?'],
            [3, 2, 4, 1, 0]
    )]
)
def test(words, queries, expected):
    result = solution(words, queries)
    return result == expected


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


def solution(words, queries):
    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]

    answer = []

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)
    return answer
