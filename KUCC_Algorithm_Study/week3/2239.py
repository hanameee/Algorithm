import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
board = [list(map(int, list(input().strip()))) for i in range(9)]


def check_row(board, num_arr, x, y):
    for i in range(9):
        if board[i][y]:
            num_arr[board[i][y]-1] = 0
    return


def check_column(board, num_arr, x, y):
    for i in range(9):
        if board[x][i]:
            num_arr[board[x][i]-1] = 0
    return


def check_box(board, num_arr, x, y):
    if x % 3 == 0:
        x_range = [x, x+3]
    elif x % 3 == 1:
        x_range = [x-1, x+2]
    else:
        x_range = [x-2, x+1]
    if y % 3 == 0:
        y_range = [y, y+3]
    elif y % 3 == 1:
        y_range = [y-1, y+2]
    else:
        y_range = [y-2, y+1]
    for i in range(x_range[0], x_range[1]):
        for j in range(y_range[0], y_range[1]):
            if board[i][j]:
                num_arr[board[i][j]-1] = 0
    return


def check(board, i, j):
    if board[i][j]:
        if i == 8 and j == 8:
            for row in board:
                row = map(str, row)
                print("".join(row))
            sys.exit(0)
        if j == 8:
            return check(board, i+1, 0)
        else:
            return check(board, i, j+1)
    num_arr = list(range(1, 10))
    check_row(board, num_arr, i, j)
    check_column(board, num_arr, i, j)
    check_box(board, num_arr, i, j)
    if sum(num_arr) == 0:
        return
    for n in num_arr:
        if n:
            board[i][j] = n
            if i == 8 and j == 8:
                for row in board:
                    row = map(str, row)
                    print("".join(row))
                sys.exit(0)
            if j == 8:
                check(board, i+1, 0)
            else:
                check(board, i, j+1)
            board[i][j] = 0
    return


check(board, 0, 0)
