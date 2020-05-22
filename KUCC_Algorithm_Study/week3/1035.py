from collections import deque


board = [list(input().strip()) for i in range(5)]
candidate_list = []
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def calculate_distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


def bfs(need_visit, target, visited):
    global board, directions
    while need_visit:
        x, y, path = need_visit.popleft()
        if [x, y] in target:
            print(path)
            if len(path) < 2:
                return [0, [x, y]]
            return [len(path)-2, path[-2]]
        for dx, dy in directions:
            nx = dx+x
            ny = dy+y
            if nx < 0 or ny < 0 or nx > 4 or ny > 4 or [nx, ny] in path:
                continue
            need_visit.append([nx, ny, path+[[nx, ny]]])


for i in range(5):
    for j in range(5):
        if board[i][j] == "*":
            candidate_list.append([i, j])

distances = []
for i in range(len(candidate_list)):
    distance = 0
    for j in range(len(candidate_list)):
        if j != i:
            distance += calculate_distance(
                candidate_list[i], candidate_list[j])
    candidate_list[i].append(distance)

candidate_list.sort(key=lambda x: x[2])
target = [[candidate_list[0][0], candidate_list[0][1]]]
total_length = 0

for candidate in candidate_list[1:]:
    need_visit = deque(
        [[candidate[0], candidate[1], [[candidate[0], candidate[1]]]]])
    visited = [[0]*5 for i in range(5)]
    length, last_position = bfs(need_visit, target, visited)
    total_length += length
    target.append([last_position[0], last_position[1]])

print(total_length)
