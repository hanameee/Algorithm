import sys
from collections import deque


def bfs():
    n, k = map(int, sys.stdin.readline().split())
    limit = 100000
    visited = [0 for _ in range(limit+1)]
    queue = deque([n])
    time = 0
    while True:
        for i in range(len(queue)):
            current_node = queue.popleft()
            if current_node == k:
                return time
            for next_node in [current_node-1, current_node+1, current_node*2]:
                if 0 <= next_node <= limit and not visited[next_node]:
                    queue.append(next_node)
                    visited[next_node] = True
        time += 1


print(bfs())
