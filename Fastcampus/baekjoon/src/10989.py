import sys

N = int(sys.stdin.readline())
data = [0] * 10001
for i in range(N):
    target = int(sys.stdin.readline())
    data[target] += 1

for i in range(10001):
    if data[i] != 0:
        for j in range(data[i]):
            print(i)
