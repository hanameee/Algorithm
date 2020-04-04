import sys

n = int(sys.stdin.readline().strip())
e = int(sys.stdin.readline().strip())

adj = [[] for i in range(n+1)]
for i in range(e):
    x, y = map(int, sys.stdin.readline().split())
    adj[x].append(y)
    adj[y].append(x)


def dfs(start_node):
    visited = [0 for i in range(n+1)]
    stack = [start_node]
    result = 0
    while stack:
        current_node = stack.pop()
        for adj_node in adj[current_node]:
            if not visited[adj_node]:
                stack.append(adj_node)
                visited[adj_node] = 1
                result += 1
    return result-1


print(dfs(1))
