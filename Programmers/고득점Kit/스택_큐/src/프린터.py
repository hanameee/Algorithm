from collections import deque


def solution(priorities, location):
    deq = deque([[priorities[idx], idx] for idx in range(len(priorities))])
    priority_arr = sorted(priorities, key=lambda x: -x)
    count = 0
    answer = 0
    while deq:
        max_priority = priority_arr[count]
        if deq[0][0] == max_priority:
            answer += 1
            if deq[0][1] == location:
                return answer
            deq.popleft()
            count += 1
        else:
            deq.append(deq.popleft())
    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
