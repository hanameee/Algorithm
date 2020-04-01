import sys

n, s, m = map(int, sys.stdin.readline().split())
v = list(map(int, sys.stdin.readline().split()))

dp = [[False]*(m+1) for _ in range(n+1)]
dp[0][s] = True

result = -1

for i in range(1, n+1):
    flag = 1
    for j in range(m+1):
        if dp[i-1][j] == True:
            if j+v[i-1] <= m:
                dp[i][j+v[i-1]] = True
                flag = 0
            if j-v[i-1] >= 0:
                dp[i][j-v[i-1]] = True
                flag = 0

for volume in range(m, -1, -1):
    if dp[n][volume] == True:
        result = volume
        break

print(result)
