import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []

deadline_score = [[] for i in range(n + 1)]
max_deadline = 0
for _ in range(n):
    deadline, score = map(int, input().split())
    deadline_score[deadline].append(score)
    max_deadline = max(deadline, max_deadline)
max_score = 0

for i in range(max_deadline, 0, -1):
    for score in deadline_score[i]:
        heapq.heappush(q, -score)
    if q:
        max_score -= heapq.heappop(q)
print(max_score)
