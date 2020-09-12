def solution(n, money):
    money = money
    dp = [[0]*(n+1) for _ in range(len(money))]
    for i in range(len(money)):
        dp[i][0] = 1
    for i in range(money[0], n+1, money[0]):
        dp[0][i] = 1
    for i in range(1, len(money)):
        for j in range(n+1):
            if money[i] > j:
                dp[i][j] = dp[i-1][j]
            if money[i] <= j:
                dp[i][j] = (dp[i-1][j]+dp[i][j-money[i]]) % 1000000007
    for _ in dp:
        print(_)
    return dp[-1][-1]


print(solution(5, [1, 2, 5]))
