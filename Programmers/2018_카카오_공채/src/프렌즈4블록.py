# 1:54~


def check_4(board, x, y, checked):
    directions = [(0, 0), (-1, 0), (0, -1), (-1, -1)]
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if board[nx][ny] != board[x][y] or board[nx][y] == False:
            return False
    # 4방향 다 일치한다면
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        checked[nx][ny] = True
    return True


def count_checked(board, checked, m, n):
    count = 0
    for i in range(m):
        for j in range(n):
            if checked[i][j]:
                count += 1
    return count


def dropdown(board, checked, m, n):
    # 한 열씩 떨어뜨린다
    for i in range(n):
        new_column = []
        for j in range(m):
            # 0이 아니라면 column에 쌓고
            if not checked[j][i]:
                new_column.append(board[j][i])
            board[j][i] = 0
        for idx in range(len(new_column)):
            board[m-len(new_column)+idx][i] = new_column[idx]


def solution(m, n, board):
    brd = []
    for i in range(m):
        brd.append(list(board[i]))
    count = 0
    while True:
        flag = False
        checked = [[False]*n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                # 사라질 블록들이 있다면
                if not brd[i][j]:
                    continue
                if check_4(brd, i, j, checked):
                    flag = True
        if flag:
            count += count_checked(brd, checked, m, n)
            # 떨어뜨린다
            dropdown(brd, checked, m, n)
        else:
            break
    answer = count
    return answer
