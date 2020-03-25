import sys

N, k = list(map(int, sys.stdin.readline().split()))
data = list(map(int, sys.stdin.readline().split()))
data.sort()
print(data[k-1])
