import heapq


def solution(n, edge):
    graph = [[] for i in range(n+1)]
    # 그래프 만들기
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    # 초기화 (출발 점과 각 노드 간의 최단거리를 저장할 배열 만들기)
    distances = [float("inf") for i in range(n+1)]
    distances[1] = 0
    q = []
    # 우선순위 큐에 기준이 되는 노드 넣기 [해당 노드까지의 거리, 해당 노드]
    heapq.heappush(q, [distances[1], 1])
    max_dist = -1
    while q:
        curr_distance, curr_node = heapq.heappop(q)
        # 현재 거리보다 해당 노드까지의 거리가 더 짧다면 검토할 이유가 없음
        if distances[curr_node] < curr_distance:
            continue
        # 현재 노드와 인접한 노드들에 대해
        for adj in graph[curr_node]:
            distance = curr_distance + 1
            # 지금까지의 최단거리보다 짧다면 업데이트하고 큐에 넣어준다
            if distance < distances[adj]:
                distances[adj] = distance
                heapq.heappush(q, [distance, adj])
    max_distance = max(distances[2:])
    answer = 0
    for i in range(2, len(distances)):
        if distances[i] >= max_distance:
            answer += 1
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
