def solution(s):
    stk = []
    for char in s:
        if stk:
            if stk[-1] == char:
                stk.pop()
                continue
        # 항상 append 해줘야 함.
        stk.append(char)
    if len(stk) == 0:
        return True
    return False


print(solution("baaab"))
