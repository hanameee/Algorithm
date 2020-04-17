import sys
import heapq

input = sys.stdin.readline

n = int(input())
data = []
classroom_num = 0
for _ in range(n):
    s, t = map(int, input().split())
    data.append((s, t))
data.sort(key=lambda x: x[1])
while data:
    next_data = []
    cur_data = []
    classroom_num += 1
    cur_data.append(data[0])
    for c in data[1:]:
        if cur_data[-1][1] <= c[0]:
            cur_data.append(c)
        else:
            next_data.append(c)
    data = next_data
    cur_data = []
print(classroom_num)
