import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = list(map(int, input().split()))
graph = [[0]*n for _ in range(m)]
result = 0
need_visit = deque([])
time = 0
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]


for i in range(m):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == -1:
            result += 1
        if row[j] == 1:
            need_visit.append([i, j, 0])
            result += 1
        graph[i][j] = row[j]

while need_visit:
    cur_x, cur_y, cur_time = need_visit.popleft()
    time = max(cur_time, time)
    for dx, dy in directions:
        nx = cur_x + dx
        ny = cur_y + dy
        if nx < 0 or nx > m-1 or ny < 0 or ny > n-1:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 1
            result += 1
            need_visit.append([nx, ny, cur_time+1])

if result == n*m:
    print(time)
else:
    print(-1)
