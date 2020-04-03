import sys
from collections import deque


def catch():
    time = 0
    limit = 200000
    visited = [[0]*2 for i in range(limit+1)]
    c, b = map(int, sys.stdin.readline().split())
    q = deque()
    q.append((b, 0))
    while 1:
        c += time
        if c > limit:
            return -1
        if visited[c][time % 2]:
            return time
        for i in range(len(q)):
            current = q.popleft()
            current_position = current[0]
            next_time = (current[1]+1) % 2
            for next_position in [current_position-1, current_position+1, current_position*2]:
                if next_position <= limit and next_position >= 0 and not visited[next_position][next_time]:
                    visited[next_position][next_time] = True
                    q.append((next_position, next_time))
        time += 1


print(catch())


# def solve(conyPosition, brownPosition):
#     time = 0
#     visit = [[0]*2 for _ in range(200001)]
#     q = deque()
#     q.append((brownPosition, 0))

#     while 1:
#         conyPosition += time
#         if conyPosition > 200000:
#             return -1
#         if visit[conyPosition][time % 2]:
#             return time
#         for i in range(0, len(q)):
#             current = q.popleft()
#             currentPosition = current[0]
#             newTime = (current[1]+1) % 2

#             newPosition = currentPosition - 1
#             if newPosition >= 0 and not visit[newPosition][newTime]:
#                 visit[newPosition][newTime] = True
#                 q.append((newPosition, newTime))

#             newPosition = currentPosition + 1
#             if newPosition < 200001 and not visit[newPosition][newTime]:
#                 visit[newPosition][newTime] = True
#                 q.append((newPosition, newTime))

#             newPosition = currentPosition * 2
#             if newPosition < 200001 and not visit[newPosition][newTime]:
#                 visit[newPosition][newTime] = True
#                 q.append((newPosition, newTime))
#         time += 1


# print(solve(11, 2))
