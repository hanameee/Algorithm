# 소수 구하기
# def prime_list(n):
#     arr = [1 for i in range(n+1)]
#     arr[0], arr[1] = 0, 0
#     max_limit = int(n**0.5)
#     for i in range(2, max_limit+1):
#         if arr[i]:
#             j = 2
#             while j*i <= n:
#                 arr[j*i] = 0
#                 j += 1
#     for idx in range(n+1):
#         if arr[idx]:
#             print(idx, end=" ")


def find_prime(n):
    min_prime = 2
    prime_list = []
    while True:
        if n % min_prime == 0:
            flag = True
            for p in prime_list:
                if n % p == 0:
                    flag = False
                    break
            if flag:
                prime_list.append(min_prime)
                n = n//min_prime
                if n == 1:
                    return prime_list
        min_prime += 1
    return prime_list


print(find_prime(600851475143))
