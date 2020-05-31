import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n, m = map(int, input().split())
rank = [0 for i in range(n+1)]
parent = [i for i in range(n+1)]


def union(a, b):
    global rank, parent
    if rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        if rank[a] == rank[b]:
            rank[a] += 1


def find_parent(node):
    global parent
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]


for i in range(m):
    command, a, b = map(int, input().split())
    a_parent = find_parent(a)
    b_parent = find_parent(b)
    if command == 0:
        if a_parent != b_parent:
            union(a_parent, b_parent)
        pass
    else:
        if a_parent == b_parent:
            print("YES")
        else:
            print("NO")
