def make_set(node):
    parent[node] = node
    rank[node] = 0
    number[node] = 1


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(x, y):
    root1 = find(x)
    root2 = find(y)
    if root1 != root2:
        if rank[root1] < rank[root2]:
            parent[root1] = root2
            number[root2] += number[root1]
        else:
            parent[root2] = root1
            number[root1] += number[root2]
            if rank[root1] == rank[root2]:
                rank[root1] += 1


test_case = int(input())

for case in range(test_case):
    parent = dict()
    rank = dict()
    number = dict()

    F = int(input())
    for _ in range(F):
        A, B = input().split()
        if A not in parent:
            make_set(A)
        if B not in parent:
            make_set(B)
        union(A, B)
        print(number[find(A)])
