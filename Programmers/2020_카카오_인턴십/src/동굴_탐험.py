# _*_ coding: utf-8 _*_
from collections import deque


def solution(n, path, order):
    need_visit = deque()
    answer = False
    visit = [0]*n
    visit[0] = 1
    cango = [0]*n
    cango[0] = 1
    parent_graph = {}
    child_graph = {}
    for prev_node, next_node in order:
        parent_graph[next_node] = prev_node
        child_graph[prev_node] = next_node
    graph = [[] for _ in range(n)]
    # graph 완성해주기 (양방향 그래프)
    for prev_node, next_node in path:
        graph[prev_node].append(next_node)
        graph[next_node].append(prev_node)
    # root node인 0이 선행지점이 없는지 체크해야 함
    if parent_graph.get(0) is None:
        need_visit.extend(graph[0])
    while need_visit:
        curr_node = need_visit.popleft()
        cango[curr_node] = 1
        # curr_node를 방문하기 위한 선행지점이 없을 경우
        if parent_graph.get(curr_node) is None:
            visit[curr_node] = 1
            for adj_node in graph[curr_node]:
                if visit[adj_node] == 0:
                    need_visit.append(adj_node)
            # curr_node을 선행지점으로 하는 노드가 있고, 해당 노드를 갈 수 있는 경우
            if child_graph.get(curr_node) is not None and cango[child_graph[curr_node]]:
                need_visit.append(child_graph[curr_node])
        else:
            # curr_node를 방문하기 위한 선행지점이 있는데, 그 선행 지점을 방문했을 경우
            if visit[parent_graph.get(curr_node)] == 1:
                visit[curr_node] = 1
                for adj_node in graph[curr_node]:
                    if visit[adj_node] == 0:
                        need_visit.append(adj_node)
    if sum(visit) == n:
        answer = True
    return answer


print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6],
                   [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))
print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6],
                   [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]))

# 0,3,4,6,7
