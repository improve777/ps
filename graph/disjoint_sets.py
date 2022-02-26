# 특정 원소가 속한 집합을 찾기
# 시간 복잡도 최대 O(V)
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 경로 압축
def find_parent2(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == '__main__':
    v, e = map(int, input().split())
    parent = [0] * (v + 1)

    for i in range(1, v + 1):
        parent[i] = i

    # union 연산 수행
    for i in range(e):
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    print('각 노드가 속한 집합: ', end='')
    for i in range(1, v + 1):
        print(find_parent(parent, i), end=' ')

    print()

    print('부모 테이블: ', end='')
    for i in range(1, v + 1):
        print(parent[i], end=' ')
