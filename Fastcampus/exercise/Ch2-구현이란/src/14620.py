import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
mp = [list(map(int, input().split())) for i in range(n)]
dx, dy = [0, 1, -1, 0, 0], [0, 0, 0, 1, -1]
price = [[0]*n for i in range(n)]
sorted_price = []
result = 10000


def is_available_combination(combination):
    visited = [[0]*n for i in range(n)]
    for data in combination:
        price, x, y = data
        for d in range(5):
            nx = x+dx[d]
            ny = y+dy[d]
            if visited[nx][ny] != -1:
                visited[nx][ny] = -1
            else:
                return False
    return True


for i in range(1, n-1):
    for j in range(1, n-1):
        p = 0
        for d in range(5):
            nx = i+dx[d]
            ny = j+dy[d]
            p += mp[nx][ny]
        price[i][j] = p
        sorted_price.append((price[i][j], i, j))
sorted_price.sort()

for combination in combinations(sorted_price, 3):
    if is_available_combination(combination):
        a, b, c = combination
        result = min(result, a[0]+b[0]+c[0])

print(result)
