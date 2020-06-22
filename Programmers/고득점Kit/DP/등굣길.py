def solution(m, n, puddles):
    mp = [[0]*(m+1) for i in range(n+1)]
    for x, y in puddles:
        mp[y][x] = -1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                mp[i][j] = 1
                continue
            if mp[i][j] == -1:
                mp[i][j] = 0
                continue
            mp[i][j] = (mp[i-1][j] + mp[i][j-1]) % 1000000007
    answer = (mp[n][m]) % 1000000007
    return answer


print(solution(4, 3, [[2, 2]]))
