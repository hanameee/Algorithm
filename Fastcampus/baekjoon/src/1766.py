import heapq

n, m = map(int, input().split())
priority = [[] for i in range(n+1)]

indegree = [0 for i in range(n+1)]

for i in range(1, m+1):
    A, B = map(int, input().split())
    priority[A].append(B)
    indegree[B] += 1

result = []

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(result, i)

while result:
    popped = heapq.heappop(result)
    print(popped)
    for j in priority[popped]:
        indegree[j] -= 1
        if indegree[j] == 0:
            heapq.heappush(result, j)
