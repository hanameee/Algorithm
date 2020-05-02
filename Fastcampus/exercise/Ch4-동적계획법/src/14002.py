import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 해당 인덱스까지의 최장증가수열의 길이를 저장한다
dp = [1 for i in range(n)]
# 해당 인덱스까지의 최장증가수열을 저장한다
lst = [[i] for i in arr]

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            # dp[j]+1한 값이 현재 dp[i] 보다 클 때만.
            if dp[j] + 1 > dp[i]:
                lst[i] = lst[j] + [arr[i]]
                dp[i] = dp[j] + 1

max_len = 0
max_idx = 0
for i in range(n):
    if max_len < dp[i]:
        max_idx = i
        max_len = dp[i]

print(max_len)
print(*lst[max_idx])
