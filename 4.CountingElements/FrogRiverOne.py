def solution(X, A):
    s = set([])
    for i in range(len(A)):
        s.add(A[i])
        if len(s) == X:
            return i
    return -1