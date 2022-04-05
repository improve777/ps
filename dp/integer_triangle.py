import pytest


@pytest.mark.parametrize(
    'n, array, expected',
    [(5,
      [[7],
       [3, 8],
       [8, 1, 0],
       [2, 7, 4, 4],
       [4, 5, 2, 6, 5]],
      30)]
)
def test(n, array, expected):
    result = solution(n, array)
    assert result == expected


# x 0 1 2 x
#  0 1 2 3
def solution(n, array):
    for i in range(1, n):
        up = [0] + array[i - 1] + [0]

        for j in range(len(array[i])):
            num = array[i][j]
            array[i][j] = max(num + up[j], num + up[j + 1])

    return max(array[n - 1])


# 0 1 2
# 0 1 2 3
def solution2(n, array):
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:  # 좌측 맨끝
                up_left = 0
            else:
                up_left = array[i - 1][j - 1]
            if j == i:  # 우측 맨끝
                up = 0
            else:
                up = array[i - 1][j]

            array[i][j] = array[i][j] + max(up_left, up)

    return max(array[n - 1])
