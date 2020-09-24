def solution(A):
    A.sort()
    try:
        start_idx = A.index(1)
    except ValueError:
        return 1
    for i in range(start_idx+1, len(A)):
        if A[i] > A[i-1]+1:
            return A[i-1]+1
    return A[-1]+1