def solution(board, moves):
    stack = []
    count = 0
    for m in moves:
        block = 0
        for i in range(len(board)):
            if board[i][m-1] != 0:
                block = board[i][m-1]
                board[i][m-1] = 0
                break
        if block:
            if stack:
                if stack[-1] == block:
                    stack.pop()
                    count += 2
                    continue
            stack.append(block)
    answer = count
    return answer


solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
    4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4])  # 4
