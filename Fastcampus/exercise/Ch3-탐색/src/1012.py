import sys
input = sys.stdin.readline

t = int(input())
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def search(x, y):
    visited[x][y] = 1
    need_visit = [(x, y)]
    while need_visit:
        current_place = need_visit.pop()
        c_x, c_y = current_place
        for i in range(4):
            nx = c_x+dx[i]
            ny = c_y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            else:
                if mp[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    need_visit.append((nx, ny))
    return True


for _ in range(t):
    m, n, k = map(int, input().split())
    visited = [[0]*m for i in range(n)]
    position_lst = []
    result = 0
    mp = [[0]*m for i in range(n)]
    for i in range(k):
        y, x = map(int, input().split())
        mp[x][y] = 1
        position_lst.append((x, y))
    for position in position_lst:
        position_x, position_y = position
        if not visited[position_x][position_y]:
            search(position_x, position_y)
            result += 1
    print(result)
