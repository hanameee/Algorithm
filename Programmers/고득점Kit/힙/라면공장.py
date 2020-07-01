import heapq


def solution(stock, dates, supplies, k):
    answer = 0
    queue = []
    supply_idx = 0
    while stock < k:
        for i in range(supply_idx, len(supplies)):
            if dates[i] <= stock:
                heapq.heappush(queue, -supplies[i])
                supply_idx = i+1
            else:
                break
        stock += heapq.heappop(queue)*(-1)
        answer += 1
    return answer


print(solution(4, [4, 10, 15], [20, 5, 10], 30))
print(solution(4, [4], [20], 15))
