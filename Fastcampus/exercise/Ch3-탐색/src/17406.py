from collections import deque
from copy import deepcopy
import sys

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
commands = []
min_value = 1000000

for _ in range(k):
    commands.append(list(map(int, input().split())))


def rotate(r, c, s, graph):
    global n, m
    g = deepcopy(graph)
    while s > 0:
        for x in range(r-s+1, r+s+1):
            g[x-1][c-s] = graph[x][c-s]
        for y in range(c-s, c+s):
            g[r-s][y+1] = graph[r-s][y]
        for x in range(r-s, r+s):
            g[x+1][c+s] = graph[x][c+s]
        for y in range(c-s+1, c+s+1):
            g[r+s][y-1] = graph[r+s][y]
        s -= 1
    return g


def compute_min(graph):
    global min_value
    for x in range(n):
        min_value = min(sum(graph[x]), min_value)
    return


def dfs(path, g):
    global k
    if len(path) == k:
        compute_min(g)
        return
    for i in range(k):
        if i not in path:
            path.append(i)
            gr = rotate(commands[i][0]-1, commands[i][1]-1, commands[i][2], g)
            dfs(path, gr)
            path.pop()


dfs([], graph)

print(min_value)
