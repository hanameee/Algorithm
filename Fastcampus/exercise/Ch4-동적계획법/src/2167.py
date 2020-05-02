import sys
input = sys.stdin.readline

n, m = map(int, input().split())
brd = [[0]*(m+1)] + [[0]+list(map(int, input().split())) for i in range(n)]
dp = [[0]*(m+1) for i in range(n+1)]
k = int(input())
commands = [list(map(int, input().split())) for i in range(k)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + brd[i][j]

for command in commands:
    i, j, x, y = command
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])
