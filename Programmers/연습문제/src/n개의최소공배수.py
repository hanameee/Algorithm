# get_primes
def get_primes(n):
    arr = [0, 0] + [1]*(n-1)
    for i in range(2, int(n**0.5)+1):
        if not arr[i]:
            continue
        j = 2
        while i*j <= n:
            arr[i*j] = 0
            j += 1
    result_arr = []
    for _ in range(2, n+1):
        if arr[_]:
            result_arr.append(_)
    return(result_arr)


def get_divisor(n):
    for prime in prime_arr:
        if n % prime == 0:
            i = 1
            n = n//prime
            while n % prime == 0:
                n = n//prime
                i += 1
            if prime in divisor_dict and divisor_dict[prime] >= i:
                continue
            else:
                divisor_dict[prime] = i
        if prime > n:
            return


def solution(arr):
    global divisor_dict, prime_arr
    prime_arr = get_primes(100)
    divisor_dict = {}
    for num in arr:
        get_divisor(num)
    answer = 1
    for key in divisor_dict.keys():
        answer *= key**divisor_dict[key]
    return answer


print(solution([2, 6, 8, 14]))

get_divisor(100)
