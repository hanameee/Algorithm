def solution(dirs):
    directions = {"U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}
    opposite_dir = {"U": "D", "D": "U", "R": "L", "L": "R"}
    mp_dict = {"U": [[0]*11 for _ in range(11)],
               "D": [[0]*11 for _ in range(11)],
               "R": [[0]*11 for _ in range(11)],
               "L": [[0]*11 for _ in range(11)]}
    curr_location = [5, 5]
    answer = 0
    for dir in dirs:
        [x, y] = curr_location
        dx, dy = directions[dir]
        nx, ny = dx+x, dy+y
        if nx < 0 or ny < 0 or nx > 10 or ny > 10:
            continue
        curr_location = [nx, ny]
        if mp_dict[dir][x][y] or mp_dict[opposite_dir[dir]][nx][ny]:
            continue
        mp_dict[dir][x][y] = 1
        mp_dict[opposite_dir[dir]][nx][ny] = 1
        answer += 1
    return answer
