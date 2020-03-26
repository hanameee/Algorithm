from collections import deque
import sys


N, M = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N+1)]

min_weight = 1000000000
max_weight = 0


def bfs(c):
    visited = [False] * (N+1)
    visited[start_node] = True
    check_adj = deque([start_node])
    while check_adj:
        node = check_adj.popleft()
        for y, weight in adj[node]:
            if not visited[y] and c <= weight:
                visited[y] = True
                check_adj.append(y)
    return visited[end_node]


for i in range(M):
    x, y, weight = map(int, sys.stdin.readline().split())
    adj[x].append((y, weight))
    adj[y].append((x, weight))
    min_weight = min(weight, min_weight)
    max_weight = max(weight, max_weight)

start_node, end_node = map(int, sys.stdin.readline().split())
result = min_weight

while min_weight <= max_weight:
    mid_weight = (min_weight + max_weight) // 2
    if bfs(mid_weight):
        result = mid_weight
        min_weight = mid_weight + 1
    else:
        max_weight = mid_weight - 1

print(result)
