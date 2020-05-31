from collections import deque


def bfs(node):
    global trees, visited, adj
    visited[node] = 1
    v_ = 1
    e_ = 0
    need_visit = deque([node])
    while need_visit:
        current_node = need_visit.popleft()
        for adj_node in adj[current_node]:
            e_ += 1
            if not visited[adj_node]:
                visited[adj_node] = 1
                v_ += 1
                need_visit.append(adj_node)
    if v_ == e_+1:
        trees += 1
    return


case = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    adj = [[] for i in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        x = min(a, b)
        y = max(a, b)
        if x == y:
            continue
        adj[x].append(y)
    visited = [0 for i in range(n+1)]
    trees = 0
    for i in range(1, n+1):
        if not visited[i]:
            bfs(i)
    if trees == 0:
        print("Case {0}: No trees.".format(case))
    elif trees == 1:
        print("Case {0}: There is one tree.".format(case))
    else:
        print("Case {0}: A forest of {1} trees.".format(case, trees))
    case += 1
