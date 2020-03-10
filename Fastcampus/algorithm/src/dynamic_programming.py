# 재귀 함수 활용
def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


# 동적 계획법 활용
def dp_fibonacci(n):
    cache = [0 for i in range(n+1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, n + 1):
        cache[index] = cache[index-1] + cache[index-2]
    return cache[n]


print(recursive_fibonacci(10))
print(dp_fibonacci(10))
