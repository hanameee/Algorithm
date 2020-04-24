from collections import deque
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
cache = [['' for _ in range(c)] for _ in range(r)]


def bfs(x, y):
    q = deque([(x, y, board[x][y])])
    ans = 0
    while q:
        x, y, path = q.popleft()
        flag = False
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x+dx, y+dy
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if board[nx][ny] not in path:
                flag = True
                if cache[nx][ny] != path + board[nx][ny]:
                    cache[nx][ny] = path + board[nx][ny]
                    q.append((nx, ny, cache[nx][ny]))
        if not flag:
            ans = max(ans, len(path))
    return ans


print(bfs(0, 0))
