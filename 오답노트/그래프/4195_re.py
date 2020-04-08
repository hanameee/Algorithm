test_cases = int(input())


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


for test_case in range(test_cases):
    f = int(input())
    parent = dict()
    rank = dict()
    number = dict()

    for i in range(f):
        x, y = input().split()
        if x not in parent:
            make_set(x)
        if y not in parent:
            make_set(y)
        union(x, y)
        print(number[find(x)])
