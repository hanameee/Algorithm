n, m = map(int, input().split())
a = [list(map(int, list(input().strip()))) for i in range(n)]
b = [list(map(int, list(input().strip()))) for i in range(n)]
ans = 0


# 배열의 참조값이 넘어가기때문에 배열을 그대로 바꿀 수 있다.
def flip(x, y, a):
    for i in range(3):
        for j in range(3):
            a[x+i][y+j] ^= 1  # xor 사용. 0에다 xor하면 1, 1에다 xor하면 0 되니까


# 기준점은 3*3 행렬의 첫번째 점으로 잡아주기
for i in range(n-2):
    for j in range(m-2):
        # 지금 보고 있는 점이 다르면
        if a[i][j] != b[i][j]:
            # a배열의 i,j를 기준으로 3*3 행렬을 뒤집어준다
            flip(i, j, a)
            ans += 1

if a == b:
    print(ans)
else:
    print(-1)
