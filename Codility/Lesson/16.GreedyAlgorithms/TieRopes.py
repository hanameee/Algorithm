from collections import deque


def solution(K, A):
    answer = 0
    A = deque(A)
    while A:
        cur = A.popleft()
        if cur >= K:
            answer += 1
            continue
        else:
            while A:
                cur2 = A.popleft()
                cur += cur2
                if cur >= K:
                    answer += 1
                    break
    return answer
