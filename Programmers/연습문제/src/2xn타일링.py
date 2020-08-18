def solution(n):
    global arr
    arr = [0, 1, 2] + [0]*(n-2)
    if n <= 2:
        return arr[n]
    else:
        i = 3
        while arr[n] == 0:
            arr[i] = arr[i-1]+arr[i-2]
            i += 1
    return arr[n]


print(solution(4))
print(solution(5))
