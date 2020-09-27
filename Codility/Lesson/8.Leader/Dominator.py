import collections


def solution(A):
    if len(A) == 0:
        return -1
    c = collections.Counter(A)
    most_common = c.most_common(1)[0]
    if most_common[1] <= len(A)/2:
        return -1
    else:
        return A.index(most_common[0])
