def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    b = 0
    for a in A:
        if a >= B[b]:
            while a >= B[b]:
                b += 1
                if b == len(B):
                    return answer
        answer += 1
        b += 1
        if b == len(B):
            return answer
    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
