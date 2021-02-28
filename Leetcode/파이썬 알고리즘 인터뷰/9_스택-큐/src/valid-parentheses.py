def solution(s):
    s_list = list(s)
    parenthesis_map = {")": "(", "]": "[", "}": "{"}
    stk = []

    for _ in s_list:
        if _ in ["(", "[", "{"]:
            stk.append(_)
        else:
            if stk[-1] == parenthesis_map[_]:
                stk.pop()
            else:
                return False
    if stk:
        return False
    else:
        return True


print(solution("()[]{}"))
print(solution("([)]"))
