N, r, c = list(map(int, input().split()))


def findWhere(N, r, c):
    result = 0
    if r < pow(2, N-1) and c < pow(2, N-1):
        return 0
    elif r < pow(2, N-1) and c >= pow(2, N-1):
        return 1
    elif r >= pow(2, N-1) and c < pow(2, N-1):
        return 2
    else:
        return 3


def solution(N, r, c):
    result = 0
    while N > 1:
        section = findWhere(N, r, c)
        result += (pow(2, 2*N-2) * section)
        if section == 1:
            c -= pow(2, N-1)
        elif section == 2:
            r -= pow(2, N-1)
        elif section == 3:
            r -= pow(2, N-1)
            c -= pow(2, N-1)
        N -= 1
    result += findWhere(N, r, c)
    return result


print(solution(N, r, c))
