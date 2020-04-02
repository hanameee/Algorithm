import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
MAX = 100001
depth = [0 for _ in range(MAX)]
queue = deque([n])


def dfs():
    while queue:
        current_node = queue.popleft()
        if current_node == k:
            return depth[current_node]
        for next_node in [current_node-1, current_node+1, current_node*2]:
            if 0 <= next_node < MAX and depth[next_node] == 0:
                queue.append(next_node)
                depth[next_node] = depth[current_node] + 1


print(dfs())
