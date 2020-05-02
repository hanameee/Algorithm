import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*1001
max_num = 0
data = list(map(int, input().split()))


for i in data:
    dp[i] = i
    dp[i] += max(dp[:i])
    max_num = max(dp[i], max_num)

print(max_num)
