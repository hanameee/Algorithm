from collections import deque


def solution(board):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    answer = [0]

    def find_block(x, y, chk, target):
        need_visit = deque([[x, y]])
        min_x, max_x, min_y, max_y = [x, x, y, y]
        while need_visit:
            x, y = need_visit.popleft()
            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board) or chk[nx][ny] or board[nx][ny] != target:
                    continue
                chk[nx][ny] = 1
                min_x, max_x, min_y, max_y = min(nx, min_x), max(nx, max_x), min(ny, min_y), max(ny, max_y)
                need_visit.append([nx, ny])
        return [min_x, max_x, min_y, max_y]

    def is_deleteable(data, target, answer):
        x_m, x_M, y_m, y_M = data
        for i in range(x_m, x_M + 1):
            for j in range(y_m, y_M + 1):
                if board[i][j] == 0:
                    for row in range(0, i + 1):
                        if board[row][j] != 0:
                            return False
                else:
                    if board[i][j] != target:
                        return False
        for i in range(x_m, x_M + 1):
            for j in range(y_m, y_M + 1):
                board[i][j] = 0
        answer[0] += 1
        return True

    while True:
        repeat = False
        ck = [[0] * len(board) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 0 and ck[i][j] == 0:
                    target = board[i][j]
                    data = find_block(i, j, ck, target)
                    repeat = is_deleteable(data, target, answer)
        if not repeat:
            break
    return answer[0]


print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
                [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
                [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))
