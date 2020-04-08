# 에라토스테네스의 체
def get_primes(n):
    primes = [False, False] + [True]*(n-1)
    max_range = int(n**0.5)
    for i in range(2, max_range+1):
        if primes[i]:
            for j in range(2*i, n+1, i):
                primes[j] = False
    return [prime for prime in range(2, n+1) if primes[prime]]
