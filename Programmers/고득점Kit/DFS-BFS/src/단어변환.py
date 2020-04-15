from collections import deque
graph = []
target_idx = 0
def bfs(start_node):
    global graph, target_idx
    q = deque([])
    visited = [start_node]
    q.extend(graph[start_node])
    level = [0]*len(graph)
    for adj_node in graph[start_node]:
        q.append(adj_node)
        level[adj_node] = 1
    while q:
        cur_node = q.popleft()
        if cur_node == target_idx:
            return(level[cur_node])
        visited.append(cur_node)
        for adj_node in graph[cur_node]:
            if adj_node not in visited:
                q.append(adj_node)
                if level[adj_node] == 0:
                    level[adj_node] = level[cur_node] +1
    return -1

def solution(begin, target, words):
    global graph
    global target_idx
    data = [begin] + words
    target_idx = -1
    for idx in range(len(data)):
        if data[idx] == target:
            target_idx = idx
            break
    if target_idx == -1:
        return 0
    graph = [[] for i in range(len(data))]
    for i in range(0,len(data)-1):
        for j in range(i+1,len(data)):
            is_different = 0
            for idx in range(len(data[i])):
                if data[i][idx] != data[j][idx]:
                    is_different += 1
                    if is_different > 1:
                        break
            if is_different == 1:
                graph[i].append(j)
                graph[j].append(i)
    print(graph)
    answer = bfs(0)
    if answer == -1:
        return 0
    else:
        return answer