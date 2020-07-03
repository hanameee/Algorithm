from itertools import permutations


def find_primes(n):
    prime_arr = [0, 0] + [1 for i in range(2, n+1)]
    limit = int(n**0.5)+1
    for i in range(2, limit):
        if prime_arr[i]:
            for j in range(2*i, n+1, i):
                prime_arr[j] = 0
    return prime_arr


def solution(numbers):
    max_num = sorted(map(int, list(str(numbers))), key=lambda x: -x)
    max_num = int("".join(map(str, max_num)))
    prime_arr = find_primes(int(max_num))
    permutations_set = set([])
    for i in range(1, len(str(numbers))+1):
        p = permutations(str(numbers), i)
        for _ in p:
            permutations_set.add(int("".join(_)))
    answer = 0
    for p in permutations_set:
        if prime_arr[p]:
            answer += 1
    return answer


print(solution("011"))
