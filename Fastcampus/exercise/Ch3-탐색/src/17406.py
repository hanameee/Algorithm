from collections import deque
from itertools import permutations
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
    for x in range(r-s, r+s+1):
        for y in range(c-s, c+s+1):
            if x == r-s and y < c+s:
                g[x][y+1] = graph[x][y]
            if x < r-s and y == c+s:
                g[x+1][y] = graph[x][y]
            if x == r+s and y > c-s:
                g[x][y-1] = graph[x][y]
            if x > r-s and y == c-s:
                g[x-1][y] = graph[x][y]
    for _ in g:
        print(_)
    return g


def compute_min(graph):
    global min_value
    for x in range(n):
        min_value = min(sum(graph[x]), min_value)
    return


commands_perm = permutations(range(len(commands)))
# 0,1 1,0
for command in commands_perm:
    print(command)
    g = graph
    for i in range(k):
        r = commands[command[i]][0]-1
        c = commands[command[i]][1]-1
        s = commands[command[i]][2]-1
        g = rotate(r, c, s, g)
    print(command)
    compute_min(g)

print(min_value)
