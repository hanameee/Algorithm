import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = list(map(int, input().split()))
graph = [[0]*n for _ in range(m)]
dp = [[-1]*n for _ in range(m)]

for x in range(m):
    row_data = list(map(int, input().split()))
    for y in range(n):
        graph[x][y] = row_data[y]


def get_dp(x, y):
    global graph, dp
    directions = [(0, -1), (0, +1), (-1, 0), (1, 0)]
    dp[x][y] = 0
    if x == 0 and y == 0:
        dp[x][y] = 1
        return 1
    for dx, dy in directions:
        nx = x+dx
        ny = y+dy
        if nx < 0 or nx > m-1 or ny < 0 or ny > n-1:
            continue
        if graph[x][y] < graph[nx][ny]:
            if dp[nx][ny] < 0:
                dp[nx][ny] = get_dp(nx, ny)
                dp[x][y] += dp[nx][ny]
            else:
                dp[x][y] += dp[nx][ny]
    return dp[x][y]


get_dp(m-1, n-1)
print(dp[m-1][n-1])
