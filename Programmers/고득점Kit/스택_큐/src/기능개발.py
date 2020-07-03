import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    date = deque([math.ceil((100-progresses[i])/speeds[i])
                  for i in range(len(speeds))])
    cumulate_num = 0
    while date:
        curr_date = date.popleft()
        cumulate_num += 1
        while date:
            next_date = date[0]
            if curr_date >= next_date:
                date.popleft()
                cumulate_num += 1
            else:
                answer.append(cumulate_num)
                cumulate_num = 0
                break
    if cumulate_num:
        answer.append(cumulate_num)
    return answer


print(solution([93, 30, 55], [1, 30, 50]))
