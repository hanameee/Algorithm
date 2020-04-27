from collections import deque
import sys
input = sys.stdin.readline

q = deque([])
n = int(input())
q_len = 0
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        q.append(command[1])
        q_len += 1
    elif command[0] == "pop":
        if q:
            print(q.popleft())
            q_len -= 1
        else:
            print(-1)
    elif command[0] == "size":
        print(q_len)
    elif command[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif command[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
