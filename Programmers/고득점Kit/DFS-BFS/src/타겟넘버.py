from collections import deque

data = []


def bfs(v, target):
    q = deque([v])
    depth = 0
    number = data[0]
    while q:
        for i in range(len(q)):
            current_node = q.popleft()
            for adj_node in [current_node-number, current_node+number]:
                q.append(adj_node)
        depth += 1
        if depth == len(data):
            break
        else:
            number = data[depth]
    target_number = 0
    for num in q:
        if num == target:
            target_number += 1
    return target_number


def solution(numbers, target):
    global data
    data = numbers
    answer = bfs(0, target)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
