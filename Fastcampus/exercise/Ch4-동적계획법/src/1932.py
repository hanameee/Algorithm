import sys
from copy import deepcopy
input = sys.stdin.readline
n = int(input())
mp = [list(map(int, input().split())) for i in range(n)]
dp = deepcopy(mp)

for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + mp[i][j]
        elif j == len(dp[i])-1:
            dp[i][j] = dp[i-1][j-1] + mp[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + mp[i][j]

print(max(dp[-1]))
