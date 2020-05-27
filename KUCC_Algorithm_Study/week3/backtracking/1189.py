r, c, k = map(int, input().split())
mp = [list(input().strip()) for i in range(r)]
ck = [[0]*c for i in range(r)]
ck[r-1][0] = 1
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
count = 0


def dfs(x, y, length, ck, mp):
    global k, count
    if length > k:
        return
    if x == 0 and y == c-1:
        if length == k:
            count += 1
    for dx, dy in directions:
        nx = dx+x
        ny = dy+y
        if nx < 0 or nx > r-1 or ny < 0 or ny > c-1 or mp[nx][ny] == "T" or ck[nx][ny]:
            continue
        else:
            ck[nx][ny] = 1
            length += 1
            dfs(nx, ny, length, ck, mp)
            ck[nx][ny] = 0
            length -= 1
    return


dfs(r-1, 0, 1, ck, mp)
print(count)
