r, c = map(int, input().split())
m = [list(input()) for i in range(r)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
flag = False


for i in range(r):
    for j in range(c):
        if m[i][j] == 'W':
            for w in range(4):
                nx, ny = i+dx[w], j+dy[w]
                if nx < 0 or nx == r or ny < 0 or ny == c:  # 범위 벗어나는 경우
                    continue
                # 늑대와 인접한 곳에 양이 있는 경우
                if m[nx][ny] == "S":
                    flag = True
                    break

if flag:
    print(0)
else:
    print(1)
    for i in range(r):
        for j in range(c):
            if m[i][j] == '.':
                m[i][j] = 'D'

for i in m:
    print(''.join(i))
