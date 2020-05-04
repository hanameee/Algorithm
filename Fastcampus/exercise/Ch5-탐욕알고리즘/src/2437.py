import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
idx = 0

for i in range(n):
    if arr[i] <= idx+1:
        idx += arr[i]
    else:
        break
print(idx+1)
