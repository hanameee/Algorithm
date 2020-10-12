def solution(S):
    if len(S) == 0:
        return 1
    matching_map = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stk = []
    for s in S:
        if s in ["(", "{", "["]:
            stk.append(s)
        else:
            if not stk:
                return 0
            elif stk[-1] == matching_map[s]:
                stk.pop()
    if len(stk) != 0:
        return 0
    else:
        return 1
