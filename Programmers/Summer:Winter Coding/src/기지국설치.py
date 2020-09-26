import math


def solution(n, stations, w):
    start_idx = 0
    answer = 0
    gap = w*2+1
    for station in stations:
        if start_idx >= n:
            break
        end_idx = station-1-w-1
        if start_idx > end_idx:
            start_idx = station+w
            continue
        else:
            answer += math.ceil((end_idx-start_idx+1)/gap)
            start_idx = station+w
    if start_idx < n:
        answer += math.ceil((n-start_idx)/gap)
    return answer


print(solution(16, [9], 2))
