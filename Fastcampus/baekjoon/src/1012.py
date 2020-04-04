from collections import deque

t = int(input())


def bfs(plant):
    global worm
    worm += 1
    q = deque()
    q.append(plant)
    while q:
        x, y = q.popleft()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < m and 0 <= ny < n:
                if plants[nx][ny] and not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
    return


for test_case in range(t):
    m, n, k = map(int, input().split())
    visited = [[0]*n for i in range(m)]
    q = deque([])
    plants = [[0]*n for i in range(m)]
    worm = 0
    for i in range(k):
        x, y = map(int, input().split())
        visited[x][y] = 0
        plants[x][y] = 1

    for i in range(m):
        for j in range(n):
            if plants[i][j] and not visited[i][j]:
                visited[i][j] = 1
                bfs([i, j])

    print(worm)
