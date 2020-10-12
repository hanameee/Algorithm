def solution(A, B):
    stk = []
    for idx in range(len(B)-1, -1, -1):
        if B[idx] == 0:
            stk.append((0, A[idx]))
        else:
            eaten = False
            while stk and stk[-1][0] == 0:
                if stk[-1][1] < A[idx]:
                    stk.pop()
                else:
                    eaten = True
                    break
            if not eaten or stk[-1][0] == 1:
                stk.append((1, A[idx]))
    return len(stk)
