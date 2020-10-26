def solution(s):
    stk = []
    for char in s:
        if stk:
            if stk[-1] == char:
                stk.pop()
                continue
        # early return 안되면 항상 append 해줘야 함. 분기문 주의
        stk.append(char)
    if len(stk) == 0:
        return True
    return False


print(solution("baaab"))
