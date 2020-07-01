import heapq


def solution(jobs):
    heapq.heapify(jobs)
    candidate_queue = []
    curr_time = jobs[0][0]
    answer = []
    while candidate_queue or jobs:
        if candidate_queue:
            target = heapq.heappop(candidate_queue)
            curr_time += target[0]
            answer.append(curr_time-target[1])
            while True:
                if jobs and jobs[0][0] <= curr_time:
                    heapq.heappush(candidate_queue, heapq.heappop(jobs)[::-1])
                else:
                    break
        else:
            target = heapq.heappop(jobs)
            curr_time = target[0]+target[1]
            answer.append(target[1])
            while True:
                if jobs and jobs[0][0] <= curr_time:
                    heapq.heappush(candidate_queue, heapq.heappop(jobs)[::-1])
                else:
                    break
    return sum(answer)//len(answer)


print(solution([[0, 3], [1, 9], [2, 6]]	))  # 9
