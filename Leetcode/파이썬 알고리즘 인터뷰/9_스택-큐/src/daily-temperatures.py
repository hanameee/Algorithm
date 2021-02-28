def solution(t):
    stk = []
    arr = [0]*len(t)
    for idx, v in enumerate(t):
        while stk and stk[-1][1] < v:
            target = stk.pop()
            arr[target[0]] = idx - target[0]
        stk.append([idx, v])
    return arr


print(solution([73, 74, 75, 71, 69, 72, 76, 73]))
