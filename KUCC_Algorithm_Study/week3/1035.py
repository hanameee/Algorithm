from itertools import combinations
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(curr, target):
    x, y = arr[node_idx]
    for dx, dy in directions:
        nx = dx+x
        ny = dy+y


def is_path(combination):
    arr = list(map(map_position, combination))
    visited = [0]*len(arr)
    for node_idx in len(arr):
        if not visited[node_idx]:
            x, y = arr[node_idx]
            for dx, dy in directions:
                nx = dx+x
                ny = dy+y
    pass


def map_position(num):
    x = num//5
    y = num % 5
    return [x, y]


board = [list(input().strip()) for i in range(5)]
parts_num = 0

for i in range(5):
    for j in range(5):
        if board[i][j] == "*":
            parts_num += 1

position_combination = combinations(range(25), parts_num)
for combination in position_combination:
    if is_path(combination):
        print(combination)
