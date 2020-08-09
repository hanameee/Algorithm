def solution(s):
    stack = list(s)
    open_needed = 0
    while stack:
        cur = stack.pop()
        if cur == ")":
            open_needed += 1
        else:
            if open_needed < 1:
                return False
            else:
                open_needed -= 1
    if open_needed == 0:
        return True
    else:
        return False


print(solution("()()"))
