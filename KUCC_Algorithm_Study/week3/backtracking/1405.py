n, E, W, S, N = map(int, input().split())
E /= 100
W /= 100
S /= 100
N /= 100

ck = [[0]*(2*n+1) for i in range(2*n+1)]
directions = [(0, 1, E), (0, -1, W), (-1, 0, S), (1, 0, N)]
total_prob = 0
ck[n][n] = 1


def dfs(x, y, depth, ck, prob):
    global total_prob, n
    if depth == n:
        total_prob += prob
        return
    for dx, dy, p in directions:
        nx = x + dx
        ny = y + dy
        if not p or ck[nx][ny] or nx < 0 or nx > 2*n or ny < 0 or ny > 2*n:
            continue
        ck[nx][ny] = 1
        dfs(nx, ny, depth+1, ck, prob*p)
        ck[nx][ny] = 0
    return


dfs(n, n, 0, ck, 1)
print(total_prob)
