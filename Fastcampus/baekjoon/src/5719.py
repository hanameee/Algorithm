import sys
import heapq
from collections import deque
input = sys.stdin.readline


def dijkstra():
    q = []
    heapq.heappush(q, (0, start))
    while q:
        curr_dist, curr_node = heapq.heappop(q)
        if dists[curr_node] < curr_dist:
            continue
        else:
            for adj_dist, adj_node in adj[curr_node]:
                new_dist = adj_dist + curr_dist
                if new_dist < dists[adj_node] and not dropped[curr_node][adj_node]:
                    dists[adj_node] = new_dist
                    heapq.heappush(q, (new_dist, adj_node))


def bfs():
    path_q = deque()
    path_q.append(end)
    while path_q:
        node = path_q.popleft()
        if node == start:
            continue
        for prev_dist, prev_node in reverse_adj[node]:
            if prev_dist + dists[prev_node] == dists[node]:
                dropped[prev_node][node] = True
                path_q.append(prev_node)


while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    start, end = map(int, input().split())
    adj = [[] for i in range(n)]
    reverse_adj = [[] for i in range(n)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        adj[u].append((p, v))
        reverse_adj[v].append((p, u))
    dropped = [[False]*n for i in range(n)]
    dists = [1e9]*n
    dists[start] = 0
    dijkstra()
    bfs()
    dists = [1e9]*n
    dists[start] = 0
    dijkstra()
    print(dists[end] if dists[end] != 1e9 else -1)
