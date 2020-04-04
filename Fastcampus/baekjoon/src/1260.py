import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    node_a, node_b = map(int, sys.stdin.readline().split())
    graph[node_a].append(node_b)
    graph[node_b].append(node_a)

adj_queue = deque([])
adj_stack = []
visited = [False for _ in range(n+1)]


def dfs(start_node):
    visited[start_node] = True
    print(start_node, end=' ')
    adj = sorted(graph[start_node], reverse=True)
    adj_stack.extend(adj)
    while adj_stack:
        node = adj_stack.pop()
        if visited[node] == False:
            visited[node] = True
            print(node, end=' ')
            adj = sorted(graph[node], reverse=True)
            adj_stack.extend(adj)
    return


def bfs(start_node):
    visited[start_node] = True
    print(start_node, end=' ')
    adj = sorted(graph[start_node])
    adj_queue.extend(adj)
    while adj_queue:
        node = adj_queue.popleft()
        if visited[node] == False:
            visited[node] = True
            print(node, end=' ')
            adj = sorted(graph[node])
            adj_queue.extend(adj)
    return


dfs(v)
print()

visited = [False for _ in range(n+1)]

bfs(v)
