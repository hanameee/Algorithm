def solution(prices):
    n = len(prices)
    answer = [0 for i in range(n)]
    stk = []
    for idx in range(n):
        while(stk and prices[idx] < prices[stk[-1]]):
            answer[stk[-1]] = idx-stk[-1]
            stk.pop()
        stk.append(idx)
    while stk:
        answer[stk[-1]] = n-1-stk[-1]
        stk.pop()
    return answer


print(solution([1, 2, 3, 2, 3]))
