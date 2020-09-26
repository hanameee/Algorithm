import heapq


def solution(N, road, K):
    adj = [[] for i in range(N+1)]
    dist = [float("inf") for i in range(N+1)]
    dist[1] = 0
    need_visit = [(0, 1)]
    for r in road:
        a, b, c = r
        adj[a].append((c, b))
        adj[b].append((c, a))
    while need_visit:
        curr_dist, curr_v = heapq.heappop(need_visit)
        for adj_dist, adj_v in adj[curr_v]:
            if dist[adj_v] > adj_dist+curr_dist:
                dist[adj_v] = adj_dist+curr_dist
                heapq.heappush(need_visit, (dist[adj_v], adj_v))
    answer = 0
    for d in dist:
        if d <= K:
            answer += 1
    return answer


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2],
                   [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
