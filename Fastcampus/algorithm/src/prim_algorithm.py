# 중복된 간선은 빼고 표현, 노드는 별도로 표현할 필요 X
from collections import defaultdict
from heapq import *

myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'), (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]


def prim(start_node, edges):
    adjacent_edges = defaultdict(list)
    mst = list()
    for weight, n1, n2 in edges:
        # 이 과정에서 자동으로 간선들이 양쪽 노드에 중복으로 잘 들어감
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))
    connected_nodes = set(start_node)  # 연결된 노드들을 집합 형태로
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)  # n1은 원래 정점, n2가 인접 정점
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))
            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)
    return mst


print(prim('A', myedges))
