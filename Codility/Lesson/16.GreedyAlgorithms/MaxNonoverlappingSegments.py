import heapq


def solution(A, B):
    q = []
    for i in range(len(A)):
        heapq.heappush(q, [B[i], A[i]])
    answer = 0
    end = -1
    while q:
        cur_end, cur_start = heapq.heappop(q)
        if cur_start > end:
            answer += 1
            end = cur_end
    return answer
