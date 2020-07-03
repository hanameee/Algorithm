import math


def get_gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a = a % b
        a, b = b, a
    return a


def solution(w, h):
    total_rects = w*h
    gcd = get_gcd(w, h)
    if gcd == 1:
        return total_rects - w+h-1
    else:
        return total_rects - ((w//gcd)+(h//gcd)-1)*gcd


print(solution(8, 12))
