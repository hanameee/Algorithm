# DP로 풀기
def solution(n):
    fib_arr = [0, 1]+[0 for _ in range(99998)]
    if n < 2:
        return fib_arr[n]
    idx = 2
    while idx < n:
        fib_arr[idx] = (fib_arr[idx-1]+fib_arr[idx-2]) % 1234567
        idx += 1
    return (fib_arr[idx-1]+fib_arr[idx-2]) % 1234567
