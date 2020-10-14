def solution(n):
    answer = [[0]*i for i in range(1, n+1)]
    direction = 0
    x, y = 0, 0
    num = 1
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            answer[x][y] = num
            num += 1
            print(answer)
            if direction % 3 == 0:
                x += 1
            elif direction % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
        direction += 1
    return answer


print(solution(5))
