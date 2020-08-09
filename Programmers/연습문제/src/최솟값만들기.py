def solution(A, B):
    A.sort(key=lambda x: [-x])
    B.sort()
    answer = 0
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer
