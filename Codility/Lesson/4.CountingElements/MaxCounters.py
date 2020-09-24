def solution(N, A):
    arr = [0]*N
    max_num = 0
    base_limit = 0
    for i in A:
        if i == N+1:
            base_limit = max_num
        else:
            if arr[i-1] < base_limit:
                arr[i-1] = base_limit
            arr[i-1] += 1
            if arr[i-1] > max_num:
                max_num = arr[i-1]
    for i in range(len(arr)):
        if arr[i] < base_limit:
            arr[i] = base_limit
    return arr