import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
cumm = 0
for i in range(n):
    data[i] = data[i]*(i+1)-cumm
    cumm += data[i]
print((" ").join(list(map(str, data))))
