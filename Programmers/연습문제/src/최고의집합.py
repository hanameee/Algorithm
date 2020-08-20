def solution(n, s):
    answer = []
    if s//n < 1:
        return [-1]
    else:
        while n != 0:
            if s % n == 0:
                answer.extend([s//n]*(n))
                return sorted(answer)
            target = s//n
            answer.append(target)
            s -= target
            n -= 1
    return sorted(answer)
