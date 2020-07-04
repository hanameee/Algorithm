def solution(n):
    answer = 1
    for i in range(1, (n//2)+1):
        sum_value = i
        j = i
        while sum_value <= n:
            j += 1
            sum_value += j
            if sum_value == n:
                answer += 1
                break
    return answer


print(solution(15))
