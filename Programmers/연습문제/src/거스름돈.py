def solution(n, money):
    money = [0]+money
    dp = [[0]*(n+1) for _ in range(len(money))]
    for i in range(len(money)):
        dp[i][0] = 1
    for i in range(money[1], n+1, money[1]):
        dp[1][i] = 1
    for i in range(2, len(money)):
        for j in range(n+1):
            if money[i] > j:
                dp[i][j] = dp[i-1][j]
            if money[i] <= j:
                dp[i][j] = (dp[i-1][j]+dp[i][j-money[i]]) % 1000000007
    return


solution(5, [1, 2, 5])
