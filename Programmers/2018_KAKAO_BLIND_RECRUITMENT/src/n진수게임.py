# -*- coding: utf-8 -*-
# def get(number, n):
#     result = ""
#     while number != 0:
#         q = str(hex(number % n)[2].upper())
#         number = number//n
#         result = q + result
#     return result


# def solution(n, t, m, p):
#     answer = ''
#     number = 0
#     idx = 0
#     for i in range(t):
#         target_idx = p+i*m
#         if target_idx <= n:
#             answer += str(hex(target_idx-1))[2].upper()
#         else:
#             number = n
#             target_idx -= n
#             j = 2
#             while target_idx >= j*(n-1)*pow(n, j-1):
#                 number += (n-1)*pow(n, j-1)
#                 target_idx -= j*(n-1)*pow(n, j-1)
#                 j += 1
#             number += target_idx//j
#             idx = target_idx % j
#             if idx == 0:
#                 answer += get(number-1, n)[-1]
#             else:
#                 answer += get(number, n)[idx-1]
#     return answer

# 10진수를 2~16진수로 변환하는 함수
def baseConv(n, num):
    if num == 0:
        return "0"
    t = "0123456789ABCDEF"
    ret = ""
    while num > 0:
        ret += t[int(num % n)]
        num = int(num/n)

    return ret[::-1]


def solution(n, t, m, p):
    answer = ""
    num = 0
    i = 0  # 턴 계산하는 변수

    while True:
        cur = baseConv(n, num)
        print(cur, i)
        # 0부터 시작해서 플레이어 턴마다 리스트에 넣어줌
        for ch in cur:
            if i % m == p-1:
                answer += ch
                t -= 1
            if t == 0:
                return answer
            i += 1
        num += 1


# print(solution(5, 10, 10, 1))
print(solution(16, 16, 2, 2))
