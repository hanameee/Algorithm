from itertools import combinations
from itertools import permutations
import sys
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(idx, arr):
    node = arr[idx]
    node[2] = 1
    for dx, dy in directions:
        nx = dx+node[0]
        ny = dy+node[1]
        if [nx, ny, 0] not in arr:
            continue
        else:
            dfs(arr.index([nx, ny, 0]), arr)
    return


def is_path(arr):
    dfs(0, arr)
    for _ in arr:
        if not _[2]:
            return False
    return True


def map_position(num):
    x = num//5
    y = num % 5
    return [x, y, 0]


board = [list(input().strip()) for i in range(5)]
position = []
parts_num = 0

for i in range(5):
    for j in range(5):
        if board[i][j] == "*":
            position.append([i, j])
            parts_num += 1

min_distance = 1e6


def get_distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


perm = list(permutations(range(len(position)), len(position)))


def get_min_distance(position, arr):
    global perm
    m_distance = 1e6
    for p in perm:
        distance = 0
        for idx in range(len(position)):
            distance += get_distance(position[idx], arr[p[idx]])
        m_distance = min(m_distance, distance)
    return m_distance


position_combination = combinations(range(25), parts_num)
for combination in position_combination:
    arr = list(map(map_position, combination))
    arr.sort()
    if is_path(arr):
        min_distance = min(min_distance, get_min_distance(position, arr))
        if min_distance == 0:
            print(0)
            sys.exit(0)

print(min_distance)
