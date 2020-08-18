from itertools import combinations
def get_primes(n):
    prime_arr = [0,0]+[1]*(n-1)
    for i in range(2,int((n**0.5))+1):
        if prime_arr[i]:
            j = 2
            while i*j <= n:
                prime_arr[i*j] = 0
                j += 1
    return prime_arr


def solution(nums):
    answer = 0
    prime_arr = get_primes(3000)
    num_combination = combinations(nums,3)
    for comb in num_combination:
        if prime_arr[sum(comb)]:
            answer +=1
    return answer