import sys
input = sys.stdin.readline


def memoization(rocks):
    a, b, c = sorted(rocks)
    memory[a][b][c] = True
    return


def play_game(rocks):
    global result
    a, b, c = sorted(rocks)
    if memory[a][b][c]:
        return
    if a == b and b == c:
        result = 1
        return
    else:
        rocks_list = [[2*a, b-a, c], [2*a, b, c-a], [a, 2*b, c-b]]
        memoization(rocks_list[0])
        play_game(rocks_list[0])
        memoization(rocks_list[1])
        play_game(rocks_list[1])
        memoization(rocks_list[2])
        play_game(rocks_list[2])


data = list(map(int, input().split()))
sum_data = sum(data)
result = 0
if sum_data % 3 != 0:
    print(0)
    sys.exit(0)
else:
    memory = [[[False]*1001]*501]*501
a, b, c = data
play_game([a, b, c])
print(result)
