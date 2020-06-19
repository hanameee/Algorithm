parent = [0 for i in range(501)]
cycle = [0 for i in range(501)]


def union(a, b):
    if cycle[a] or cycle[b]:
        cycle[a] = 1
        cycle[b] = 1
    parent[b] = a
    return


def find_parent(node):
    global parent
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]


case = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    for i in range(1, n+1):
        parent[i] = i
        cycle[i] = 0
    for _ in range(m):
        a, b = map(int, input().split())
        a_parent = find_parent(a)
        b_parent = find_parent(b)
        if a_parent == b_parent:
            cycle[a_parent] = 1
        else:
            union(a_parent, b_parent)
    trees = 0
    for idx in range(1, len(parent)):
        p = find_parent(parent[idx])
        if p == idx and not cycle[p]:
            trees += 1
        parent[idx] = p
    if trees == 0:
        print("Case {0}: No trees.".format(case))
    elif trees == 1:
        print("Case {0}: There is one tree.".format(case))
    else:
        print("Case {0}: A forest of {1} trees.".format(case, trees))
    case += 1
