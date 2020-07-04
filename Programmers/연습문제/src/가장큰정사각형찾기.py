import copy
row_length, column_length = 0, 0


def is_quadrate(i, j, board, dp):
    global row_length, column_length
    if i-1 < 0 or j-1 < 0:
        return board[i][j]
    else:
        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        return dp[i][j]


def solution(board):
    global row_length, column_length
    answer = 0
    row_length = len(board)
    column_length = len(board[0])
    dp = copy.deepcopy(board)
    for i in range(row_length):
        for j in range(column_length):
            if dp[i][j]:
                answer = max(answer, is_quadrate(i, j, board, dp))
    return answer**2


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
