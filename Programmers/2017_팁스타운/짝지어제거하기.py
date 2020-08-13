def solution(s):
    stk = []
    for char in s:
        if stk:
            if stk[-1] == char:
                stk.pop()
                continue
        stk.append(char)
    if len(stk) == 0:
        return True
    return False


print(solution("baaab"))
