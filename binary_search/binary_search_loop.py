def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


if __name__ == '__main__':
    n = 10
    target = 7

    array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    index = binary_search(array, target, 0, n - 1)
    if index is None:
        print("원소가 존재하지 않습니다")
    else:
        print(index + 1)

    array = [1, 3, 5, 6, 9, 11, 13, 15, 17, 19]
    index = binary_search(array, target, 0, n - 1)
    if index is None:
        print("원소가 존재하지 않습니다")
    else:
        print(index + 1)
