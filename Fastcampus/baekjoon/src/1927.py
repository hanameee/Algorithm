import heapq
import sys
heap = []
N = int(sys.stdin.readline())
for i in range(N):
    command = int(sys.stdin.readline())
    if command != 0:
        heapq.heappush(heap, command)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
