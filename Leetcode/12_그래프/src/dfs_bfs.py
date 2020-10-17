from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}


def recursive_dfs(v, visited=[]):
    visited.append(v)
    for w in graph[v]:
        if not w in visited:
            visited = recursive_dfs(w, visited)
    return visited


def iterative_dfs(start_v):
    visited = []
    need_visit = [start_v]
    while need_visit:
        v = need_visit.pop()
        # element in stk can be already visited
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                need_visit.append(w)
    return visited


def bfs(v):
    visited = [v]
    need_visit = deque([v])
    while need_visit:
        v = need_visit.popleft()
        for w in graph[v]:
            if w not in visited:
                # adjacent node should be checked as visited before it is pushed to queue
                visited.append(w)
                need_visit.append(w)
    return visited


print(recursive_dfs(1))
print(iterative_dfs(1))
print(bfs(1))
