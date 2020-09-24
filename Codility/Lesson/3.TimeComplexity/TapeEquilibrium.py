def solution(A):
    cumm = 0
    min_v = float('inf')
    sum_v = sum(A)
    for i in A[:-1]:
        cumm += i
        min_v = min(min_v, abs(sum_v - 2 * cumm))
    return min_v
