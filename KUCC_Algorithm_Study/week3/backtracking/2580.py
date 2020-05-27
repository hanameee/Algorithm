import sys
input = sys.stdin.readline
ck_row = [[0]*10 for i in range(9)]
ck_column = [[0]*10 for i in range(9)]
ck_box = [[0]*10 for i in range(9)]
board = [list(map(int, input().strip().split())) for i in range(9)]


for i in range(9):
    for j in range(9):
        if board[i][j]:
            ck_row[i][board[i][j]] = 1
            ck_box[(i//3)*3+(j//3)][board[i][j]]
            if i <= 2:
                ck_box[(j//3)][board[i][j]] = 1
            elif i <= 5:
                ck_box[(j//3)+3][board[i][j]] = 1
            else:
                ck_box[(j//3)+6][board[i][j]] = 1
        if board[j][i]:
            ck_column[i][board[j][i]] = 1


def dfs(x, y):
    if board[x][y]:
        if x == 8 and y == 8:
            for row in board:
                row = map(str, row)
                print(" ".join(row))
            sys.exit(0)
        if y == 8:
            return dfs(x+1, 0)
        else:
            return dfs(x, y+1)
    for i in range(1, 10):
        if ck_row[x][i] or ck_column[y][i] or ck_box[(x//3)*3+(y//3)][i]:
            continue
        board[x][y] = i
        if x == 8 and y == 8:
            for row in board:
                row = map(str, row)
                print(" ".join(row))
            sys.exit(0)
        ck_row[x][i] = 1
        ck_column[y][i] = 1
        ck_box[(x//3)*3+(y//3)][i] = 1
        if y == 8:
            dfs(x+1, 0)
        else:
            dfs(x, y+1)
        board[x][y] = 0
        ck_row[x][i] = 0
        ck_column[y][i] = 0
        ck_box[(x//3)*3+(y//3)][i] = 0
    return


dfs(0, 0)
