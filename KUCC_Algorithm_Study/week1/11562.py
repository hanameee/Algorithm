import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
cost = [0]*(n+1)


def dijkstra(start_node):
    dists = [1e9]*(n+1)
    dists[start_node] = 0
    q = []
    heapq.heappush(q, (dists[start_node], start_node))
    while q:
        curr_dist, curr_node = heapq.heappop(q)
        if dists[curr_node] < curr_dist:
            continue
        for w, adj in graph[curr_node]:
            dist = curr_dist + w
            if dist < dists[adj]:
                dists[adj] = dist
                heapq.heappush(q, (dist, adj))
    cost[start_node] = dists


for _ in range(m):
    u, v, b = map(int, input().split())
    graph[u].append((0, v))
    if b == 1:
        graph[v].append((0, u))
    else:
        graph[v].append((1, u))

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    if not cost[x]:
        dijkstra(x)
    print(cost[x][y])
