import math
import sys
input = sys.stdin.readline

primes = []


def get_primes(n):
    global primes
    is_primes = [False, False]+[True]*(n-1)
    primes = []
    max_range = int(n**0.5)
    for i in range(2, max_range+1):
        if is_primes[i]:
            for j in range(2*i, n+1, i):
                is_primes[j] = False
    return [i for i in range(2, n+1) if is_primes[i]]


def get_factorization(num):
    global primes
    factors = []
    for prime in primes:
        if num < prime:
            break
        count = 0
        while num % prime == 0:
            num /= prime
            count += 1
        if count > 0:
            factors.append((prime, count))
    return factors


n = int(input())
num_arr = list(map(int, input().split()))
primes = get_primes(1000000)  # 몇 까지의 소수가 필요한가
factorized_num_arr = []
factorized_total = [0]*1000000  # max 소수 = 999983
factorized_total_arr = []


for num in num_arr:
    factorized_num = get_factorization(num)
    for f_num in factorized_num:
        if factorized_total[f_num[0]]:  # 최종 값에 있는 소수면
            factorized_total[f_num[0]] += f_num[1]
        else:
            factorized_total[f_num[0]] = f_num[1]  # 최종 값에 없는 소수면
    factorized_num_arr.append(factorized_num)
for i in range(len(factorized_total)):
    if factorized_total[i]:
        factorized_total_arr.append((i, factorized_total[i]))


gcd = 1
for f_t in factorized_total_arr:
    if f_t[1] >= n:
        gcd *= f_t[0]**(f_t[1]//n)

factorized_gcd = get_factorization(gcd)
total_change_needed = 0


for f_num in factorized_num_arr:
    change_needed = 0
    for g_base, g_exponent in factorized_gcd:
        have_g_base = False
        for f_base, f_exponent in f_num:
            if f_base == g_base:
                have_g_base = True
                if f_exponent < g_exponent:
                    change_needed += g_exponent - f_exponent
                break
        if not have_g_base:
            change_needed += g_exponent
    total_change_needed += change_needed

print(gcd, total_change_needed)
