def solution(n, a, b):
    i = 1
    while True:
        # 그냥 abs(a-b) == 1하면 안된다. 2,3같은 애들을 못거름.
        if abs((a+1)//2-(b+1)//2) == 0:
            return i
        a = (a+1)//2
        b = (b+1)//2
        i += 1


print(solution(8, 7, 8))
