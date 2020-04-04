import sys
n = int(sys.stdin.readline())
cranes = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))

cranes = sorted(cranes, reverse=True)
boxes = sorted(boxes, reverse=True)
moved = [0]*m
positions = [0]*n  # 크레인이 어디까지 옮겼는지 저장


def solution():
    if cranes[0] < boxes[0]:
        return -1
    time = 0
    left = m
    while left > 0:
        for c in range(n):  # 모든 크레인들에 대해서
            while positions[c] < len(boxes):
                if not moved[positions[c]] and boxes[positions[c]] <= cranes[c]:
                    moved[positions[c]] = True
                    positions[c] += 1
                    left -= 1
                    break
                positions[c] += 1
        time += 1
    return time


print(solution())
