import sys
import heapq

input = sys.stdin.readline

n = int(input())
data = []
q = []
for _ in range(n):
    s, t = map(int, input().split())
    data.append((s, t))
data.sort(key=lambda x: x[0])
heapq.heappush(q, data[0][1])
for c in data[1:]:
    if c[0] >= q[0]:
        heapq.heappop(q)
    heapq.heappush(q, c[1])
print(len(q))
