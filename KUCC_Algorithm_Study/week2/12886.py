import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def play_game(rocks):
    global result
    a, b, c = rocks
    if memory[a][b] or a == 0:
        return
    if a == b and b == c:
        print(1)
        sys.exit(0)
    else:
        memory[a][b] = True
        rocks_list = [[2*a, b-a, c], [2*a, b, c-a], [a, 2*b, c-b]]
        rocks_list[0].sort()
        rocks_list[1].sort()
        rocks_list[2].sort()
        play_game(rocks_list[0])
        play_game(rocks_list[1])
        play_game(rocks_list[2])


data = list(map(int, input().split()))
sum_data = sum(data)
result = 0
if sum_data % 3 != 0:
    print(0)
    sys.exit(0)
else:
    memory = [[0]*726 for i in range(726)]
a, b, c = sorted(data)
play_game([a, b, c])
print(result)
