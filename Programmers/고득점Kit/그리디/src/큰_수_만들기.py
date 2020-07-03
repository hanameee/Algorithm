import heapq


def solution(number, k):
    number = list(map(int, list(str(number))))
    n = len(number)
    answer = ""
    minHeap = []
    for idx in range(0, k+1):
        heapq.heappush(minHeap, [-number[idx], idx])
    num, num_idx = heapq.heappop(minHeap)
    answer += str(-num)
    max_idx = num_idx
    for i in range(1, n-k):
        heapq.heappush(minHeap, [-number[k+i], k+i])
        while len(minHeap):
            num, num_idx = heapq.heappop(minHeap)
            if num_idx > max_idx:
                answer += str(-num)
                max_idx = num_idx
                break
    return answer
