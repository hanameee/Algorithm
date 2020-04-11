import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0]*(n+1)
rank = [0]*(n+1)
position = [[] for i in range(n+1)]
cost = []
mst = []


def make_set(node):
    parent[node] = node
    rank[node] = 0


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(u, v):
    root1 = find(u)
    root2 = find(v)
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


# 각 노드의 가중치 구하는 함수
def get_cost(a, b):
    return (abs(position[a][0]-position[b][0])**2 + abs(position[a][1]-position[b][1])**2)**0.5


for i in range(n):
    make_set(i+1)

# n개의 노드들에 대해 좌표 정보 position에 저장
for i in range(n):
    x, y = map(int, input().split())
    position[i+1] = (x, y)

# 간선들의 모든 가중치 구하기
for i in range(1, n):
    for j in range(i+1, n+1):
        cost.append((get_cost(i, j), i, j))


# 연결된 m개의 간선들에 대해 union
for j in range(m):
    a, b = map(int, input().split())
    union(a, b)

cost.sort()

for edge in cost:
    weight, u, v = edge
    if find(u) != find(v):
        union(u, v)
        mst.append(edge)

total_cost = 0
for edges in mst:
    total_cost += edges[0]

print(format(total_cost, ".2f"))
