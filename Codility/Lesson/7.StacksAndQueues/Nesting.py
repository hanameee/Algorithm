def solution(S):
    if len(S) == 0:
        return 1
    stk = []
    for s in S:
        if s == "(":
            stk.append(s)
        else:
            if not stk:
                return 0
            else:
                if stk[-1] == "(":
                    stk.pop()
    if stk:
        return 0
    else:
        return 1
