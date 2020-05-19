n, E, W, S, N = map(int, input().split())
ck = [[0]*(2*n+1) for i in range(2*n+1)]
directions = [(1, 0, 0), (-1, 0, 1), (0, -1, 2), (0, 1, 3)]
total_prob = 0
ck[n][n] = 1
ck[n+1][n] = 1
prob_arr = [[E, W, S, N], [W, S, N, E], [S, N, E, W], [N, E, W, S]]


def dfs(x, y, path, ck):
    global total_prob, n
    if len(path) == n:
        for pa in prob_arr:
            prob = 1
            for p in path:
                prob *= pa[p]/100
            total_prob += prob
    for dx, dy, p in directions:
        nx = x + dx
        ny = y + dy
        if not prob_arr[0][p] or nx < 0 or nx > 2*n or ny < 0 or ny > 2*n or ck[nx][ny]:
            continue
        ck[nx][ny] = 1
        path.append(p)
        dfs(nx, ny, path, ck)
        ck[nx][ny] = 0
        path.pop()
    return


dfs(n, n, [0], ck)
print(total_prob)
