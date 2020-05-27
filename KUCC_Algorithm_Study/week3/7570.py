import sys
input = sys.stdin.readline

n = int(input())
children_num = list(map(int, input().split()))
dp = [0]*1000001
max_dp = 0
for num in children_num:
    dp[num] = dp[num-1]+1
    max_dp = max(dp[num], max_dp)

print(n-max_dp)
