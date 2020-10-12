def solution(H):
    stk = []
    answer = 0
    for h in H:
        while True:
            if not stk:
                answer += 1
                stk.append(h)
                break
            else:
                if stk[-1] == h:
                    break
                elif stk[-1] <= h:
                    stk.append(h)
                    answer += 1
                    break
                elif stk[-1] > h:
                    stk.pop()
    return answer
