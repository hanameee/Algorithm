def solution(n, times):
    min_value = min(times)
    l, r, mid = 0, min_value*n, 0
    answer = r
    while l <= r:
        mid = (l+r)//2
        count = 0
        for time in times:
            count += mid//time
        if count > n:
            r = mid-1
            answer = min(answer, mid)
        elif count <= n:
            if count < n:
                l = mid+1
            else:
                answer = min(answer, mid)
                r = mid-1
    return answer


print(solution(11, [3, 4, 10]))
print(solution(6, [4, 10]))  # 20
print(solution(6, [7, 10]))  # 28
print(solution(10, [1, 5]))
print(solution(2, [1, 2, 2, 2, 100]))
