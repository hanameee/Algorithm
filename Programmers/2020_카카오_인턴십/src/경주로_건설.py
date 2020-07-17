from collections import deque


def solution(board):
    n = len(board)
    min_cost = [[[float("inf") for _ in range(2)]
                 for _ in range(n)] for _ in range(n)]
    min_cost[0][0] = [0, 0]
    directions = [[1, 0, 0], [-1, 0, 0], [0, 1, 1], [0, -1, 1]]
    queue = deque([[0, 0, 0, 0]])
    while queue:
        [x, y, direction, cost] = queue.popleft()
        if cost > min_cost[x][y][direction]:
            continue
        for dx, dy, direct in directions:
            nx, ny = x+dx, y+dy
            if cost == 0:
                estimated_cost = 100
            else:
                if direction == direct:
                    estimated_cost = cost + 100
                else:
                    estimated_cost = cost + 600
            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1 or board[nx][ny] or estimated_cost > min_cost[nx][ny][direct]:
                continue
            min_cost[nx][ny][direct] = estimated_cost
            queue.append([nx, ny, direct, estimated_cost])
    answer = min(min_cost[n-1][n-1])
    return answer


print(solution(	[[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [
      0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
