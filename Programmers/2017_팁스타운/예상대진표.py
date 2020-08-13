def solution(n, a, b):
    i = 1
    while True:
        if abs((a+1)//2-(b+1)//2) == 0:
            return i
        a = (a+1)//2
        b = (b+1)//2
        i += 1


print(solution(8, 7, 8))
