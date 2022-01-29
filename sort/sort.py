# 이 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고,
# 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복하면 어떨까?
# O(N^2)
def selection_sort():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]  # 스왑

    print(array)


# 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입하면 어떨까?
# O(N^2)
def insertion_sort():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

    print(array)


# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸면 어떨까?
# 최선 O(NlogN), 최악 O(N^2)
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


def quick_sort_py_style(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_py_style(left_side) + [pivot] + quick_sort_py_style(right_side)


# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
# 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 O
# 데이터의 값이 무한한 범위를 가질 수 있는 실수형 데이터가 주어지는 경우 X
# 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 O
# O(N + K)
def count_sort():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

    count = [0] * (max(array) + 1)

    for i in range(len(array)):
        count[array[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')


def py_sorted():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    result = sorted(array)
    print(result)


def py_sort():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    array.sort()
    print(array)


def py_sorted_by_key():
    array = [('바나나', 2), ('사과', 5), ('당근', 3)]

    result = sorted(array, key=lambda data: data[1])
    print(result)


if __name__ == '__main__':
    selection_sort()
    insertion_sort()

    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    quick_sort(array, 0, len(array) - 1)
    print(array)

    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    print(quick_sort_py_style(array))

    count_sort()
    print()

    py_sorted()

    py_sort()

    py_sorted_by_key()

