n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(1, k+1):
        if j < w:  # 아이템 무게보다 용량이 더 작다면
            dp[i][j] = dp[i-1][j]  # 이전 아이템까지 고려했을때의 최댓값
        else:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])

print(dp[n][k])
