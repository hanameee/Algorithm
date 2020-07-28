# _*_ coding: utf-8 _*_
import sys
from collections import deque
sys.setrecursionlimit(10**9)


def set_adj_graph(path):
    adj_graph = [[] for _ in range(N)]
    for node_a, node_b in path:
        adj_graph[node_a].append(node_b)
        adj_graph[node_b].append(node_a)
    return adj_graph


def set_dir_graph(graph, order):
    dir_graph = [[] for _ in range(N)]
    # bfs로 방향 그래프 만들기
    need_visit = deque([0])
    visited = [0 for _ in range(N)]
    while need_visit:
        curr_node = need_visit.popleft()
        visited[curr_node] = 1
        for adj_node in graph[curr_node]:
            if not visited[adj_node]:
                dir_graph[curr_node].append(adj_node)
                need_visit.append(adj_node)
    # order도 추가해주기
    for prev_node, next_node in order:
        dir_graph[prev_node].append(next_node)
    return dir_graph


def is_cyclic(start_node):
    visited[start_node] = True
    in_dfs[start_node] = True
    for child_node in dir_graph[start_node]:
        if visited[child_node]:
            if in_dfs[child_node]:
                return True
            continue
        if is_cyclic(child_node):
            return True
    in_dfs[start_node] = False
    return False


def solution(n, path, order):
    global N, adj_graph, dir_graph, visited, in_dfs
    N = n
    adj_graph = set_adj_graph(path)
    dir_graph = set_dir_graph(adj_graph, order)
    visited = [0 for _ in range(N)]
    in_dfs = [0 for _ in range(N)]
    visited[0] = 1
    flag = is_cyclic(0)
    return False if flag else True


print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6],
                   [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))
print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6],
                   [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]))
