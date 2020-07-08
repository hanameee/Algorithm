from collections import deque
from copy import deepcopy


def solution(board):
    global answer, directions
    answer = float("inf")
    n = len(board)
    min_cost = [[float("inf")]*n for _ in range(n)]
    queue = deque([[0, 0, "", 0, visited]])
    directions = [[0, -1, "H"], [0, 1, "H"], [1, 0, "V"], [-1, 0, "V"]]
    if cost > min_cost[x][y]:
        continue
    else:
        min_cost[x][y] = cost
    if answer != float("inf") and cost > answer:
        continue
    if x == n-1 and y == n-1:
        answer = min(answer, cost)
        continue
    visited[x][y] = 1
    for dx, dy, direction in directions:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1 or visited[nx][ny] or board[nx][ny]:
            continue
        if path == "":
            next_cost = cost + 100
        elif direction != path:
            next_cost = cost + 600
        else:
            next_cost = cost + 100
        if next_cost > min_cost[nx][ny]:
            continue
        else:
            min_cost[nx][ny] = next_cost
        ck = deepcopy(visited)
        ck[nx][ny] = 1
        if path == "":
            queue.append([nx, ny, direction, next_cost, ck])
        elif direction != path:
            queue.append([nx, ny, direction, next_cost, ck])
        else:
            queue.append([nx, ny, direction, next_cost, ck])
    return answer


print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
