import heapq


def solution(scoville, k):
    heapq.heapify(scoville)
    answer = 0
    while True:
        target = heapq.heappop(scoville)
        if target <= k:
            if len(scoville):
                next_target = heapq.heappop(scoville)
                heapq.heappush(scoville, target+next_target*2)
            else:
                return -1
        else:
            return answer
        answer += 1
    return answer


print(solution([1, 2, 3, 9, 10, 12],	7))
