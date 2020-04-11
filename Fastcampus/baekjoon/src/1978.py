n = int(input())
data = []
data = list(map(int, input().split()))
data.sort()
result = 0


def get_primes(n):
    is_prime = [False, False] + [True]*(n+1)
    max_range = int(n**0.5)
    for i in range(2, max_range+1):
        if is_prime[i]:
            for j in range(i*2, n+1, i):
                is_prime[j] = False
    return [prime for prime in range(2, n+1) if is_prime[prime]]


primes = get_primes(data[-1])
for number in data:
    if number in primes:
        result += 1

print(result)
