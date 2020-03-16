import heapq


mygraph = {
    "A": {"B": 8, "C": 1, "D": 2},
    "B": {},
    "C": {"B": 5, "D": 2},
    "D": {"E": 3, "F": 5},
    "E": {"F": 1},
    "F": {"A": 5},
}


def dijsktra(graph, start, end):
    # 시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리를 생성하고, 무한대로 초기화
    distances = {vertex: [float("inf"), start] for vertex in graph}
    distances[start] = [0, start]
    # 모든 정점이 저장될 큐(최소힙) 생성
    queue = []
    # 그래프의 시작 정점과 시작 정점의 거리를 최소힙에 넣어줌
    heapq.heappush(queue, [distances[start][0], start])

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if distances[current_vertex][0] < current_distance:
            continue

        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[adjacent][0]:
                # 기존 알고리즘과의 차이점이라면, current_vertex 도 저장한다는 점! 어딜 거쳐서 가는게 최단인지!
                distances[adjacent] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adjacent])
    path = end
    path_output = end + '->'
    # 최초 정점 직전까지 계속해서 반복문을 돌며 최단경로의 경유 노드를 찾아나감
    while distances[path][1] != start:
        path_output += distances[path][1] + '->'
        # 최단 경로를 위한 직전 경유지를 다시 path에 할당
        path = distances[path][1]
    path_output += start
    print(path_output)
    return distances


dijsktra(mygraph, "A", "F")
