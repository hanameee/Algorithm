def solution(N, number):
    dp = [set([]) for i in range(8)]
    for idx, s in enumerate(dp):
        s.add(int(str(N)*(idx+1)))
    for i in range(1, 8):
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i-j-1]:
                    dp[i].add(op1+op2)
                    dp[i].add(op1-op2)
                    dp[i].add(op1*op2)
                    if op2 != 0:
                        dp[i].add(op1//op2)
        if number in dp[i]:
            return i+1
    return -1


print(solution(2, 11))
