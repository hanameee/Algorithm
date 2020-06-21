def solution(weight):
    weight.sort()
    cumm_sum = 0
    for w in weight:
        cumm_sum += w
        if cumm_sum-2*w+1 < 0:
            return cumm_sum-w+1


print(solution([1, 1, 1, 1, 1]))
