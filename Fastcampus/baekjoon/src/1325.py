from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[b].append(a)


def bfs(node):
    q = deque([node])
    visited_node = [0]*(n+1)
    visited_node[node] = 1
    count = 1
    while q:
        current_node = q.popleft()
        for adj_node in adj[current_node]:
            if not visited_node[adj_node]:
                q.append(adj_node)
                visited_node[adj_node] = 1
                count += 1
    return count


result = []
max_value = -1

for node in range(1, n+1):
    c = bfs(node)
    if c > max_value:
        result = [node]
        max_value = c
    elif c == max_value:
        result.append(node)
        max_value = c


for answer in result:
    print(answer, end=' ')
