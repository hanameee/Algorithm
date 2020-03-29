import heapq
import sys

heap = list()
n = int(input())
result = 0

for i in range(n):
    data = int(sys.stdin.readline())
    heapq.heappush(heap, data)

if len(heap) <= 1:
    result = heapq.heappop(heap)
else:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    result = a + b

while len(heap) > 0:
    a = heapq.heappop(heap)
    result += result + a

print(result)
