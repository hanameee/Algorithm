def solution(arrangement):
    stack = []
    count = 0
    answer = 0
    for idx in range(len(arrangement)):
        if arrangement[idx] == "(":
            count += 1
        else:
            if arrangement[idx-1] == "(":
                count -= 1
                answer += count
            else:
                count -= 1
                answer += 1
    return answer


print(solution("()(((()())(())()))(())"))
