import sys
input = sys.stdin.readline

n = int(input())
answer = input()
bonus_point = 0
total_point = 0
for i in range(n):
    if answer[i] == "O":
        total_point += i+1+bonus_point
        bonus_point += 1
    else:
        bonus_point = 0
print(total_point)
