import math

def solution(X, Y, D):
    gap = Y-X
    return math.ceil(gap/D)