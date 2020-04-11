import heapq
import sys
input = sys.stdin.readline


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0
    while q:
        current_dist, current_node = heapq.heappop(q)
        if distances[current_node] < current_dist:
            continue
        for adj_dist, adj_node in adj[current_node]:
            distance = current_dist + adj_dist
            if distances[adj_node] > distance:
                distances[adj_node] = distance
                heapq.heappush(q, (distance, adj_node))


for _ in range(int(input())):
    n, m, start = map(int, input().split())
    adj = [[] for i in range(n+1)]
    for _ in range(m):
        x, y, cost = map(int, input().split())
        adj[y].append((cost, x))
    distances = [1e9] * (n+1)
    dijkstra(start)
    count = 0
    max_distance = 0
    for i in distances:
        if i != 1e9:
            count += 1
            max_distance = max(max_distance, i)
    print(count, max_distance)
