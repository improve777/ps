def find_parent(parent, x):
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


# O(ElogE)
if __name__ == '__main__':
    v, e = 7, 9
    parent = [0] * (v + 1)

    edges = []
    result = 0

    for i in range(1, v + 1):
        parent[i] = i

    edges.append((29, 1, 2))
    edges.append((75, 1, 5))
    edges.append((35, 2, 3))
    edges.append((34, 2, 6))
    edges.append((7, 3, 4))
    edges.append((23, 4, 6))
    edges.append((13, 4, 7))
    edges.append((53, 5, 6))
    edges.append((25, 6, 7))

    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    print(result)
