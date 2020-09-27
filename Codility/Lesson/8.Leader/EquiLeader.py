import collections


def solution(A):
    if len(A) == 0:
        return -1
    c = collections.Counter(A)
    most_common = c.most_common(1)[0]
    if most_common[1] <= len(A)/2:
        return 0
    count = 0
    answer = 0
    for i in range(0, len(A)):
        if A[i] == most_common[0]:
            count += 1
        if count > (i+1)/2 and most_common[1]-count > (len(A)-(i+1))/2:
            answer += 1
    return answer
