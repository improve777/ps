import pytest

@pytest.mark.parametrize(
    'n, inputs, expected',
    [(2,
      ['홍길동 95', '이순신 77'],
      ['이순신', '홍길동'])])
def test_solve(n, inputs, expected):
    result = solve(inputs)
    assert result == expected


def solve(inputs):
    def mapToStudent(data):
        nameAndScore = data.split()
        return nameAndScore[0], int(nameAndScore[1])

    students = map(mapToStudent, inputs)

    students = sorted(students, key=lambda x: x[1])
    return list(map(lambda x: x[0], students))
