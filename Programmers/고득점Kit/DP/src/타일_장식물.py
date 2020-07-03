def solution(N):
    if N == 1:
        return 1
    elif N == 2:
        return 6
    else:
        len_arr = [1, 1] + [0]*(N-2)
        for i in range(2, N):
            len_arr[i] = len_arr[i-1] + len_arr[i-2]
        answer = 4*len_arr[N-1] + 2*len_arr[N-2]
        return answer


print(solution(6))
