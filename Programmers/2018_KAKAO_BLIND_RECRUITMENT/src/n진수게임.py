# -*- coding: utf-8 -*-
def get(number, n):
    result = ""
    while number != 0:
        q = str(hex(number % n)[2].upper())
        number = number//n
        result = q + result
    return result


def solution(n, t, m, p):
    answer = ''
    number = 0
    idx = 0
    for i in range(t):
        target_idx = p+i*m
        if target_idx <= n:
            answer += str(hex(target_idx-1))[2].upper()
        else:
            number = n
            target_idx -= n
            j = 2
            while target_idx >= j*(n-1)*pow(n, j-1):
                number += (n-1)*pow(n, j-1)
                target_idx -= j*(n-1)*pow(n, j-1)
                j += 1
            number += target_idx//j
            idx = target_idx % j
            if idx == 0:
                answer += get(number-1, n)[-1]
            else:
                answer += get(number, n)[idx-1]
    return answer


print(solution(5, 10, 10, 1))
# print(solution(16, 16, 2, 2))
