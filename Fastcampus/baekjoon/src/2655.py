import sys
n = int(sys.stdin.readline())
data = [[i] for i in range(n+1)]
dp = [0 for i in range(n+1)]
blocks = [[i] for i in range(n+1)]

data[0] = [0, 0, 0, 0]
for i in range(1, n+1):
    a, h, w = map(int, sys.stdin.readline().split())
    data[i].extend([a, h, w])

data = sorted(data, key=lambda x: x[3])


for i in range(1, n+1):
    dp[i] = data[i][2]  # 원래 dp[i] 는 자기자신
    for j in range(1, i):
        if data[i][1] >= data[j][1]:  # 밑변이 작다면
            dp[i] = max(dp[i], data[i][2] + dp[j])
            if dp[i] == data[i][2] + dp[j]:
                blocks[i] = blocks[j] + [i]
max_height = 0
max_index = 0
for i in range(1, n+1):
    if dp[i] > max_height:
        max_height = dp[i]
        max_index = i

print(len(blocks[max_index]))
for idx in blocks[max_index]:
    print(data[idx][0])
