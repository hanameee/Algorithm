from collections import deque
import sys
from copy import deepcopy
sys.setrecursionlimit(100000)
directions = ["up", "down", "left", "right"]

input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
max_block = 0


def clear_zero(direction, bd):
    global n
    # 위, 아래
    if direction in ["up", "down"]:
        for y in range(n):
            tmp = []
            for x in range(n):
                if bd[x][y] != 0:
                    tmp.append(bd[x][y])
                    bd[x][y] = 0
            for idx in range(len(tmp)):
                if direction == "down":
                    bd[n-len(tmp)+idx][y] = tmp[idx]
                else:
                    bd[idx][y] = tmp[idx]
    # 좌, 우
    else:
        for x in range(n):
            tmp = []
            for y in range(n):
                if bd[x][y] != 0:
                    tmp.append(bd[x][y])
                    bd[x][y] = 0
            for idx in range(len(tmp)):
                if direction == "right":
                    bd[x][n-len(tmp)+idx] = tmp[idx]
                else:
                    bd[x][idx] = tmp[idx]
    return bd


def concat_num(direction, Board):
    global n
    bd = deepcopy(Board)
    bd = clear_zero(direction, bd)
    # 위로 합치기
    if direction in ["up", "down"]:
        merged = [[False]*n for _ in range(n)]
        for y in range(n):
            if direction == "up":
                for x in range(1, n):
                    if not merged[x][y] and bd[x][y] != 0:
                        if bd[x-1][y] == bd[x][y] and not merged[x-1][y]:
                            merged[x-1][y] = True
                            merged[x][y] = True
                            bd[x-1][y] *= 2
                            bd[x][y] = 0
            else:
                for x in range(n-1, 0, -1):
                    if not merged[x][y] and bd[x][y] != 0:
                        if bd[x-1][y] == bd[x][y] and not merged[x-1][y]:
                            merged[x-1][y] = True
                            merged[x][y] = True
                            bd[x][y] *= 2
                            bd[x-1][y] = 0
    else:
        merged = [[False]*n for _ in range(n)]
        for x in range(n):
            if direction == "left":
                for y in range(1, n):
                    if not merged[x][y] and bd[x][y] != 0:
                        if bd[x][y-1] == bd[x][y] and not merged[x][y-1]:
                            merged[x][y-1] = True
                            merged[x][y] = True
                            bd[x][y-1] *= 2
                            bd[x][y] = 0
            else:
                for y in range(n-1, 0, -1):
                    if not merged[x][y] and bd[x][y] != 0:
                        if bd[x][y-1] == bd[x][y] and not merged[x][y-1]:
                            merged[x][y-1] = True
                            merged[x][y] = True
                            bd[x][y] *= 2
                            bd[x][y-1] = 0
    bd = clear_zero(direction, bd)
    return bd


def find_max(bd):
    global n
    max_num = 0
    for x in range(n):
        for y in range(n):
            max_num = max(max_num, bd[x][y])
    return max_num


def dfs(bd, depth):
    global directions, max_block
    if depth > 4:
        max_block = max(max_block, find_max(bd))
        return
    for d in directions:
        b = concat_num(d, bd)
        dfs(b, depth+1)
    return


dfs(board, 0)
print(max_block)
