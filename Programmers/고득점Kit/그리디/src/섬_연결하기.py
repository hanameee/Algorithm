import heapq

# 프림 알고리즘 사용


def solution(n, costs):
    answer = 0
    costs = [[cost[2], cost[0], cost[1]] for cost in costs]
    mst = []
    adj_edges = [[] for i in range(n)]
    for cost, n1, n2 in costs:
        adj_edges[n1].append([cost, n1, n2])
        adj_edges[n2].append([cost, n2, n1])
    connected_nodes = set([costs[0][1]])
    candidate_edges = adj_edges[costs[0][1]]
    heapq.heapify(candidate_edges)

    while candidate_edges:
        cost, n1, n2 = heapq.heappop(candidate_edges)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            answer += cost
            for edge in adj_edges[n2]:
                if edge[2] not in connected_nodes:
                    heapq.heappush(candidate_edges, edge)
    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
