import sys
input = sys.stdin.readline
n, k = map(int, input().split())
mp = [0]*n
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
flag = True


def dfs(x, y, num):
    global visited, mp, flag
    visited[x][y] = 1
    need_visit = [(x, y)]
    group = [(x, y)]
    while need_visit:
        current = need_visit.pop()
        c_x, c_y = current
        for i in range(4):
            nx = dx[i]+c_x
            ny = dy[i]+c_y
            if nx < 0 or nx >= n or ny < 0 or ny >= 10:
                continue
            if not visited[nx][ny] and mp[nx][ny] == num:
                need_visit.append((nx, ny))
                visited[nx][ny] = 1
                group.append((nx, ny))
    if len(group) >= k:
        flag = True
        for position in group:
            p_x, p_y = position
            mp[p_x][p_y] = 0


def clear_zero():
    # 세로 한 줄씩 돌면서
    global mp, n
    for y in range(10):
        q = []
        for x in range(n):
            if mp[x][y] != 0:
                q.append(mp[x][y])
        if not q:
            continue
        for x in range(n-len(q)):
            mp[x][y] = 0
        for x in range(n-len(q), n):
            mp[x][y] = q[x-(n-len(q))]


for i in range(n):
    mp[i] = list(map(int, list(input().strip())))

while flag:
    flag = False
    visited = [[0]*10 for _ in range(n)]
    for i in range(n):
        for j in range(10):
            if not visited[i][j] and mp[i][j] != 0:
                dfs(i, j, mp[i][j])
    clear_zero()

for _ in mp:
    print("".join(list(map(str, _))))
