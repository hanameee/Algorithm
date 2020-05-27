import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for i in range(n)]
combi = list(combinations(range(n), n//2))
iter_idx = list(combinations(range(n//2), 2))
min_diff = 1e9

for i in range(n):
    for j in range(i+1, n):
        board[i][j] += board[j][i]

for start_combi in combi:
    start_sum = 0
    link_sum = 0
    link_combi = list(set(range(n)) - set(start_combi))
    for i, j in iter_idx:
        start_sum += board[start_combi[i]][start_combi[j]]
        link_sum += board[link_combi[i]][link_combi[j]]
    min_diff = min(min_diff, abs(start_sum-link_sum))
    if min_diff == 0:
        break

print(min_diff)
