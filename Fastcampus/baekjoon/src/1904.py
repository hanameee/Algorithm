import sys
n = int(sys.stdin.readline())

data = [0 for i in range(n+1)]

for i in range(1, n+1):
    if i <= 2:
        data[i] = i % 15746
    else:
        data[i] = (data[i-1] + data[i-2]) % 15746

print(data[n])
