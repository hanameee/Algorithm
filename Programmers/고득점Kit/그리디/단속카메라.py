def solution(routes):
    answer = 0
    routes.sort()
    curr_end = -30001
    for car in routes:
        start, end = car
        if start <= curr_end:
            if curr_end > end:
                curr_end = end
            continue
        answer += 1

        curr_end = end
    return answer


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
