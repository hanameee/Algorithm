def solution(A):
    N = len(A)
    A.sort()
    A = list(set(A))
    if A[0] == 1 and A[-1] == N and len(A) == N:
        return 1
    else:
        return 0