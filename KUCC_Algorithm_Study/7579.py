import sys
input = sys.stdin.readline

N, M = map(int, input().split())
app_memory = list(map(int, input().split()))
app_cost = list(map(int, input().split()))
dp = [[0]*(10001) for i in range(N+1)]
data = [0]*(N+1)
for i in range(N):
    data[i+1] = (app_cost[i], app_memory[i])

min_cost = 1e9
for i in range(1, N+1):
    c, m = data[i]
    for j in range(0, 10001):
        if j < c:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], m+dp[i-1][j-c])
        if dp[i][j] >= M:
            min_cost = min(min_cost, j)

print(min_cost)
