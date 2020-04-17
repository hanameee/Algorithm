dp = [-1]*5100
dp[3] = 1
dp[5] = 1

target = int(input())
for i in range(3, 5001):
    if dp[i] != -1:
        if i == target:
            print(dp[i])
            break
        if dp[i+3] == -1:
            dp[i+3] = dp[i]+1
        if dp[i+5] == -1:
            dp[i+5] = dp[i]+1
if dp[target] == -1:
    print(-1)
