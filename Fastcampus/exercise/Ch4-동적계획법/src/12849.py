adj = [[] for i in range(8)]
adj[0] = [1, 2]
adj[1] = [0, 2, 3]
adj[2] = [0, 1, 3, 5]
adj[3] = [1, 2, 4, 5]
adj[4] = [3, 5, 6]
adj[5] = [2, 3, 4, 7]
adj[6] = [4, 7]
adj[7] = [5, 6]

# dp[i][j] = 시작점과 j사이의 길이 n인 경로의 수
graph = [[0]*8 for i in range(8)]
d = int(input())
dp = [[0]*8 for i in range(d+1)]

# 모든 지점들에 대해 연결된 간선 1로 표시
for i in range(8):
    for j in adj[i]:
        graph[i][j] = 1

# 0과 연결된 지점들에 대해 dp[1][근접노드] = 1 (시작점과 인접노드 사이의 길이는 1)
for adj_0 in adj[0]:
    dp[1][adj_0] = 1

# 2초부터, n초까지
for i in range(2, d+1):
    # 모든 노드들에 대해
    for j in range(0, 8):
        # dp[i][j] = dp[i-1][인접노드들]
        for k in adj[j]:
            dp[i][j] += dp[i-1][k]
        dp[i][j] = dp[i][j] % 1000000007

print((dp[d-1][1] + dp[d-1][2]) % 1000000007)
