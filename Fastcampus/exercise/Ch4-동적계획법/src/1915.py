from copy import deepcopy
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0]*(m+1)] + [list(map(int, list("0"+input().strip())))
                     for i in range(n)]
dp = deepcopy(arr)
max_size = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if dp[i][j]:
            dp[i][j] = 1+min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
            max_size = max(dp[i][j], max_size)
print(max_size**2)
