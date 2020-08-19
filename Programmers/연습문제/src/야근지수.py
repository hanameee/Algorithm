import heapq


def solution(n, works):
    q = []
    for work in works:
        heapq.heappush(q, [-work, work])
    for _ in range(n):
        if not q:
            return 0
        target = heapq.heappop(q)
        target[0] += 1
        target[1] -= 1
        if target[1] != 0:
            heapq.heappush(q, target)
    answer = 0
    for priority, number in q:
        answer += (number**2)
    return answer


print(solution(3, [1, 1]))
