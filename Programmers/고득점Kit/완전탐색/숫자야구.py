from itertools import permutations


def compare(A, B):
    strike = 0
    ball = 0
    for idx in range(3):
        if A[idx] in B:
            if A[idx] == B[idx]:
                strike += 1
            else:
                ball += 1
    return [strike, ball]


def solution(baseball):
    perm = permutations(range(1, 10), 3)
    i = 0
    for b in baseball:
        candidate = []
        for p in perm:
            if [b[1], b[2]] == compare(list(map(int, str(b[0]))), p):
                candidate.append(list(p))
        perm = candidate
    return len(perm)


print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))
