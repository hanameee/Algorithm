directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
ck = []
grid = []


def dfs(x, y):
    global ck, grid
    need_visit = [[x, y]]
    while need_visit:
        cur_x, cur_y = need_visit.pop()
        if not ck[cur_x][cur_y]:
            ck[cur_x][cur_y] = 1
            for dx, dy in directions:
                nx = cur_x+dx
                ny = cur_y+dy
                if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                    continue
                if not ck[nx][ny] and grid[nx][ny] == "1":
                    need_visit.append([nx, ny])


def solution(g):
    global ck, grid
    answer = 0
    grid = g
    ck = [[0]*len(grid[0]) for _ in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1" and not ck[row][col]:
                answer += 1
                dfs(row, col)
    return answer


print(solution([["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]]))
